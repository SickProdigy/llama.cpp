"""Local Gitea text-read defaults using Hermes's supported pre-tool hook."""
from pathlib import PurePosixPath

_TOOL = 'mcp__mcp_gitea_hermes__get_file_contents'
_BINARY = {'.png','.jpg','.jpeg','.gif','.webp','.ico','.pdf','.zip','.gz','.7z','.tar','.woff','.woff2','.ttf','.mp3','.mp4','.ogg','.sqlite','.db','.gguf'}

def readable_defaults(tool_name='', args=None, **kwargs):
    if tool_name != _TOOL or not isinstance(args, dict):
        return None
    if PurePosixPath(str(args.get('path') or '')).suffix.lower() in _BINARY:
        return None
    # Explicit raw reads and invalid values belong to the caller/tool validation.
    if 'with_lines' in args and args['with_lines'] is not True:
        return None
    changes = {}
    if 'with_lines' not in args:
        changes['with_lines'] = True
    start = args.get('start_line')
    if 'start_line' not in args:
        start = 1
        changes['start_line'] = start
    if isinstance(start, int) and not isinstance(start, bool) and start >= 1:
        if 'end_line' not in args:
            changes['end_line'] = start + 159
    return {'action': 'modify', 'args': changes} if changes else None

def register(ctx):
    ctx.register_hook('pre_tool_call', readable_defaults)
