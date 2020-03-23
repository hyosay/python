from pip._vendor.distlib.compat import raw_input


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b

a = 10
b = 20

cmd = input()
print(eval(cmd))