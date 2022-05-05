ARRAY = [1, 3, 6, 4, 8, 2, 11, 5, 9, 7, 12, 10]

def swap(a, x, y):
    z = a[x]
    a[x] = a[y]
    a[y] = z

def sortArray(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] > x[i]):
                swap(x, i, j)
                
def oddThenEven(x):
    sortArr(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] % 2 == 0):
                if (x[j] > x[i]):
                    swap(x, i, j)
                swap(x, i, j)
                
print("ARRAY:\t" + str(ARRAY))
print("-" * 55)
oddThenEven(ARRAY)
print("ODD THEN EVEN:\t" + str(ARRAY))
print("-" * 55)
sortArr(ARRAY)
print("SORTED ARRAY:\t" + str(ARRAY))
