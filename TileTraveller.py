#Úlfur Ingólfsson 18/09/2020
def walk(direction):
  pos1 = 0
  pos2 = 0

  if direction == "e":
    pos1 = 1
  
  if direction == "n":
    pos2 = 1

  if direction == "w":
    pos1 = -1

  if direction == "s":
    pos2 = -1
  
  return pos1,pos2
post1 = 1
post2 = 1
wall = False
print("You can travel: (N)orth.")
inp = input("choose direction: ").lower()
if inp != "n":
  print("Not a valid direction!")
else:
  post2 += 1
if post1 >= 1 and post2 >= 1 or post1 <= 3 and post2 <= 3:
  direct_inp = list (walk(inp))

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
       
  direct_inp[0] = 0
  direct_inp[1] = 0
  if post1 == 3 and post2 == 1:
    print("Victory!")
    break