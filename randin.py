'''
(c) 2018 charles pantoga
github: varcharlie
1e100: suspects >(/dev/tcp/`dig google.com. A`/80)
'''
import os
import io

BLOCK_SIZE = 4096
DEV_URANDOM = '/dev/urandom'

def getrandbytes(nbytes=BLOCK_SIZE//8, nskip=BLOCK_SIZE, device=DEV_URANDOM):
    '''Returns `nbits` random bytes, where `nbytes` is an integer > 0.
    * Bytes are read from `device`, which should either be /dev/urandom,
        /dev/random, or some other file-like device that produces
        sufficiently random bits.
    * Skip `nskip` bytes before reading random bytes.
    '''
    randfd = os.open(device, os.O_RDONLY | os.O_NONBLOCK)
    randombytes = os.pread(randfd, nbytes, nskip)
    os.close(randfd)
    return randombytes
