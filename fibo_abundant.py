#Úlfur Ingólfsson - 06/09/2020
main_input = input("Input f|a|b (fibonacci, abundant or both): ")

if main_input == "f":
  number1 = 0
  number2 = 1
  number3 = 1
  i = 2
  length = int (input("Input the length of the sequence: "))
  print("Fibonacci Sequence:\n-------------------")
  print(number1)
  print(number2)
  for i in range(1, length - 1): #loops from 1 to desired range - 1
    number3=number1+number2 #3rd number is equal to 1st number + 2nd number
    print(number3)
    number1=number2 #makes the 1st number equal to the 2nd number continuing the cycle
    number2=number3 #makes the 2nd number equal to the 3rd number continuing the cycle

if main_input == "a":
  input_a = int (input("Input the max number to check: "))
  print("Abundant numbers:\n-----------------")
  sum_all = 0  
  for i in range(1, input_a + 1):  
      for j in range(1, int(i)): #this loop runs from (1, i) amount of times within the main loop  
          if (i % j == 0):  #checks for if i is divisible by j
              sum_all = sum_all + j
      if (sum_all > i): #print number if sum_all is smaller than i
          print(i)  
      sum_all = 0

if main_input == "b":
  number1 = 0
  number2 = 1
  number3 = 1
  i = 2
  length = int (input("Input the length of the sequence: "))
  print("Fibonacci Sequence:\n-------------------")
  print(number1)
  print(number2)
  for i in range(1, length - 1): #loops from 1 to desired range - 1
    number3=number1+number2 #3rd number is equal to 1st number + 2nd number
    print(number3)
    number1=number2 #makes the 1st number equal to the 2nd number continuing the cycle
    number2=number3 #makes the 2nd number equal to the 3rd number continuing the cycle
  
  input_a = int (input("Input the max number to check: "))
  print("Abundant numbers:\n-----------------")
  sum_all = 0  
  for i in range(1, input_a + 1):  
      for j in range(1, int(i)):  #this loop runs from (1, i) amount of times within the main loop  
          if (i % j == 0):  #checks for if i is divisible by j
              sum_all = sum_all + j  
      if (sum_all > i):  #print number if sum_all is smaller than i
          print(i)  
      sum_all = 0
