'''
(c) 2018 charles pantoga
github: varcharlie
1e100: suspects >(/dev/tcp/`dig google.com. A`/80)
'''
import functools
import copy

def reset_defaults(func):
    @functools.wraps(func)
    def _closure(*args, **kwds):
        func_defaults = copy.deepcopy(func.__defaults__)
        func_kwdefaults = copy.deepcopy(func.__kwdefaults__)
        result = func(*args, **kwds)
        setattr(func, '__defaults__', func_defaults)
        setattr(func, '__kwdefaults__', func_kwdefaults)
        return result
    return _closure
