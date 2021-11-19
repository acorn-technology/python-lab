# Modules with __init__.py

Python packages can contain a `__init__.py` file meant for initialization of packages, but it also has an impact on module loading.

Before Python 3.3 it was compulsary with an `__init__.py` file in a folder to make it into a package. With 3.3 (PEP 420) Python included implicit namespace packages. Which meant that a folder without an `__init__.py` file  is considered a namespace package. This is however slightly different from a regular package which we will see below.

In the file structure, there are examples of two directories with the same name but with differing content

```
first
  foo
    a.py
second
  foo
    b.py
```

There are three versions of this structure.
* *no_init*: None of the folders have an `__init__.py`
* *partial_init*: Only `second/foo` has an `__init__.py`
* *with_init_*: Both `first/foo` and `second/foo` has an `__init__.py`

In your personal folder, create a file with the following content

```python
from pathlib import PurePath
import sys

dir = PurePath(__file__).parent.parent

sys.path.append(str(dir.joinpath('no_init', 'first')))
sys.path.append(str(dir.joinpath('no_init', 'second')))

try:
    import foo.a as a
    print(a.a_name)
except ImportError as e:
    print(e)

try:
    import foo.b as b
    print(b.b_name)
except ImportError as e:
    print(e)
```

Running the file should print the two module names

```
foo.a
foo.b
```

This is because Python sees the `foo` folder as a namespace package and therefore creates a package containing both `a` and `b`.

Now, modify the path that is added to sys.path to include `partial_init` instead of `no_init`.

```python
sys.path.append(str(dir.joinpath('partial_init', 'first')))
sys.path.append(str(dir.joinpath('partial_init', 'second')))
```

Running the file will give you a different output

```
No module named 'foo.a'
foo.b
```

Python will first find `first/foo` and treat it as a namespace package. Secondly it will find `second/foo` which due to the `__init__.py` is treated as a regular package. A regular package means a package that is contained in a single folder. Which in turn means that it only contains `b`.

Now for the last version, modify the path so we use `with_init`

```python
sys.path.append(str(dir.joinpath('with_init', 'first')))
sys.path.append(str(dir.joinpath('with_init', 'second')))
```

Running this will again change the output

```
foo.a
No module named 'foo.b'
```

In this version, both `first/foo` and `second/foo` are regular packages (single folder packages). The fact that `first/foo` is added before `second/foo` means that it is the one that will be imported.

So should we use a `__init__.py` or not? There are plenty of tooling that relies heavily on `__init__.py`. That together with that many might find the automatic merging of packages unexpected means that it is best to always create an `__init__.py` except when package merging is explicitly wanted.