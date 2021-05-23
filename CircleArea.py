# Author : Guru prasad Raju

''' This program calculate circle area'''


def calculateArea(radius):
    PI = 3.14
    return PI * (radius*radius)


# Circle 1
calculated_area = calculateArea(4)
print(f"{calculated_area} is the area of Circle 1")

# Circle 2
calculated_area = calculateArea(5)
print(f"{calculated_area} is the area of Circle 2")

# Circle 3
calculated_area = calculateArea(6)
print(f"{calculated_area} is the area of Circle 3")
