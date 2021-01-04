# this programe showcase boolean operation
'''Python boolean operators are spelled out as the words "and" "or" "not",
 instead of the && syntax in other languages.'''


def a_bigger(a, b):
    if a > b and (a-b) >= 2:
        return True
    else:
        return False


a_bigger(0, 2)
