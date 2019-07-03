import csv
from Table import *



def read_csv(filename):
    table = Table()
    flag_atributes = True 
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #dates = []
        #colors = []

        for row in readCSV:
            if flag_atributes:
                table.set_atributes(row)
                flag_atributes = False
            else:
                table.add_entry(row)
    return table

def load_menu():
    files = ["Restaurant.csv", "Weather.csv", "Iris.csv"]
    print("+----- Choose a file to load -------+")
    print("|   1. Restaurant.csv               |")
    print("|   2. Weather.csv                  |")
    print("|   3. Iris.csv                     |")
    print("+-----------------------------------+")
    op = input("Enter your option [1-3]: ")
    if op.isdigit() and int(op) >= 1 and int(op) <= 3:
        table = read_csv(files[int(op) -1])
        return table
    else:
        print("Please choose one of the numbers above!")
        load_menu()

def menu():
    print("+--------------------+")
    print("|   Decision Trees   |")
    print("+--------------------+")

    table = load_menu()
    """
    table.print_table()
    print()
    print(table.get_entry(2))
    print(table.get_atribute(2))
    
    print(table.get_column_atribute("Price"))
    print(table.get_column(8))
    """

def main():
    menu()



if __name__ == "__main__":
    main()