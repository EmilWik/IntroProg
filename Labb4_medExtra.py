class contact:
    def __init__(self, name, number):
        self.alias = []
        self.name = name
        self.number = number


def add(name, number):
    phonebook[name] = contact(name, number)

def lookup(name):
    print(phonebook[name].number)

def alias(name, newname):
    phonebook[newname] = phonebook[name]
    phonebook[name].alias.append(newname)
    allAlias.append(newname)

def change(name, number):
    phonebook[name].number = number

def save(filename):
    file = open(filename,"w+")
    
    for key in phonebook:
        if not (key in allAlias):
           s =  phonebook[key].number + ';'
           s += phonebook[key].name   + ';'
           for x in phonebook[key].alias:
               s += x + ';'
           print(s)
    
    file.close()

def load(filename):
    file = open(filename)
    file.close()


#---main---#

phonebook = {}
allAlias = []
