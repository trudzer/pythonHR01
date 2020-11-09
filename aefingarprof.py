NUMBERS = 13
DASH_1 = 1
DASH_2 = 5
DASH_3 = 11
isbn = input


while isbn != "q".lower():
    isbn = input("Enter an ISBN: ").strip()
    if len(isbn) == NUMBERS:
        if isbn[0:DASH_1].isdigit():
            if isbn[DASH_1] == "-":
                if isbn[DASH_1+1:DASH_2].isdigit():
                    if isbn[DASH_2] == "-":
                        if isbn[DASH_2+1:DASH_3].isdigit():
                            if isbn[DASH_3] == "-":
                                if isbn[DASH_3+1::].isdigit():
                                    print("Valid format!")
                                else:
                                    print("Invalid format!")
                            else:
                                print("Invalid format!")
                        else:
                            print("Invalid format!")
                    else:
                        print("Invalid format!")
                else:
                    print("Invalid format!")
            else:
                print("Invalid format!")
        else:
            print("Invalid format!")
    elif isbn != "q".lower():
        print("Invalid format!")


--------------------------------------------------------------------------------------------------------------------------------------

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def createList(theList):
    newList = []
    for i in theList:
        numbers = []
        for j in i.split():
            number = ""
            for n in j:
                number += n
                numbers.append(number)
        newList.append(numbers)
    return newList

def findReplace(list, numbers):
    count = 0
    newList = []
    numbersList = []
    for i in numbers:
        i = int(i)
        numbersList.append(i)
    if numbersList[0] < 0 or numbersList[0] > 40 and numbersList[1] < 0 or numbersList[1] > 40 and numbersList[2] < 0 or numbersList[2] > 40 and numbersList[3] < 0 or numbersList[3] > 40 and numbersList[4] < 0 or numbersList[4] > 40:
        if numbers[0].isdigit() and numbers[1].isdigit() and numbers[2].isdigit() and numbers[3].isdigit() and numbers[4].isdigit():
            for i in (list):
                for j in i: 
                    if j == numbers[0] or j == numbers[1] or j == numbers[2] or j == numbers[3] or j == numbers[4]:
                        j = j+"*"
                    newList.append(j)
                    count += 1
                    print("{}".format(j), end=" ")
                    if count % 5 == 0:
                        print()
                        count = 0
        else:
            print("Winning numbers are invalid!")
    else:
        print("Winning numbers are invalid!")

file_name = input("Enter file name: ")
try:
    file_object = open_file(file_name)
    mainList = createList(file_object)
    numbers = input("Enter winning numbers: ").split(" ")
    findReplace(mainList,numbers)
    file_object.close()

except (FileNotFoundError):
    print("File", file_name, "not found!")
