import os
from base64 import b64encode
from sys import stdout

def imgcat(data, inline=1, filename=''):
    buf = bytes()
    enc = 'utf-8'

    is_tmux = os.environ['TERM'].startswith('screen')

    # OSC
    buf += b'\033'
    if is_tmux: buf += b'Ptmux;\033\033'
    buf += b']'

    buf += b'1337;File='

    if filename:
        buf += b'name='
        buf += b64encode(filename.encode(enc))

    buf += b';size=%d' % len(data)
    buf += b';inline=%d' % int(inline)
    buf += b':'
    buf += b64encode(data)

    # ST
    buf += b'\a'
    if is_tmux: buf += b'\033\\'

    buf += b'\n'

    stdout.buffer.write(buf)
    stdout.flush()

