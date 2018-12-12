from first import add
from first import sub
from first import mul
from first import div

while True:
    def go(x, y, s):
        x = int(input("Please enter the first number of your choice: "))
        y = int(input("Please enter the second number of your choice: "))
        s = input("I can perform addition, subtraction, division and multiplication. What do you intend to perform?")
        if (s == 'add') | (s == 'addition') | (s == 'Add') | (s == 'Addition'):
            add(x,y)
        elif (s == 'subtract') | (s == 'subtraction') | (s == 'Subtract') | (s == 'Subtraction'):
            (sub(x, y))
        elif (s == 'multiply') | (s == "multiplication") | (s == 'Multiply') | (s == 'Multiplication'):
            (mul(x, y))
        elif (s == 'divide') | (s == 'division') | (s == 'Divide') | (s == 'Division'):
            (div(x, y))
        elif s == 'q':
            print("Thank you for using the calculator! You are amazing!")
        else:
            print("This is beyond my scope of learning as of now. Please try again.")
    go(5, 6, add)
