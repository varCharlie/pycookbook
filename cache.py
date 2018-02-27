#!/usr/bin/env python3
'''
(c) 2018 charles pantoga
github: varcharlie
1e100: suspects >(/dev/tcp/`dig google.com. A`/80)
'''
from collections import OrderedDict

class Cache():
    '''Python cache decorator
    class X(object):
        @Cache
        def func(self, i):
            print i
    '''
    def __init__(self, func, size=256):
        self.func = func
        self.size = size
        self.cache = OrderedDict()

    def __repr__(self):
        return self.func.__doc__

    def __call__(self, *args, **kwds):
        key = (frozenset(args), frozenset(kwds.items()))
        if key not in self.cache:
            if len(self.cache) > self.size:
                self.cache.popitem(last=False)
            self.cache[key] = self.func(*args, **kwds)
        return self.cache[key]
