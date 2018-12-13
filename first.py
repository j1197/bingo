def add(a, b):
    z = a + b
    print(z)


def mul(a, b):
    z = a * b
    print(z)


def sub(a, b):
    z = a - b
    print(z)


def div(a, b):
    if b == 0:
        print(" [ INFO] A division by zero is not possible, please give appropriate values.")
    else:
        z = a / b
        print(z)
