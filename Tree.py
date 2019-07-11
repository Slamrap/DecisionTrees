import Main

class Tree:
    def __init__(self, value):
        self.value = value
        self.branch = []
        #self.frequency = frequency

    def print_tree(self, attributes):
        self.print_rec(0, attributes)

    def print_spaces(self, level):
        tabs = ""
        for i in range(level):
            tabs += "\t"
        return tabs

    def print_rec(self, level, attributes):
        tabs = self.print_spaces(level)
        
        if self.value in attributes:
            print(tabs, "<" + self.value + ">:")
        elif self.value not in attributes and isinstance(self.branch[0], Tree):
            #print(tabs + self.value + ": " + self.branch[0])
            print(tabs, self.value + ":")
        else:
            print(tabs, self.value + ": ", end='')

        for node in self.branch:
            if isinstance(node, Tree):
                #print()
                node.print_rec(level + 1, attributes)
            else:
                #tabs = self.print_spaces(level + 1)
                #print(tabs, node)
                print(node)

    def save_to_dot_file(self):
        a = 0