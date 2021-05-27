# Author : Guru prasad Raju

''' This program will inverse the given list'''


from typing import List


def reversingList(list):
    # usage of python slicing function
    new_list = list[::-1]
    return new_list


# initializing new list
fresh_list = [8, 6, 7, 2, 1, 4]
print(reversingList(fresh_list))
