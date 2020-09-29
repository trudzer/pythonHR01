print("List to tuple")
#list_to_int_tuple function goes here
def list_to_int_tuple(theList):
    newList = []
    for i in theList:
        try:
            i = int(i)
            newList.append(i)
        except ValueError:
            continue
    return tuple(newList) 
#Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_int_tuple(a_list)
print(a_tuple)
print()
print("----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

print("\nSum of even numbers")
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    a_list = [int(i) for i in a_list]
    return a_list

def even_sum(num):
    total = 0
    for i in num:
        if (i % 2) == 0:
            total += i
    return total

#Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
print()
print("----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

print("\nEmail addresses")
def get_emails():
    a_list = input
    newList = []
    while a_list != "q":
        a_list = input("Email address: ").strip()
        newList.append(a_list)
        if a_list == "q":
            break
    return newList[0:-1]

def get_names_and_domains(str):
    newList = []
    for i in str:
        i = i.split('@')
        newList.append(tuple(i))
    return newList

#Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)
print()
print("----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

print("\nScores")
def getFloat():
    a_list = input("Enter scores separated by space: ").strip().split(' ')
    newList = []
    for i in a_list:
        newList.append(float(i))
    return sorted(newList)

def getSum(num):
    total = 0
    try:
        if len(num) < 2:
            print("At least two scores needed!")
        else:
            num = num[2:]
            for i in num:
                total += i
            print ("Sum of scores (two lowest removed):", round(total,2))
    except ValueError:
            return None

list_a = getFloat()
getSum(list_a)
