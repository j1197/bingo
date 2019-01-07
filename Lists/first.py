def makinglists():
    numbers = input("Please enter your numbers: ")
    delimiter = ','
    l = numbers.split(delimiter)
    print("Your list is: ",l)
    t = tuple(l)
    print("Your tuple is: ",t)


makinglists()