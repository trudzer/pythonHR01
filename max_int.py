num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
list = [] #create empty list
while num_int > 0: #make the program run while the input isn't a negative number
  num_int = int(input("Input a number: "))
  list.append(num_int) #adds num_int inputs to the empty list
  max_int = max(list)
print("The maximum is", max_int)    # Do not change this line