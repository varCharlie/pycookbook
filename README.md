# pycookbook
This is meant to be a repository to store useful or useless code written in python.

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
