from first import *


def calculating():
    while True:
        print(
            "I can perform addition, subtraction, division and multiplication. What do you intend to "
            "perform?\nOr press 'q' to exit the calculator.\n----------------------")
        s = input("Please type the initials for the operation: ").lower()
        if s == 'q':
            print('I hope you enjoyed this!')
            quit()
        else:
            try:
                x = int(input("Please enter the first number of your choice: "))
                y = int(input("Please enter the second number of your choice: "))
                if s == 'a':
                    add(x, y)
                elif s == 's':
                    sub(x, y)
                elif s == 'm':
                    mul(x, y)
                elif s == 'd':
                    div(x, y)
                else:
                    print("\n[WARNING] Please enter correct initial!\n")
            except ValueError:
                print('\n[WARNING] Please enter a number!\n')


if __name__ == '__main__':
    calculating()
