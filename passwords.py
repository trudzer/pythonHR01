#Úlfur Ingólfsson 14/09/2020
password = input
valid_tries = 0
invalid_tries = 0
tries = -1
lower = 0
upper = 0
digit = 0
while password != "q":
  password = input("Enter a new password: ")
  if len(password) >= 6 and len(password) <= 20:
    for i in password:
      if i.isdigit(): 
        digit += 1
      if i.islower(): 
        lower+=1        
      if i.isupper(): 
        upper+=1              
    if lower>=1 and upper>=1 and digit>=1 and lower+upper+digit==len(password): 
      valid_tries += 1
      print("Valid password of length", len(password))
    if lower < 1 and password != "q":
      print("At least one lower case letter needed")
    if upper < 1 and password != "q":
      print("At least one upper case letter needed")
    if digit < 1 and password != "q":
      print("At least one number needed")
    if digit < 1 or lower < 1 or upper < 1 and password != "q":
      invalid_tries +=1
  elif password != "q":
    print("Invalid length")
    invalid_tries +=1
  tries += 1
  lower = 0
  upper = 0
  digit = 0
if password == "q":
  txt = ("You tried {} passwords, {} valid, {} invalid")
  print(txt.format(tries, valid_tries, invalid_tries))
