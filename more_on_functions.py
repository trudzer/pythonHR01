#Úlfur Ingólfsson 01/10/2020
#definition for music_func goes here
def music_func(music, group, singer):
    print("The best type of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func(music = "Classic Rock", group = "The Beatles", singer = "Freddie Mercury")

main()

print()
print("------------------------------------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------------------------------

def remove_evens(int_list):
    for i in int_list[:]:
        if (i % 2) == 0:
            int_list.remove(i)
    return int_list

def remove_evens2(int_list):
    newList = []
    for i in int_list:
        if i % 2 == 0:
            continue
        else:
            newList.append(i)
    return newList

#Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)

print()
print("------------------------------------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------------------------------

def openFile(filename):
  fileObject = open(filename, 'r')
  fileContent = fileObject.read()
  fileContent = fileContent.replace("\n", " ")
  fileContent = fileContent.replace("!", "")
  fileContent = fileContent.replace(",", "")
  fileContent = fileContent.replace(".", "")
  fileContent = fileContent.replace("?", "")
  fileContent = fileContent.replace("\'", "")
  fileContent = fileContent.replace("\"", "")
  fileContent = fileContent.replace("[", "")
  fileContent = fileContent.replace("]", "")
  return fileContent.strip().split(' ')

def uniqWord(text):
    newList = []
    for i in text[:]:
        if i not in newList:
            newList.append(i)
    print(sorted(newList))

def main():
    text = input("Enter filename: ")
    file = openFile(text)
    uniqWord(file)

main()

print()
print("------------------------------------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------------------------------

def theList(int_list, check_list):
    counter = 0
    for i in int_list:
        if i == check_list:
            counter += 1
    if counter >= 2:
        print(True)
    else:
        print(False)

def main():
    try:
        int_list = input("Enter elements of list separated by commas: ").split(',')
        for i in int_list:
            i = int(i)
        check_list = input("Consecutive check: ")
        theList(int_list, check_list)
    except ValueError:
        print("Error: enter only integers.")

main()

print()
print("------------------------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------------------

def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def average(the_list):
    total = 0
    for i in the_list:
        total += i
    return (total / len(the_list))

def list_to_int(theList):
    newList = []
    for i in theList:
        i = int(i)
        newList.append(i)
    return newList
        
# The main program starts here
def lists(theList):
    primeList = []
    newList = []
    for i in theList:
        if i not in newList:
            newList.append(i)
    print("Input list:", theList)
    print("Sorted list:", sorted(theList))
    for i in newList:
        if is_prime(i):
            primeList.append(i)
    print("Prime list:", primeList)
    print("Min:", min(theList), " Max:", max(theList), " Average:", round(average(theList),2))

theList = input("Enter integers separated with commas: ").split(',')
newList = list_to_int(theList)
lists(newList)