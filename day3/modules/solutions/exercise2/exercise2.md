1. Importing the entire package is as easy as: `import exercise2`. This assumes that `exercise2` directory is on your path, or you are in the same directory as `exercise2` (or whatever you named your package).
    - You can verify this in a script or the REPL by using the `dir()` function:
```
>>> import exercise2
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'exercise2']
>>> dir(exercise2)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'func1', 'func2', 'func3', 'mod1', 'mod2', 'mod3']
>>>
```
2. Importing an individual function is also straight forward: `from exercise2 import func3`:
```
>>> from exercise2 import func3
>>> func3()
func3
>>>
```
