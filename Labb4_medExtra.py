class contact:
    def __init__(self, name, number, isAliasTo = None):
        self.alias = []
        self.isAliasTo = isAliasTo
        self.name = name
        self.number = number


def findAll(name, number = None):
    retVal = []
    if(number == None):
        for contacts in phonebook:
            if contacts.name == name:
                retVal.append(contacts)
    else:
        for contacts in phonebook:
            if contacts.number == number and contacts.isAliasTo == None:
                retVal.append(contacts)
                
    return retVal


def add(name, number):
    if findAll(name, number) == []:
        phonebook.append( contact(name, number))
    else:
        print("contact with that number already exist!")
        

def lookup(name):
    contacts = findAll(name)
    for element in contacts:
        print(element.number)
        

def alias(name, newname, number = None):
    contacts = findAll(name, number)
    
    if len(contacts) > 1:
        print("Serveral contacts with that name exists, please enter a number aswell.")
            
    elif len(contacts) == 1:
        if(contacts[0].isAliasTo == None):
            cont = contact(newname, number, contacts[0])
            phonebook.append(cont)
            contacts[0].alias.append(cont)

        else:
            cont = contact(newname, number, contacts[0].isAliasTo)
            phonebook.append(cont)
            contacts[0].isAliasTo.alias.append(cont)
            
            
    else:
        print("Contact dosn't exist!")
    
    

def change(name, newNumber, oldNumber = None):
    contacts = findAll(name, oldNumber)
    
    if len(contacts) > 1:
        print("Serveral contacts with that name exists, please enter a number aswell.")
            
    elif len(contacts) == 1:
        contacts[0].number = newNumber
        
        if(contacts[0].isAliasTo == None):
            
            for elements in contacts[0].alias:
                elements.number = newNumber

        else:
            contacts[0].isAliasTo.number = newNumber
            
            for elements in contacts[0].isAliasTo.alias:
                elements.number = newNumber
            
    else:
        print("Contact dosn't exist!")


def save(filename):
    file = open(filename,"w+")
    
    for contacts in phonebook:
        if contacts.isAliasTo == None:
           s =  contacts.number + ';'
           s += contacts.name   + ';'
           for x in contacts.alias:
               s += x.name + ';'
           s += "\n"
           file.write(s)
    
    file.close()

def load(filename):
    file = open(filename)
    lines = [line.rstrip(';\n') for line in file]
    
    for contacts in lines:
        cont = contacts.split(';')
        
        add(cont[1], cont[0])
        
        if len(cont) > 2:
            for element in cont[2:]: #börjar på cont[2]
                alias(cont[1], element, cont[0])
        
    file.close()


#---main---#

phonebook = []
