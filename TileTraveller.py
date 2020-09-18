#Úlfur Ingólfsson 18/09/2020
#https://github.com/trudzer/pythonHR01/blob/master/TileTraveller.py
post1 = 1
post2 = 1
print("You can travel: (N)orth.")
inp = input("choose direction: ").lower() #taken in input from user and returns it as lowercase
if inp != "n": #if input is not = n
  print("Not a valid direction!")
else:
  post2 += 1 #increase vertical position by 1
if post1 >= 1 and post2 >= 1 or post1 <= 3 and post2 <= 3: #checks if the position is within the allowed spaces

  if post2 > 3:
    post2 = 3 #stops position from going over limit
    print("Not a valid direction!")
  if post1 > 3:
    post1 = 3 #stops position from going over limit
    print("Not a valid direction!")
  if post2 < 1:
    post2 = 1 #stops position from going under limit
    print("Not a valid direction!")
  if post1 < 1:
    post1 = 1 #stops position from going under limit
    print("Not a valid direction!")
while True:
  if post1 == 1 and post2 == 1 or post1 == 2 and post2 == 1: #checks for position and returns value if true
    print("You can travel: (N)orth.")
    inp = input("choose direction: ").lower()
    if inp != "n": #checks for if invalid input was typed in
      print("Not a valid direction!")
    else:
      post2 += 1 #increase lateral position by 1
  if post1 == 1 and post2 == 2: #checks for position and returns value if true
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "n" and inp != "e" and inp != "s": #checks for if invalid input was typed in
      print("Not a valid direction!")
    elif inp == "n":
      post2 += 1 #increase vertical position by 1
    elif inp == "s":
      post2 -= 1 #decreases vertical position by 1
    elif inp == "e":
      post1 += 1 #increase horizontal position by 1
  if post1 == 1 and post2 == 3: #checks for position and returns value if true
    print("You can travel: (E)ast or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "e" and inp != "s": #checks for if invalid input was typed in
      print("Not a valid direction!")
    elif inp == "s":
      post2 -= 1 #decreases vertical position by 1
    elif inp == "e":
      post1 += 1 #increase horizontal position by 1
  if post1 == 2 and post2 == 2 or post1 == 3 and post2 == 3: #checks for position and returns value if true
    print("You can travel: (W)est or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "w" and inp != "s": #checks for if invalid input was typed in
      print("Not a valid direction!")
    elif inp == "w":
      post1 -= 1 #decreases horizontal position by 1
    elif inp == "s":
      post2 -= 1 #decreases vertical position by 1
  if post1 == 2 and post2 == 3: #checks for position and returns value if true
    print("You can travel: (W)est or (E)ast.")
    inp = input("choose direction: ").lower()
    if inp != "w" and inp != "e": #checks for if invalid input was typed in
      print("Not a valid direction!")
    elif inp == "w":
      post1 -= 1 #decreases horizontal position by 1
    elif inp == "e":
      post1 += 1 #increase horizontal position by 1
  if post1 == 3 and post2 == 2: #checks for position and returns value if true
    print("You can travel:(N)orth or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "n" and inp != "s": #checks for if invalid input was typed in
      print("Not a valid direction!")
    elif inp == "n":
      post2 += 1 #increase vertical position by 1
    elif inp == "s":
      post2 -= 1 #decreases vertiacal position by 1
       
  if post1 == 3 and post2 == 1: #checks for position and returns value if true
    print("Victory!")
