ARRAY = [1, 3, 6, 4, 8, 2, 11, 5, 9, 7, 12, 10]

def FUNC_1(a, x, y):
    z = a[x]
    a[x] = a[y]
    a[y] = z

def FUNC_2(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] > x[i]):
                FUNC_1(x, i, j)
                
def FUNC_3(x):
    FUNC_2(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[j] % 2 == 0):
                if (x[j] > x[i]):
                    FUNC_1(x, i, j)
                FUNC_1(x, i, j)
                
print("ARRAY:\t" + str(ARRAY))
print("-" * 55)
FUNC_3(ARRAY)
print("FUNC_3:\t" + str(ARRAY))
print("-" * 55)
FUNC_2(ARRAY)
print("FUNC_2:\t" + str(ARRAY))
