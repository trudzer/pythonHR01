#Úlfur Ingólfsson 28/09/2020
def open_file(filename):
  file_object = open(filename, 'r')
  return file_object

def createList(theList):
    newList = []
    for i in theList:
        try:
            newList.append(float(i))
        except ValueError:
            continue
    return newList

def  sequence(fileList):
    print("\tSequence:\n\t\t", end="")
    for i in fileList:
        print(round(i,2), end=' ')
    print()

def cumulativeSum(fileList):
    total = 0
    print("\tCumulative sum:\n\t\t", end="")
    for i in fileList:
        total += i
        print(round(total,2), end=' ')
    print()

def sortedSequence(fileList):
    num_sort = sorted(fileList)
    print("\tSorted sequence:\n\t\t", end="")
    for i in num_sort:
        print(round(i,2), end=' ')
    print()

def median(fileList):
    print("\tMedian:\n\t\t", end="")
    if len(fileList) > 1:
        num_sort = sorted(fileList)
        num_len = len(fileList)
        if num_len % 2 == 0:
            num1 = num_sort[num_len//2]
            num2 = num_sort[num_len//2-1]
            median = (num1 + num2) / 2
        else:
            median = num_sort[num_len//2]
        return print(round(median, 4))
    else:
        return []
    print()

def func(fileList):
    sequence(fileList)
    cumulativeSum(fileList)
    sortedSequence(fileList)
    median(fileList)