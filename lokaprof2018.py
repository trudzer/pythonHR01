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

import random

TEAM_SIZE = 5
GAME_LENGTH = 48

class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i+1) # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE-1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


class BasketballPlayer:
    # You need to implment this class
    def __init__(self, number):
        self.__number = number
        self.__points = 0

    def __str__(self):
        return "Number: {} Points: {}\n".format(self.__number, self.__points)

    def __gt__(self, other):
        return self.__points > other.__points

    def shoot_ball(self):
        shoot = random.randint(0,1)
        if shoot:
            self.__points += 2
            return 2
        else:
            return 0
    

def print_winner(team_a, team_b):
    ''' You need to implement this function. Print out:
        which team won (if tie, print "Tie!")
    '''
    if team_a.get_points() == team_b.get_points():
        print("Tie !")
    elif team_a.get_points() > team_b.get_points():
        print("{} won!".format(team_a.get_name()))
    else:
        print("{} won!".format(team_b.get_name()))

def print_scores(team_a, team_b):
    ''' You need to implent this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team  
    '''
    print()
    print("{} scored {} points!".format(team_a.get_name(), team_a.get_points()))
    print("{} scored {} points!".format(team_b.get_name(), team_b.get_points()))

    print()
    print("{} scoring".format(team_a.get_name()))
    print(team_a)
    print("{} scoring".format(team_b.get_name()))
    print(team_b)

    print("{} highest scoring player:".format(team_a.get_name()))
    print(team_a.get_player_with_highest_score())
    print("{} highest scoring player:".format(team_b.get_name()))
    print(team_b.get_player_with_highest_score())

def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()    
        team_b.play_offence()
        
def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)

main()
