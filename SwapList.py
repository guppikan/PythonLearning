# Author : Guru prasad Raju

''' This program will swap first and last element given list'''


def swapGivenList(newList):
    # here newList[-1] is last element in list
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


# calling function
newList = [16, 17, 18, 19, 20]
print(swapGivenList(newList))
