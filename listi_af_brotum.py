def get_lists():
    '''býr til 2 lista til notkun fyrir hin föllin'''
    for i in range(1, YFIR+1):
        for j in range(1, UNDIR+1):
            hnit = round(i/j,2)
            position = (i,j)
            if hnit not in hnit_list:
                hnit_list.append(hnit)
                new_list.append(position)

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
    for i in new_list:
        yfir = i[0]
        undir = i[1]
        if yfir != prev:
            prev = yfir
            print()
        print("{}/{}".format(yfir, undir), end="\t")
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

if __name__ == "__main__":
    new_list = []
    hnit_list = []
    YFIR = int(input("Yfir: "))
    UNDIR = int(input("Undir: "))
    main()
