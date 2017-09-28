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
        argstr = ', '.join(args)
        kwstr = ', '.join('{}={}'.format(k, v) for k, v in kwds.iteritems())
        text = ''
        if func.__module__ in ('__builtin__', '__main__'):
            text += '{}('.format(func.__name__)
        else:
            text += '{}('.format('.'.join((func.__module__, func.__name__)))
        if args:
            text += ', '.join("'{}'".format(_) for _ in args)
        if kwds:
            if args:
                text += ', '
            text += ', '.join('{}={}'.format(k, v) for k, v in kwds.iteritems())
        text += ')\n'
        sys.stdout.write(text)
        return None
    return wrapper
