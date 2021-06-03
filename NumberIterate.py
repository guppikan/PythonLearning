# Author : Guru prasad Raju

'''  1. range of the first 10 numbers 
     2.Iterate from the start number to the end number
     3. In each iteration print the sum of the current 
     number and previous number'''


def sumNumbers(number):
    previousNumber = 0
    for i in range(number):
        sumNumbers = previousNumber+i
        print(
            f"Current number is {i},and previous number is {previousNumber} :", sumNumbers)
        previousNumber = i


sumNumbers(10)
