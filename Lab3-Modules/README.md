# Modules

In this lab we will have a look at modules and OOP in Python.

## 1 Working with modules

### 1.1 Create and import
In Python, code is organized in files where each file is a module. Create file called `io_utils.py` with the following content.

```python
def shout(msg):
    print(msg.upper())

def shout_name():
    shout(__name__)
```

Create a second file called `io_usage.py` that imports `shout` from `io_utils.py` and uses it to print the `__name__` variable (e.g. `io_utils.shout(__name__)`).

_Note:_ Do you know how to import it so the usage becomes `io_utils.shout(...)` or just `shout(...)` or perhaps `oi.shout(...)`

The output when running `io_usage.py` will hopefully be

```
__MAIN__
```

The reason for this is that the `__name__` variable  will contain the name of the module where the code is located or if the file is run a script, it will contain the string `__main__`.

### 1.2 Use shout_name

Add an import of the `shout_name` function in `io_usage.py` and call it. What does it print and why?

### 1.3 Relative imports

Create a file called `game.py` and import the class `Bug` from `bug.py` in the lab folder.

When you run the file you should get the following error:

```
ImportError: attempted relative import with no known parent package
```

This gives us an opportunity to try to understand an error that might not be easy to interpret when first encountered. It will however hopefully become clear from the following example. Which also gives us a little more insight into Python modules.

The folder `import_example` contains three files

`a.py`:
```python
from foo.b import b_name
from foo.bar.c import c_name

print(f'a: {__name__}')
print(f'b: {b_name}')
print(f'c: {c_name}')
```

`b.py`:
```python
b_name = __name__

if __name__ == '__main__':
    from bar.c import c_name
    
    print(f'b: {b_name}')
    print(f'c: {c_name}')
```

`c.py`:
```python
c_name = __name__
```

In the following structure

```
a.py
foo
  b.py
  bar
    c.py
```

Run `a.py` and it will print

```
a: __main__
b: foo.b
c: foo.bar.c
```

If you instead run `b.py` it will print

```
b: __main__
c: bar.c
```

Here we see that the module name of relative modules depends on where it is loaded from (as well as the script that is run is named `__main__`).

If you in c.py add the lines

```python
from ..b import b_name
print(f'relative b: {b_name}')
```

and re-run `a.py`, you get the output.

```
relative b: foo.b
a: __main__
b: foo.b
c: foo.bar.c
```

We can see that from `c.py` it goes two steps above its name `foo.bar.c -> foo` and looks for `b`. Which means it correctly imports `foo.b`.

If you however now run `b.py`, you get the following error
```
ImportError: attempted relative import beyond top-level package
```

From the earlier run of `b.py` we saw that `c_name` was `bar.c`. If we try to go two steps up there is nothing left. I.e we go past the top-level package `bar`.

We are now in a better position to understand the initial error

```
ImportError: attempted relative import with no known parent package
```

Here we have a relative import from the file that we are running (i.e `__name__ == '__main__'` ). That means that we have absolutely no way of going to steps up.

So how do we fix this?

1. We could in another scenario modify our folder structure so it better fits Python's import behaviour. _This is very likely what you would like to do in a real scenario._
2. We could add the `Lab3-Modules` as a path to be search for modules (either by modifying environment variable `PYTHONPATH` or in runtime by modifying [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path)). _This is generally not a very good idea._
3. Instead of running a script, we can tell Python to run a module (e.g. `python -m Lab3-Modules.Mattias.game.py`). _This is what we will do this time._

## 2 Classes

All work in this part will be performed in the `game` module we created before.

### 2.1 Subclass

Create a class `Ant` that inherits from `Bug` in the `bug` module. Make sure it is possible to instantiate it.

Add a method called `move` that makes the ant take one step forward using `Bug._step()`. Printing the y-position before and after.

Create an Ant, take a step and verify that it works.

### 2.2 Name mangling

Modify the `move` method to use `Bug.__y` instead of `Bug.y`.

### 2.3 [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant)

Implement a game where [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) plays out using the `Ant` class and some additional classes that you create.

The game should be drawn on a 40x40 board (ASCII in console works great) where the ant starts at position 20, 20 and performs 500 moves.

### 2.4 Additional fun

What happens if you add in a second ant?

How can you handle a game where the ant is allowed to move 1x10^3 times, 1x10^6 times?