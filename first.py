print("Welcome")


def add(x, y):
    z = x + y
    print(z)


def mul(x, y):
    z = x * y
    print(z)


def sub(x, y):
    if x >> y:
        z = x - y
        print(z)

    else:
        print(" Please give appropriate values.")


def div(x, y):
    if y == 0:
        print("A division by zero is not possible, please give appropriate values.")

    else:
        z = x / y
        print(z)
