# Author : Guru prasad Raju

''' This program will print index of each characters in the string'''


def givenString(new_string):
    for i in range(len(new_string)):
        print("index[", i, "]", new_string[i])


givenString("Life")
