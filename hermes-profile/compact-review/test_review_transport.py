from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
import threading
import time
import unittest
from review_transport import TimedReview, request_body, publication_review
from review_packet import ReviewBlocked

class TransportTests(unittest.TestCase):
    def server(self, content, *, pause=0, extra_length=0, malformed=False):
        reply = b'not-json' if malformed else json.dumps({'choices':[{'finish_reason':'stop','message':{'content':json.dumps(content)}}],
                                                       'usage':{'prompt_tokens':123,'completion_tokens':7}}).encode()
        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers['Content-Length']))
                self.send_response(200);self.send_header('Content-Length',str(len(reply)+extra_length));self.end_headers()
                self.wfile.write(reply[:1024]);self.wfile.flush()
                if pause:time.sleep(pause)
                self.wfile.write(reply[1024:]);self.wfile.flush()
            def log_message(self,*a):pass
        server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        thread=threading.Thread(target=server.serve_forever,kwargs={'poll_interval':0.01},daemon=True);thread.start()
        self.addCleanup(thread.join);self.addCleanup(server.server_close);self.addCleanup(server.shutdown)
        return 'http://127.0.0.1:'+str(server.server_port),reply

    def test_complete_large_body_survives_caller_expiry(self):
        content={'decision':'revise','findings':['x'*40000]};endpoint,raw=self.server(content,pause=.1)
        with tempfile.TemporaryDirectory() as temp:
            request=TimedReview(endpoint,{'probe':True},Path(temp)/'record',caller_seconds=.01,socket_seconds=2).start()
            caller=request.caller_result();self.assertFalse(caller['caller_completed'])
            capture=request.join_capture(3)
            self.assertTrue(capture['body_complete']);self.assertEqual(capture['captured_bytes'],len(raw))
            self.assertEqual(capture['parsed_review'],content)
            self.assertEqual((Path(temp)/'record/response.bin').read_bytes(),raw)
            self.assertFalse(json.loads((Path(temp)/'record/caller.json').read_text())['caller_completed'])

    def test_incomplete_body_is_retained_but_not_parsed_as_success(self):
        endpoint,raw=self.server({'decision':'approve'},extra_length=10)
        with tempfile.TemporaryDirectory() as temp:
            request=TimedReview(endpoint,{},Path(temp)/'record',caller_seconds=1,socket_seconds=1).start()
            request.caller_result();capture=request.join_capture(2)
            self.assertFalse(capture['body_complete']);self.assertIn('error',capture)
            self.assertEqual(capture['captured_bytes'],len(raw));self.assertNotIn('parsed_review',capture)

    def test_malformed_outer_json_is_not_a_verdict(self):
        endpoint,_=self.server({},malformed=True)
        with tempfile.TemporaryDirectory() as temp:
            request=TimedReview(endpoint,{},Path(temp)/'record',caller_seconds=1,socket_seconds=1).start()
            request.caller_result();capture=request.join_capture(2)
            self.assertTrue(capture['body_complete']);self.assertIn('error',capture);self.assertNotIn('parsed_review',capture)

    def test_late_or_length_limited_valid_json_cannot_authorize(self):
        good={'caller_completed':True,'capture':{'body_complete':True,'finish_reason':'stop','parsed_review':{'decision':'approve'}}}
        self.assertEqual(publication_review(good),{'decision':'approve'})
        for item in [dict(good,caller_completed=False),dict(good,capture={**good['capture'],'finish_reason':'length'})]:
            with self.assertRaises(ReviewBlocked): publication_review(item)

    def test_request_schema_is_bound_to_packet(self):
        body=request_body({'packet_id':'example'},'local-model')
        schema=body['response_format']['json_schema']['schema']
        self.assertEqual(schema['properties']['packet_id']['enum'],['example'])
        self.assertEqual(body['max_tokens'],1024);self.assertFalse(body['stream'])
        self.assertNotIn('tools',body)

if __name__=='__main__':unittest.main()
