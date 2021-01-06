def open_file(file_name):
    try:
        file_stream = open(file_name, "r")
        return file_stream
    except FileNotFoundError:
        return None

def create_flyers_dict(file_stream):
    flyers_dict = {}
    for line in file_stream:
        name, country = line.split()
        if name not in flyers_dict:
            flyers_dict[name] = {country}
        else:
            flyers_dict[name].add(country)
    return flyers_dict

def print_dict(flyers_dict):
    for name in sorted(flyers_dict.keys()):
        print("{}:".format(name))
        for country in sorted(flyers_dict[name]):
            print("\t{}".format(country))

def visited_most_countries(flyers_dict):
    countries_count = 0
    current_name = ""
    for name, countries in flyers.items():
        if len(countries) > countries_count:
            countries_count = len(countries)
            current_name = name
    return current_name, countries_count

def print_most_visited(name, count):
    print()
    print("{} has been to {} countries".format(name, count))

file_name = "flights.txt"
file_stream = open_file(file_name)
flyers = create_flyers_dict(file_stream)
print_dict(flyers)
name, count = visited_most_countries(flyers)
print_most_visited(name, count)

#-------------------------------------------------------------------------------------------------------------------------------

# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def display_grid(grid):
    for i in range(DIM):
        for j in range(DIM):
            print(grid[i][j], end=" ")
        print()
    print()

def find_new_position(move, row, col):

    def decrease(value):
        value = value - 1 if value > 0 else DIM - 1
        return value

    def increase(value):
        value = value + 1 if value < DIM - 1 else 0
        return  value

    if move == LEFT:
        col = decrease(col)
    elif move == RIGHT:
        col = increase(col)
    elif move == UP:
        row = decrease(row)
    elif move == DOWN:
        row = increase(row)

    return row, col

def make_move(grid, move, row, col):

    grid[row][col] = EMPTY
    row, col = find_new_position(move, row, col)
    grid[row][col] = POSITION
    return (row, col)


# Main program starts here
# In your implementation, you have to use the functions and the constants given above

grid = initialize_grid()
row, col = (0,0)
display_grid(grid)
move = get_move()

while move != QUIT:
    row, col = make_move(grid, move, row, col)
    display_grid(grid)
    move = get_move()
    
#-------------------------------------------------------------------------------------------------------------------------------

