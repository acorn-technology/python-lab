from foo.b import b_name
from foo.bar.c import c_name

print(f'a: {__name__}')
print(f'b: {b_name}')
print(f'c: {c_name}')