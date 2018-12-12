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


while True:
    def go(x, y, s):
        x = int(input("Please enter the first number of your choice: "))
        y = int(input("Please enter the second number of your choice: "))
        s = input("I can perform addition, subtraction, division and multiplication. What do you intend to perform?")
        if (s == 'add') | (s == 'addition') | (s == 'Add') | (s == 'Addition'):
            add(x, y)
        elif (s == 'subtract') | (s == 'subtraction') | (s == 'Subtract') | (s == 'Subtraction'):
            sub(x, y)
        elif (s == 'multiply') | (s == "multiplication") | (s == 'Multiply') | (s == 'Multiplication'):
            mul(x, y)
        elif (s == 'divide') | (s == 'division') | (s == 'Divide') | (s == 'Division'):
            div(x, y)
        elif s == 'q':
            print("Thank you for using the calculator! You are amazing!")
        else:
            print("This is beyond my scope of learning as of now. Please try again.")
    go(5, 6, add)
