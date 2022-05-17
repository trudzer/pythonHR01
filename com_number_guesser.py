import random

num = random.randint(0, 1000000)
it = random.randint(0, 1000000)
counter = 0
newLow = 0
newHigh = 1000000

formNum = "{:,}".format(num)
print("THE NUMBER: " + str(formNum))
print("----------------------------")
while (counter < 1000000):
    if (num == it):
        print("Number found after {} tries".format(counter))
        break
    if (num > it):
        newLow = it
        it = random.randint(it, newHigh)
        counter += 1
        number = "{:,}".format(it)
        print("{}:\t{}".format(counter, number))
    elif (it > num):
        newHigh = it
        it = random.randint(newLow, it)
        counter += 1
        number = "{:,}".format(it)
        print("{}:\t{}".format(counter, number))
