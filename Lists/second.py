'''Question: (Complete this in 2 hours max)
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''

from math import sqrt


def weird_square_root():
    ip = input("Please give numbers: ")
    delimiter = ','                       
    separated = ip.split(delimiter)
    a = []
    for number in separated:
        d = int(number)
        c = 50
        h = 30
        q = str(int((sqrt(2*c*d/h))))
        a.append(q)
        delimiter = ','
        s = delimiter.join(a)
    print(s)


weird_square_root()
