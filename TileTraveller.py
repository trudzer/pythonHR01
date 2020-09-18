#Úlfur Ingólfsson 18/09/2020
#https://github.com/trudzer/pythonHR01/blob/master/TileTraveller.py
post1 = 1
post2 = 1
print("You can travel: (N)orth.")
inp = input("choose direction: ").lower()
if inp != "n":
  print("Not a valid direction!")
else:
  post2 += 1
if post1 >= 1 and post2 >= 1 or post1 <= 3 and post2 <= 3:

  if post2 > 3:
    post2 = 3
    print("Not a valid direction!")
  if post1 > 3:
    post1 = 3
    print("Not a valid direction!")
  if post2 < 1:
    post2 = 1
    print("Not a valid direction!")
  if post1 < 1:
    post1 = 1
    print("Not a valid direction!")
while True:
  if post1 == 1 and post2 == 1 or post1 == 2 and post2 == 1:
    print("You can travel: (N)orth.")
    inp = input("choose direction: ").lower()
    if inp != "n":
      print("Not a valid direction!")
    else:
      post2 += 1
  if post1 == 1 and post2 == 2:
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "n" and inp != "e" and inp != "s":
      print("Not a valid direction!")
    elif inp == "n":
      post2 += 1
    elif inp == "s":
      post2 -= 1
    elif inp == "e":
      post1 += 1
  if post1 == 1 and post2 == 3:
    print("You can travel: (E)ast or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "e" and inp != "s":
      print("Not a valid direction!")
    elif inp == "s":
      post2 -= 1
    elif inp == "e":
      post1 += 1
  if post1 == 2 and post2 == 2 or post1 == 3 and post2 == 3:
    print("You can travel: (W)est or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "w" and inp != "s":
      print("Not a valid direction!")
    elif inp == "w":
      post1 -= 1
    elif inp == "s":
      post2 -= 1
  if post1 == 2 and post2 == 3:
    print("You can travel: (W)est or (E)ast.")
    inp = input("choose direction: ").lower()
    if inp != "w" and inp != "e":
      print("Not a valid direction!")
    elif inp == "w":
      post1 -= 1
    elif inp == "e":
      post1 += 1
  if post1 == 3 and post2 == 2:
    print("You can travel:(N)orth or (S)outh.")
    inp = input("choose direction: ").lower()
    if inp != "n" and inp != "s":
      print("Not a valid direction!")
    elif inp == "n":
      post2 += 1
    elif inp == "s":
      post2 -= 1
       
  if post1 == 3 and post2 == 1:
    print("Victory!")
    break