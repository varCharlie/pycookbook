'''
(c) 2018 charles pantoga
github: varcharlie
1e100: suspects >(/dev/tcp/`dig google.com. A`/80)
'''
import functools
import copy

def reset_defaults(func):
    '''Decorator that forces default arguments to be re-initialized
    with every invocation. Similar to Ruby's behavior.

    IE:
    >>> @resetdefaults
    ... def example(k, v, x={}):
    ...   x[k] = v
    ...   print(x)
    >>> example(1,1)
    {1: 1}
    >>> example(5,5)
    {5: 5}
    >>> example(3,3)
    {3: 3}
    '''
    @functools.wraps(func)
    def _closure(*args, **kwds):
        func_defaults = copy.deepcopy(func.__defaults__)
        func_kwdefaults = copy.deepcopy(func.__kwdefaults__)
        result = func(*args, **kwds)
        setattr(func, '__defaults__', func_defaults)
        setattr(func, '__kwdefaults__', func_kwdefaults)
        return result
    return _closure
