# Author : Guru prasad Raju
'''This program will create inner and outer function 
 within function avoid loop'''

# creating a function


def outerFunction(a, b):
    claculating_square = a**2
    # creating inner function

    def innerFunction(a, b):
        return a+b

    addPlusFive = innerFunction(a, b)
    return addPlusFive+5


# calling function
finalResult = outerFunction(7, 8)
print(f'Printing value of outer function:{finalResult}')
