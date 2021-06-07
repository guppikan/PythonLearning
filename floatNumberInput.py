# Author : Guru prasad Raju

''' Accept a list of 5 float numbers as an input from the user'''

floatNumbers = []
number = int(input("Enter the list size :"))
for i in range(0, number):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

print("The user list is", floatNumbers)
