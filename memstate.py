#!/usr/bin/env python3
'''
(c) 2018 charles pantoga
github: varcharlie
1e100: suspects >(/dev/tcp/`dig google.com. A`/80)
'''
from sys import stderr

def proc_mem():
    def hexaddress(x):
        return hex(id(x))
    memory = {}
    for identifier, code in globals().items():
        memory[hexaddress(code)] = identifier
    return memory
