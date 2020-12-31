# this program will print if given number is prime or not in a range

startingNumber = 11
endginNumber = 35

for i in range(startingNumber, endginNumber):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)
