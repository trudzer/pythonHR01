def get_student():
    name, grade_1, grade_2, grade_3 = None, None, None, None        

    name = input("Student name: ")
    grade_1 = float(input("Input grade number 1: "))
    grade_2 = float(input("Input grade number 2: "))
    grade_3 = float(input("Input grade number 3: "))

    average = (grade_1 + grade_2 + grade_3) / 3

    return name, grade_1, grade_2, grade_3, average

def add_grades(student_dict, name, grade_1, grade_2, grade_3, average):
    if name not in student_dict:
        student_dict[name] = grade_1, grade_2, grade_3, average

def print_student_list(student_dict):
        sorted_list = sorted(student_dict)
        current_value = 0
        max_value = 0
        print("Student list:")
        for name in sorted_list:
            current_value = (student_dict[name][3])
            if current_value > max_value:
                    max_value = current_value
                    current_student = name
            
            print("{}: [{}, {}, {}]".format(name, student_dict[name][0], student_dict[name][1], student_dict[name][2]))
        print("Student with highest average grade:\n{} has an average grade of {:.2f}".format(current_student, max_value))

def main():
    student_dict = {}
    name = ''

    if name is not None:
        for i in range(0,4):
            name, grade_1, grade_2, grade_3, average = get_student()
            add_grades(student_dict, name, grade_1, grade_2, grade_3, average)
        print_student_list(student_dict)

main()


#-------------------------------------------------------------------------------------------------------------

# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

def find_new_position(grid, move, row, col):

    if grid[row][col-1] == move:#Left
        if col > 0:
            col = col - 1

    elif grid[row][col+1] == move:#Right
        if col < DIM:
            col = col + 1
            
    elif grid[row-1][col] == move:#Down
        if row > 0:
            row = row - 1

    elif grid[row+1][col] == move:#Up
        if row < DIM:
            row = row + 1

    return (row, col)

def make_move(grid, move, row, col):
    grid[row][col] = move
    row, col = find_new_position(grid, move, row, col)
    grid[row][col] = EMPTYSLOT
    return (row, col)
        
the_board = initialize_board()
pos_input = input
for i in range(DIM):
        for j in range(DIM):
            if the_board[i][j] == EMPTYSLOT:
                row, col = (i,j)

while pos_input != QUIT:

    display(the_board)
    pos_input = int(input())
    row, col = make_move(the_board, pos_input, row, col)
