# Setup

In this lab we are going to ensure that we have a functioning environment and can write basic tests.

## Debug

Follow the instructions of your IDE and debug the file `debuggable.py`.

* Set a breakpoint on line 3 and check that it is hit
* Ensure that you can inspect the msg variable

## Testing

While doing the labs you might want to write a few test, so we will go through a small introduction to testing in Python.

### Setup

We will not use the built in test runner (`unittest`) but [`pytest`](https://docs.pytest.org/en/latest/contents.html). Install it by running

```
pip install --user pytest
```

* Check that you didn't see a warning about that the installation folder is not in path. (Add folder to path if warning is present)

### Run tests

1. Open a terminal in the folder for this lab.
2. Run `pytest`
3. The output should show one test passed and one failed

###  Writing tests

The simplest form of tests written for pytest is to have simple functions in a file. For the tests to be run the name of the file as well as the name of the functions should start with `test_`.

Example: `test_stuff.py`
```python
def test_foo():
  pass
```

Assertions are written with Pythons standard `assert`

```python
def test_foo():
    assert 4 < 7, "The world is strange"
```

Tests can be grouped in classes which then should have the prefix `Test`. Tests are then written as methods on the class. They should still be prefixed with `test_` and are expected to take one argument called `self`. We will look more into classes, inheritance, etc in a later lab.

```python
class TestStuff:
    def test_foo(self):
        pass
```

If you want to split the implementation and the tests into seperate files, then the functions to be tested needs to be imported. Modules will also be discussed at a later lab.

Given a `file.py`:
```python
def last_lines(file):
    ...

if __name__ == "__main__":
    ...
```

The `if` statemenet will ensure that the code is not evaluated when imported but only when run as a script.

When testing this implementation we can have a test file

`test_file.py`
```python
from file import last_lines

def test_single_line():
    last_line(...
```