from pathlib import PurePath
import sys

dir = PurePath(__file__).parent.parent


# sys.path.append(str(dir.joinpath('no_init', 'first')))
# sys.path.append(str(dir.joinpath('no_init', 'second')))

sys.path.append(str(dir.joinpath('partial_init', 'first')))
sys.path.append(str(dir.joinpath('partial_init', 'second')))

# sys.path.append(str(dir.joinpath('with_init', 'first')))
# sys.path.append(str(dir.joinpath('with_init', 'second')))

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
