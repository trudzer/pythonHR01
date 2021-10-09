ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]                                             #Static name of each seat for row

def addLetters(no_of_seats, letters):
    '''Adds letters for a row depending on how many seats there are'''
    for row in range(0, no_of_seats):                                                                               #Loops for how many seats in 1 row
            letters.append(ALPHABET[row])                                                                           #Adds corresponding letters to seat value

def addRows(no_of_rows, seats_per_row, no_of_seats, letters, left_seats, right_seats):
    '''Adds the seats into 2 matrices depending on whether they're on the left or the right'''
    for row in range(0, no_of_rows + 1):                                                                            #Loops for how many rows there are
        seat_row = []                                                                                               #Empty array for storing each row
        for seat in range(0, seats_per_row):                                                                        #Loops for each seat per aisle
            seat_row.append(letters[seat])                                                                          #Appends seat to aisle
        left_seats.append(seat_row)                                                                                 #Appends row of seats to left side

    for row in range(0, no_of_rows + 1):                                                                            #Loops for how many rows there are
        seat_row = []                                                                                               #Empty array for storing each row
        for seat in range(seats_per_row, no_of_seats):                                                              #Loops for each seat per aisle
            seat_row.append(letters[seat])                                                                          #Appends seat to aisle
        right_seats.append(seat_row)                                                                                #Appends row of seats to right side

def printSeats(no_of_rows, seats_per_row, left_seats, right_seats):
    '''Prints out the seats in order'''
    for row in range(1, no_of_rows + 1):                                                                            #Loops for how many rows there are
        print("{:>2}   ".format(str(row)), end="")                                                                  #Prints out the number of the row
        for seat in range(0, seats_per_row):                                                                        #Loops for each seat on the left side
            print(left_seats[row][seat], end=" ")                                                                   #Prints out the seat
        print("  ", end="")                                                                                         #Creates space between left and right seats
        for k in range(0, seats_per_row):                                                                           #Loops for how many rows there are
            print(right_seats[row][k], end=" ")                                                                     #Prints out the seat
        print()                                                                                                     #Makes a stop after all seats in a full row are printed

def checkNumber(no_of_rows, seats_per_row, seat_booking, letters_text, occupied, temp_booking):
    '''Checks if the seat you're looking for is in the lists and books it'''
    for row in range(1, no_of_rows + 1):                                                                            #Loops for number of rows
        for seat in range(0, seats_per_row):                                                                        #Loops for each seat in left or right row
            if seat_booking[0] == row and seat_booking[1] == letters_text[row][seat]:                               #Checks if row and seat exists
                letters_text[row][seat] = "X"                                                                       #Updates seat with booked seat
                occupied.append(temp_booking)                                                                       #Adds occupied seat to occupied list

def loopContinue(book_seat):
    '''Checks if you want to continue the program or not'''
    while book_seat != ("y").upper():                                                                               #Loops while invalid input is written
        if book_seat == "n".upper():                                                                                #If "n" is chosen, breaks loop and closes program
            break
        print("Invalid input!")                                                                             
        book_seat = input("More seats (y/n)? ").upper()                                                             #Checks if you want to continue or quit

def main():
    no_of_rows = int(input("Enter number of rows:"))                                                                #Input for number of rows
    no_of_seats = int(input("Enter number of seats in each row:"))                                                  #Input for number of seats
    book_seat = input                                                                                               #Input for booking a seat
    letters = []                                                                                                    #Empty array for storing letters used in a full row
    left_seats = []                                                                                                 #Empty array for seats on the left aisle
    right_seats = []                                                                                                #Empty array for seats on the right aisle
    occupied = []                                                                                                   #Empty array for storing occupied seats
    seats_per_row = int((no_of_seats / 2))                                                                          #Takes the number of seaats per row and halvs it
                                                                                                                    
    if no_of_seats <= len(ALPHABET) and no_of_seats > 0 and no_of_rows > 0:                                         #If input is outside of boundries, break
        addLetters(no_of_seats, letters)                                                                            #Adds letters into a row for usage
        addRows(no_of_rows, seats_per_row, no_of_seats, letters, left_seats, right_seats)                           #Adds seats into matrices depending on left or right
        while book_seat != ("n").upper():                                                                           #While input is not "n"
            if no_of_seats % 2 == 0:                                                                                #Checks if number of seats is even
                printSeats(no_of_rows, seats_per_row, left_seats, right_seats)                                      #Prints out the seats in order
                seat_booking = input("Input seat number (row seat):").upper()                                       #Asks for seat to book
                temp_booking = seat_booking                                                                         #Creates temporary variable for storing input
                seat_booking = seat_booking.split(" ")                                                              #Splits input into row and seat
                try:                                                                                                #Try to run code and stop if any errors occure
                    seat_booking[0] = int(seat_booking[0])                                                          #Converts row input into int
                    if seat_booking[0] <= no_of_rows and seat_booking[1] in letters:                                #Checks if row is within range and whether there's a seat
                        if temp_booking in occupied:                                                                #If seat is occupied, break
                            print("That seat is taken!")
                        checkNumber(no_of_rows,seats_per_row, seat_booking, left_seats, occupied, temp_booking)     #Checks if seat is in left row
                        checkNumber(no_of_rows,seats_per_row, seat_booking, right_seats, occupied, temp_booking)    #Checks if seat is in right row
                        printSeats(no_of_rows, seats_per_row, left_seats, right_seats)                              #Prints out the seats in order with new values
                    else:
                        print("Seat number is invalid!")                                                            #If row or seat isn't on the list, return invalid
                except:                                                                                             #If error occures, don't run the code, and print out Invalid
                    print("Invalid input!") 
            else:
                print("Invalid number of seats!")                                                                   #If number of seats isn't even, return invalid
            book_seat = input("More seats (y/n)? ").upper()                                                         #Checks if you want to continue or quit
            loopContinue(book_seat)                                                                                 #Checks if your input is legal or not
    else:
        print("Invalid number of seats!")                                                                           #If input is larger than available seats, return invalid

if __name__ == "__main__":
    main()
