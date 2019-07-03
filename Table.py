class Table:

    def __init__(self):
        self.atributes = []
        self.entries = []
    
    def set_atributes(self, atributes):
        self.atributes = atributes
    
    def get_atribute(self, index):
        return self.atributes[index]
    
    def get_all_atributes(self):
        return self.atributes

    def get_atribute_index(self, atribute):
        for i in range(len(self.atributes)):
            if self.atributes[i] == atribute:
                return i
    
    def add_entry(self, entry):
        self.entries.append(entry)
    
    def get_entry(self, index):
        return self.entries[index]
    
    def get_column_atribute(self, atribute):
        index_atribute = self.get_atribute_index(atribute)
        print(index_atribute)
        res = []
        for entry in self.entries:
            for i in range(len(entry)):
                if i == index_atribute:
                    res.append(entry[i])
        return res
    
    def get_column(self, index):
        res = []
        for entry in self.entries:
            for i in range(len(entry)):
                if i == index:
                    res.append(entry[i])
        return res

    def print_table(self):
        print(self.atributes)
        for entry in self.entries:
            print(entry)