# Author : Guru prasad Raju

''' This program inverse the given array'''


def inverseArray(arr, n, d):
    # creating temp array
    temp = []
    # initialzing varible i
    i = 0
    while(i < d):
        temp.append(arr[i])
        i = i+1

    i = 0
    while(d < n):
        arr[i] = arr[d]
        i = i+1
        d = d+1

    arr[:] = arr[:i]+temp
    return arr


# A function to test above inverseArray
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(inverseArray(arr, len(arr), 2))
