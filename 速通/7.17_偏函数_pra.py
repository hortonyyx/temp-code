import functools

int2 = functools.partial(int, base=2)
int3 = functools.partial(int, base=3)
int4 = functools.partial(int, base=4)
int5 = functools.partial(int, base=5)

print(int2('100'))
print(int3('100'))
print(int4('100'))