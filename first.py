print("Welcome")


def add(a, b):
    z = a + b
    print(z)


def mul(a, b):
    z = a * b
    print(z)


def sub(a, b):
    if a > b:
        z = a - b
        print(z)

    else:
        print(" Please give appropriate values.")


def div(a, b):
    if b == 0:
        print("A division by zero is not possible, please give appropriate values.")

    else:
        z = a / b
        print(z)
