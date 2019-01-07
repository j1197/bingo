'''Write a program that accepts a comma separated sequence of words as input and prints the words
in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''


def sort_words():
    ip = input("Please print words in a comma-separated sequence: ")
    delimiter = ','
    separated = ip.split(delimiter)
    separated.sort()
    for word in separated:
        delimiter = ','
        s = delimiter.join(separated)
    print(s)




sort_words()