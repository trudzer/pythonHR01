#Úlfur Ingólfsson 14/09/2020
password = input #tekur inn password frá notandi
valid_tries = 0 #býr til breytuna valid tries og gefur henni gildið 0
invalid_tries = 0 #býr til breytuna invalid tries og gefur henni gildið 0
tries = 0 #býr til breytuna tries og gefur henni gildið 0
lower = 0 #býr til breytuna lower og gefur henni gildið 0
upper = 0 #býr til breytuna upper og gefur henni gildið 0
digit = 0 #býr til breytuna digit og gefur henni gildið 0
while password != "q": #keyrir forrit á meðan password er ekki = q
  password = input("Enter a new password: ") #skrifar út "Enter new password: " og tekur inn gildi frá notenda
  if len(password) >= 6 and len(password) <= 20: #ef lengdin á password er lengri en 6 og styttri en 20, keyrir forrit
    for i in password: #skrifar út hvern einasta staf í password
      if i.isdigit(): #ef einhver stafur er tala
        digit += 1 #gildi digit fær +1 á sig
      if i.islower():  #ef einhver stafur er lowercase
        lower+=1   #gildi lower fær +1 á sig     
      if i.isupper(): #ef einhver stafur er uppercase
        upper+=1   #gildi upper fær +1 á sig         
    if lower>=1 and upper>=1 and digit>=1 and lower+upper+digit==len(password): #ef lower, upper og digit eru >= 1 og lower, upper og digit eru jafn gildi lengdina á password
      valid_tries += 1 #valid tries fær +1
      print("Valid password of length", len(password)) #forrit skrifar út að þetta var valid og lengdina á password
    if lower < 1 and password != "q": #ef lower er minni en 1, þýðir að það vantar lowercase staf og passar að password er ekki = q
      print("At least one lower case letter needed") #prentar út setningu
    if upper < 1 and password != "q": #ef upper er minni en 1, þýðir að það vantar uppercase staf og passar að password er ekki = q
      print("At least one upper case letter needed") #pretnar út setningu
    if digit < 1 and password != "q": #ef digit er minni en 1, þýðir að það vantar tölustaf og passar að password er ekki = q
      print("At least one number needed") #prentar út setningu
    if digit < 1 or lower < 1 or upper < 1 and password != "q": #ef digit, lower og upper eru minni en 1 og password er ekki = q, fær invalid tries +1 við sig
      invalid_tries +=1 #invalid tries fær +1
  elif password != "q": #ef password er ekki lengri en 6 eða stærri en 20 og ef password er ekki = q
    print("Invalid length") #prentar út setningu
    invalid_tries +=1 #invalid tries fær +1 við sig
  if password != "q": #ef password er ekki = q þá fær tries +1 í gildi
    tries += 1 #tries fær +1
  lower = 0 #lætur lower vera 0 fyrir næsta hring
  upper = 0 #lætur upper vera 0 fyrir næsta hring
  digit = 0 #lætur digit vera 0 fyrir næsta hring
if password == "q": #ef password er = q
  txt = ("You tried {} passwords, {} valid, {} invalid") #býr til breytu txt og skrifar út setningu með 3 tómum placeholders
  print(txt.format(tries, valid_tries, invalid_tries)) #skrifar út breytuna txt og fyllir inn í tómu placeholders
