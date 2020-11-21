def get_candidate_votes():
    '''Returns a tuple consising of a name of a candidate and votes given to him/her.
    Either or both of the elements of the tuple can have the value None indicating an invalid input.'''

    candidate, votes = None, None

    input_list = input("Candidate and votes: ").split()
    if len(input_list) > 0:
        candidate = input_list[0].lower()
        if len(input_list) > 1:
            try:
                votes = int(input_list[1])
            except ValueError:
                pass
    
    return candidate, votes
    
    
def add_results(result_dict, candidate, votes):
    '''Adds the votes to the given to candidate in the given dictionar'''
    if candidate in result_dict:
        result_dict[candidate] += votes
    else:
        result_dict[candidate] = votes

def get_total_votes(result_dict):
    '''Returns the total number of votes for the given result dictionary'''
    total = 0
    for candidate in result_dict:
        total += result_dict[candidate]
    
    return total
    # Simpler solution
    # return sum(result_dict.values())


def print_results(result_dict):
    '''Prints the current results of the election in ascending order candidate names'''
    for candidate in sorted(result_dict):
        print("{}: {}".format(candidate, result_dict[candidate]))

# Main    
election_dict = {}
candidate = ''

while candidate is not None:
    candidate, votes = get_candidate_votes()
    if candidate is not None:
        if votes is not None:
            add_results(election_dict, candidate, votes)
        else:
            print("Invalid no. of votes!")

print_results(election_dict)
print("Total no. of votes: {}".format(get_total_votes(election_dict)))
    
#------------------------------------------------------------------------------------------------------------------------------

ZERO = 0

def open_file(file_name):
    '''Opens the given filname and returns its file object, or None if not found'''
    try:
        file_object = open(file_name, 'r')
        return file_object
    except FileNotFoundError:
        return None

def read_matrix(file_object):
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    matrix = []
    for line in file_object:
        row_str = line.split()
        row_int = [int(number) for number in row_str]
        matrix.append(row_int)
    
    return matrix
    
def display(matrix):
    '''Display the matrix, printing it one row in each line'''
    dimension = len(matrix)
    for i in range(dimension):
        for j in range(dimension):
            print(matrix[i][j], end="\t")
        print()    

def row_sum_same(matrix):
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    
    first_row_sum = sum(matrix[0])
    for row in matrix[1:]:
        row_sum = sum(row)
        if row_sum != first_row_sum:
            return ZERO
    
    return first_row_sum

def col_sum_same(matrix):
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    
    first_col_sum = 0
    for row in matrix:
        first_col_sum += row[0] 
    
    dimension = len(matrix)
    for i in range(1, dimension):
        sum_col = 0
        for row in matrix:
            sum_col += row[i]   # row[i] is the i-th column of row
        if sum_col != first_col_sum:
            return ZERO
    
    return first_col_sum

def is_same_sums(matrix):
    '''Returns true if the sum of the elements in each row and each colunm of the matrix is the same value'''
    return ZERO != row_sum_same(matrix) == col_sum_same(matrix)

def main():
    file_name = input("File name: ")
    file_object = open_file(file_name)
    if file_object is None:
        print("File not found")
    else:
        matrix = read_matrix(file_object)
        file_object.close()
        display(matrix)
        same_sums = is_same_sums(matrix)
        if same_sums:
            print("Same sums")
        else:
            print("Not same sums")

# Main program starts here
if __name__ == "__main__":
    main()
    
#------------------------------------------------------------------------------------------------------------------------------

class Order():

    def __init__(self, item, price):
        self.__item = item
        self.__price = price
    
    def __str__(self):
        return "Item: {}, price: {}".format(self.item(), self.price())

    def __gt__(self, other):
        return self.price() > other.price()
    
    def __add__(self, other):
        new_item = self.item() + "+" + other.item()
        return Order(new_item, self.price() + other.price())

    def item(self):
        return self.__item

    def price(self):
        return self.__price
