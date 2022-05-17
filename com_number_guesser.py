import random

MAXNUM = 1000000
num = random.randint(0, MAXNUM)
it = random.randint(0, MAXNUM)
counter = 0
newLow = 0
newHigh = MAXNUM

formNum = "{:,}".format(num)
print("THE NUMBER: " + str(formNum))
print("----------------------------")
while (counter < MAXNUM):
    if (num == it):
        print("Number found after {} tries".format(counter))
        break
    if (num > it):
        newLow = it
        it = random.randint(it, newHigh)
        counter += 1
        number = "{:,}".format(it)
        print("{:>2}:\t{}".format(counter, number))
    elif (it > num):
        newHigh = it
        it = random.randint(newLow, it)
        counter += 1
        number = "{:,}".format(it)
        print("{:>2}:\t{}".format(counter, number))
