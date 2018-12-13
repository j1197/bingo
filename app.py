from first import add, sub, mul, div


def go(x, y, s):
    x = input("Please enter the first number of your choice: ")
    if x == 'q':
        print("Thank you for using the calculator! You are amazing!")
    else:
        x = int(x)
    y = input("Please enter the second number of your choice: ")
    if y == 'q':
        print("Thank you for using the calculator! You are amazing!")
    else:
        y = int(y)
    s = input("I can perform addition, subtraction, division and multiplication. What do you intend to perform?")
    s = s.lower()
        # TODO: Think of a better way of taking the string from the user. There are 8! ways in which

    if (s == 'add') | (s == 'addition'):
        add(x,y)
    elif (s == 'subtract') | (s == 'subtraction'):
        sub(x, y)
    elif (s == 'multiply') | (s == "multiplication"):
        mul(x, y)
    elif (s == 'divide') | (s == 'division'):
        div(x, y)
    elif s == 'q':
        print("Thank you for using the calculator! You are amazing!")
    else:
        print("This is beyond my scope of learning as of now. Please try again.")
    # TODO: Google and read about 'if __name__ == '__main__':'


while True:
    go(5, 6, add)


# TODO: Baby doll you're not using method go correctly rethink about it
# TODO: Write appropriate commit messages, only trial 2 or T3 will not do. After reading the commit message I should
# TODO: get an idea what all logical changes have been made in that commit. So that future debugging can get a bit easy.
# TODO: You can write longer commit messages. No issues.
