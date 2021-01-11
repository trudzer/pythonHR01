def get_lists():
    '''býr til 2 lista til notkun fyrir hin föllin'''
    for i in range(1, ROW+1):
        for j in range(1, COLUMN+1):
            hnit = round(i/j,2)
            position = (i,j)
            if hnit not in hnit_list:
                hnit_list.append(hnit)
                brot_list.append(position)

def get_average():
    '''reiknar meðaltal á tölum í lista'''
    total = 0
    for i in hnit_list:
        total += i
    average = total / len(hnit_list)
    return average

def print_list():
    '''prentar út brotin sem eru unique í lista'''
    prev = 0
    for i in brot_list:
        row = i[0]
        col = i[1]
        if row != prev:
            prev = row
            print()
        print("{}/{}".format(row, col), end="\t")
    print()

def print_average():
    '''prentar út meðaltal fyrir tölur í lista'''
    print()
    print("average: {:.2f}".format(get_average()))

def main():
    get_lists()
    get_average()
    print_list()
    print_average()

#Main byrjar hérna
if __name__ == "__main__":
    brot_list = []
    hnit_list = []
    ROW = int(input("Rows: "))
    COLUMN = int(input("Columns: "))
    main()
