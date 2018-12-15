import first


def go_away():
    print("Thank you for using the calculator! You are amazing!")
    exit()


def calculating():
    x = input("Please enter the first number of your choice: ")
    if x == 'q':
        go_away()
    else:
        x = int(x)
        y = input("Please enter the second number of your choice: ")
        if y == 'q':
            go_away()
        else:
            y = int(y)
            print("I can perform addition, subtraction, division and multiplication. What do you intend to perform?")
            s = input("Please type the initials for each operation.")
            s = s.lower()
            if s == 'a':
                first.add(x, y)
            elif s == 's':
                first.sub(x, y)
            elif s == 'm':
                first.mul(x, y)
            elif s == 'd':
                first.div(x, y)
            elif s == 'q':
                go_away()
            else:
                print("This is beyond my scope of learning as of now. Please try again.")


while True:
    if __name__ == "__main__":
        print("Calc2.py is being run directly.")
    else:
        calculating()





