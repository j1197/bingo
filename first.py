print("Welcome")


def add(a, b):
    z = a + b
    print(z)

# TODO: I guess there is some serious issue with this function
def mul(a, b):
    z = a * b
    print(z)


def sub(a, b):
    if a > b:
        z = a - b
        print(z)

    else: # TODO: Why you're not giving negative output?
        print(" Please give appropriate values.")  # TODO: Extra space at the beginning of sentence.


def div(a, b):
    if b == 0:
        print("A division by zero is not possible, please give appropriate values.")
        # TODO: What do you think about this?
        # print("[INFO] A division by zero is not possible, please give appropriate values.")

    else:
        z = a / b
        print(z)
