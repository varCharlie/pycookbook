# pycookbook
This is meant to be a repository to store useful or useless code written in python.

## noop.py
Sometimes it is useful to add a 'noop' flag to a programs options. This module contains a decorator `noop` which will write functions to stderr instead of executing them. It is useful to make sure your code is sane before running it, when running it may have irreversable side effects. Consider code that may send a network packet or even wipe a computer clean, overwriting the harddrive with 0s.

Example:
```bash
$ charlie on macbook in ~/src/pycookbook
✭ (git) working on branch  master ✘
❯❯ python -i noop.py
>>>
>>> # builtins:
...
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'functools', 'noop', 'sys']
>>> sum([1,2,3])
6
>>> hash(5)
5
>>> dir = noop(dir)
>>> sum = noop(sum)
>>> hash = noop(hash)
>>>
>>> hash()
(noop): hash()
>>> sum([1,2,3])
(noop): sum([1, 2, 3])
>>> dir()
(noop): dir()
>>> hash(5)
(noop): hash(5)
>>>
>>> @noop
... def somefunc(*args, **kwargs):
...     pass
...
>>> somefunc()
(noop): somefunc()
>>> somefunc(1,2,3)
(noop): somefunc(1, 2, 3)
>>> somefunc(1,2,3,'a')
(noop): somefunc(1, 2, 3, 'a')
>>> somefunc(1,2,3,'a', b=True, c={}, d={1:1})
(noop): somefunc(1, 2, 3, 'a', c={}, b=True, d={1: 1})
>>> somefunc(auth="Charlie")
(noop): somefunc(auth='Charlie')
>>>
>>> # import a module
>>>
>>> import requests
>>> requests.get = noop(requests.get)
>>> requests.get('http://domain', data={}, auth=('user','pass'))
(noop): requests.api.get('http://domain', data={}, auth=('user', 'pass'))
>>>
>>> # Function you can't recover from:
>>>
>>> import sys
>>> exit = sys.exit
>>> sys.exit = noop(sys.exit)
>>> sys.exit()
(noop): sys.exit()
>>> exit()
```

## resetdefaults.py
Since python has higher order functions, mutable default arguments do not always work as one might expect. They are similar to the way C handles static variable declarations inside a function definition -- that is to say they retain their value throughout function calls.

Consider the following code:
```python
def func(x=[]):
    if not x:
        x.append(1)
    else:
        x.append(x[-1]+1)
    return x
```

Calling this function multiple times with no arguments does the following:
```python
>>> func()
[1]
>>> func()
[1, 2]
>>> func()
[1, 2, 3]
```

Ruby developers might not expect this. Heres the same code in ruby:
```ruby
def func(x = [])
  if x.empty?
    x << 1
  else
    x << x[-1]+1
  end
end
```

Calling this code in ruby works differently:
```ruby
irb(main):025:0> func()
=> [1]
irb(main):026:0> func()
=> [1]
```

This is because ruby does not have first class functions.

### resetdefaults.py to the rescue
`resetdefaults.py` contains a function that can be used as a decorator to achieve the ruby behavior in Python.

```python
>>> @reset_defaults
... def func(x=[]):
...     if not x:
...         x.append(1)
...     else:
...         x.append(x[-1]+1)
...     return x
...
>>> func()
[1]
>>> func()
[1]
>>> func()
[1]
```

### randbin.py
*Forthcoming*

### memstate.py
*Forthcoming*

### cache.py
*Forthcoming*
