"""Trusted fixed-suite executor. No actor/profile/grader/secret mount is allowed."""
from pathlib import Path
import os
import subprocess
from review_packet import ReviewBlocked, run_suite

class DockerExecution:
    def __init__(self, root, engine_root, image, *, suite_id='project', timeout=90):
        self.root = Path(root).resolve()
        self.engine_root = str(engine_root)
        self.image = image
        self.suite_id = suite_id
        self.timeout = timeout
        if not image.startswith('sha256:'):
            raise ReviewBlocked('Test runtime must be an immutable existing image')

    def inventory(self):
        result = {}
        for path in sorted(self.root.rglob('*')):
            rel = path.relative_to(self.root)
            if any(p in {'.git', '__pycache__', '.pytest_cache'} for p in rel.parts):
                continue
            if path.is_symlink():
                raise ReviewBlocked('Symlink source requires explicit handling')
            if path.is_file():
                try: result[str(rel)] = path.read_bytes().decode('utf-8')
                except UnicodeDecodeError as error: raise ReviewBlocked('Binary source inventory unsupported') from error
        return result

    def execute(self, argv):
        command = ['docker','run','--rm','--pull','never','--user','1000:1000',
                   '--network','none','--read-only','--cap-drop','ALL',
                   '--security-opt','no-new-privileges','--memory','1g','--cpus','1',
                   '--tmpfs','/tmp:rw,size=128m', '--mount',
                   'type=bind,source='+self.engine_root+',target=/workspace,readonly',
                   '-w','/workspace','-e','PYTHONDONTWRITEBYTECODE=1','-e','PYTHONPATH=/workspace',
                   '--entrypoint','timeout',self.image,'-s','KILL',str(self.timeout),*argv]
        # The container timeout kills the suite; its nonzero status is retained.
        return subprocess.run(command, capture_output=True, text=True, timeout=self.timeout+30)

    def run(self, *, expected_digest, key):
        return run_suite(suite_id=self.suite_id,
                         argv=['python','-m','pytest','-q','-p','no:cacheprovider'],
                         expected_digest=expected_digest, inventory=self.inventory,
                         execute=self.execute, key=key, environment_id=self.image)
