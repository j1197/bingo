# TODO:  try to import all of this in a single line
from first import add
from first import sub
from first import mul
from first import div

while True:
    # TODO: Why are you writing the function inside the while loop?
    def go(x, y, s):
        # TODO: Google how we can convert the input string to all lower case so that you don't have to look for
        # TODO: divide and Divide separately.
        x = int(input("Please enter the first number of your choice: "))
        y = int(input("Please enter the second number of your choice: "))
        s = input("I can perform addition, subtraction, division and multiplication. What do you intend to perform?")
        # TODO: Think of a better way of taking the string from the user. There are 8! ways in which
        # TODO: the user can write addition we can't try to catch each one of them. Same goes for other 3.
        if (s == 'add') | (s == 'addition') | (s == 'Add') | (s == 'Addition'):
            add(x,y)
        elif (s == 'subtract') | (s == 'subtraction') | (s == 'Subtract') | (s == 'Subtraction'):
            sub(x, y)
        elif (s == 'multiply') | (s == "multiplication") | (s == 'Multiply') | (s == 'Multiplication'):
            (mul(x, y))
        elif (s == 'divide') | (s == 'division') | (s == 'Divide') | (s == 'Division'):
            (div(x, y))
        elif s == 'q':
            print("Thank you for using the calculator! You are amazing!")
        else:
            print("This is beyond my scope of learning as of now. Please try again.")
    # TODO: Google and read about 'if __name__ == '__main__':'
    go(5, 6, add)

# TODO: I got NameError while trying to multiply 2 numbers. Look for TODO in first.py
# TODO: How will this code manage if I decide to quit and enter q on line 12 or 13?
# TODO: Baby doll you're not using method go correctly rethink about it
# TODO: Write appropriate commit messages, only trial 2 or T3 will not do. After reading the commit message I should
# TODO: get an idea what all logical changes have been made in that commit. So that future debugging can get a bit easy.
# TODO: You can write longer commit messages. No issues.
