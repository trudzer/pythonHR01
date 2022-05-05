ARRAY = [1, 3, 6, 4, 8, 2, 11, 5, 9, 7, 12, 10]

"""Swap 2 elements of an array"""
def swapElements(a, x, y):
    z = a[x]
    a[x] = a[y]
    a[y] = z

"""Sort array from lowest to highest""" 
def sortArray(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] > x[i]):
                swapElements(x, i, j)
                
"""Display odd numbers first in ascending order, then even numbers in descending order"""
def oddThenEven(x):
    sortArray(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] % 2 == 0):
                if (x[j] > x[i]):
                    swapElements(x, i, j)
                swapElements(x, i, j)
                
print("ARRAY:\t\t" + str(ARRAY))
print("-" * 55)
oddThenEven(ARRAY)
print("ODD THEN EVEN:\t" + str(ARRAY))
print("-" * 55)
sortArray(ARRAY)
print("SORTED ARRAY:\t" + str(ARRAY))
