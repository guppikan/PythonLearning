
'''Write a function, add_it_up(), that takes a single integer as input and
 returns the sum of the integers from zero to the input parameter.'''


def add_it_up(n):
    try:
        result = sum(range(n+1))

    except TypeError:
        result = 0
    return result


print(add_it_up(5))
