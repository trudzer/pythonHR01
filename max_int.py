num_int = int(input("Input a number: "))    # Do not change this line
 #Fill in the missing code
list = [] #create empty list
while num_int > 0: #make the program run while the input isn't a negative number
  num_int = int(input("Input a number: "))
  list.append(num_int) #adds num_int inputs to the empty list
  max_int = max(list)
print("The maximum is", max_int)    # Do not change this line

n = int(input("Enter the length of the sequence: ")) # Do not change this line
for i in range(1, n+1): #makes a for loop from 1 to the input range
  if i == 1:
    current = first = i #makes first = 1
  elif i == 2: #makes second = 2
    current = second = i
  elif i == 3:  #makes third = 3
    current = third = i
  else:
    current = first + second + third #makes current = first + second + third

    first, second, third = second, third, current
  print(current)