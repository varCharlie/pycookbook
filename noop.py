#!/usr/bin/env python2
'''
`noop` is a decorator that will print out a function call
instead of executing it.
'''

import functools
import sys

def noop(func):
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        text = '(noop): '
        if func.__module__ in ('__builtin__', '__main__'):
            text += '{}('.format(func.__name__)
        else:
            text += '{}('.format('.'.join((func.__module__, func.__name__)))
        if args:
            text += ', '.join("'{}'".format(_) if isinstance(_, str) else str(_)
                                for _ in args)
        if kwds:
            if args:
                text += ', '
            text += ', '.join('{}={}'.format(k, "'%s'" % v if isinstance(v, str) else v)
                                for k, v in kwds.iteritems())
        text += ')\n'
        sys.stderr.write(text)
        return None
    return wrapper
