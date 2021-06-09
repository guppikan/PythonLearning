# Author : Guru prasad Raju

''' Function such that it can accept a variable length of 
 argument and print all arguments value'''


'''To create functions that take n number of 
 Positional arguments we use * with arguments
'''


def newfunction(*args):
    for i in args:
        print(i)


newfunction(10, 20, 30, 40.50)

# new function with string values
print("******************")

newfunction("Hello", "world", "new")
