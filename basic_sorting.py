ARRAY = [1, 3, 6, 4, 8, 2, 11, 5, 9, 7, 12, 10]
EVEN = []
ODD = []

"""Swap 2 elements of an array"""
def swapElements(a, x, y):
    z = a[x]
    a[x] = a[y]
    a[y] = z

"""Sort array from lowest to highest""" 
def sortArray(x):
    [swapElements(x, i, j) for i in range(len(x)) for j in range(len(x)) if (x[j] > x[i])]
                
"""Display odd numbers first in ascending order, then even numbers in descending order"""
def oddThenEven(x):
    sortArray(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] % 2 == 0):
                if (x[j] > x[i]):
                    swapElements(x, i, j)
                    if (x[i] not in EVEN):
                        EVEN.append(x[i])
                swapElements(x, i, j)
            if (x[i] not in EVEN and x[i] not in ODD):
                ODD.append(x[i])
   
"""Add together all the numbers for each array and display the sum"""
def addTogether():
    x = 0
    y = 0
    z = 0
    for i in ODD: z += i; x += i
    for i in EVEN: z += i; y += i
    print("SUM OF EVEN:\t" + str(y))
    print("-" * 55)
    print("SUM OF ODD:\t\t" + str(x))
    print("-" * 55)
    print("SUM OF ALL:\t\t" + str(z))
                
def main():
    print("ORIGINAL ARRAY:\t" + str(ARRAY))
    print("-" * 55)
    oddThenEven(ARRAY)
    print("ODD THEN EVEN:\t" + str(ARRAY))
    print("-" * 55)
    sortArray(ARRAY)
    print("SORTED ARRAY:\t" + str(ARRAY))
    print("-" * 55)
    print("EVEN ARRAY:\t\t" + str(EVEN))
    print("-" * 55)
    print("ODD ARRAY:\t\t" + str(ODD))
    print("-" * 55)
    addTogether()
    
if (__name__ == "__main__"):
    main()
