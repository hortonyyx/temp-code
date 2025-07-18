

def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

x = calc(0, lambda a , b: a + b, 1, 2, 3, name = "horton", age = 24)
print(x)


