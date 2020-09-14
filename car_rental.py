first_input = ()
miles = int
odo_start = int
odo_end = int
number_of_days = int

print("Welcome to car rentals!")

while first_input != 'n':
  first_input = input("Would you like to continue (y/n)? ")
  if first_input == 'y':
    customer_code = input("Customer code (b or d): ")
    if customer_code == ('b'):
      number_of_days = int (input("Number of days: "))
      odo_start = int (input("Odometer reading at the start: "))
      odo_end = int (input("Odometer reading at the end: "))
      miles = odo_end - odo_start
      sum = float ((number_of_days * 40) + 0.25 * (odo_end - odo_start))
    if customer_code == ('d'):
      number_of_days = int (input("Number of days: "))
      odo_start = int (input("Odometer reading at the start: "))
      odo_end = int (input("Odometer reading at the end: "))
      miles = odo_end - odo_start
      average_miles = miles / number_of_days
      extra_miles = average_miles - 100
      new_miles = extra_miles * number_of_days
      if average_miles >= 100:
        sum = float ((number_of_days * 60) + 0.25 * new_miles)
      if odo_end - odo_start < 100:
        sum = float ((number_of_days * 60))
    print("Miles driven:", miles)
    print("Amount due:", round(sum,1))
  else:
    break