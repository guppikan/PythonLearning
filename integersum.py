'''This progamr takes a single integer as 

input and returns the sum of the integers from zero to the input parameter'''


def addGivenInput(n):
    try:
        result = sum(range(n + 1))
    except TypeError:
        result = "this is not valid postive number"
    return result


print(addGivenInput(5))
print("***************")
print(addGivenInput(-0.1))
