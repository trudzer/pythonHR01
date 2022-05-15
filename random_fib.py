import random

a = 0
b = 1
y = 0
counter = 0
x = random.randint(0, 1000)

while (x != y):
    if (y > x):
        y = y/2
        a = 0
        b = 1
        
    if (counter > 45000):
        print("\n\nUnable to match case")
        break
    y += a + b
    a = b
    b = y
    print(round(y, 2), end=", ")
    counter += 1
if (counter < 45000):
    print("\n\nNumber: " + str(x) + " was found in " + str(counter) + " iterations")
else:
    print("\nNumber: " + str(x))
