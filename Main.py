import pandas as pd
from ID3_Algorithm import *

def load_data_menu():
    files = ["Restaurant.csv", "Weather2.csv", "Iris.csv"]
    print("+----- Choose a file to load -------+")
    print("|   1. Restaurant.csv               |")
    print("|   2. Weather.csv                  |")
    print("|   3. Iris.csv                     |")
    print("+-----------------------------------+")
    op = input("Enter your option [1-3]: ")
    if op.isdigit() and int(op) >= 1 and int(op) <= 3:
        filename = files[int(op) -1]
        table = pd.read_csv(filename)
        return table
    else:
        print("Please choose one of the numbers above!")
        load_data_menu()


def menu():
    print("+--------------------+")
    print("|   Decision Trees   |")
    print("+--------------------+")

    table = load_data_menu()
    table = table.applymap(str)

    table.drop("ID", axis=1, inplace=True)  # remove ID column from dataset
    """
    print(table)
    table.drop("ID", axis=1, inplace=True)  # remove best atribute from dataset

    print()
    print(table.columns.tolist()[-1])
    print()
    print(table["Price"])
    print()
    print(table.values)
    """
    print("Generating decision tree...")
    examples = table.values.tolist()
    attributes = table.columns.tolist()
    target_attribute = table.columns.tolist()[-1]

    #helps(table, examples, attributes, target_attribute)
    #-----decision_tree = id3(table, examples, attributes, target_attribute)
    decision_tree = ID32(examples, attributes, target_attribute)
    #print_tree(table, decision_tree, 0)
    print()
    print("Generated decision tree:")
    #----print_tree2(examples, attributes, decision_tree)
    decision_tree.print_tree(attributes)
    print("---------------------------------")
    dc = id3(table, examples, attributes, target_attribute)
    print_tree2(examples, attributes, dc)
    #print(decision_tree)

    # TODO
    # arranjar print_tree - a funcionar, apenas fazer versão minha - FEITO
    # save tree to .dot file
    # Possiveis melhorias:
    #   class para Tree - FEITO
    #   class Table - acho que esta não vale a pena


def main():
    menu()



if __name__ == "__main__":
    main()