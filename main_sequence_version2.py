#Úlfur Ingólfsson 28/09/2020
import sequence_analysis_version2 as fl

file_name = input("Enter filenames: \n")
file_name = file_name.split()
try:
    for i in file_name:
        file_object = fl.open_file(i)
        print("File", i)
        mainList = fl.createList(file_object)
        fl.func(mainList)
        file_object.close()
        print()
except FileNotFoundError:
    print("File", i, "not found")
