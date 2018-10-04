class contact:
    def __init__(self, name, number, isAliasTo = None):
        self.alias = []
        self.isAliasTo = isAliasTo
        self.name = name
        self.number = number


def findAll(phonebook, name, number = None):
    retVal = []
    #använder numbret om det ät angivet, annars namnet
    if(number == None):
        for contacts in phonebook:
            if contacts.name == name:
                retVal.append(contacts)
                
    else:
        for contacts in phonebook:
            if contacts.number == number and contacts.isAliasTo == None:
                retVal.append(contacts)
                
    return retVal


def add(phonebook, name, number):
    if findAll(phonebook, name, number) == []:
        phonebook.append( contact(name, number))
    else:
        print("contact with that number already exist!")

    return phonebook
        

def lookup(phonebook, name):
    contacts = findAll(phonebook, name)
    if len(contacts) > 0:
        for element in contacts:
            print(element.number)
    else:
        print("Contact dosn't exist!")

    return phonebook
        

def alias(phonebook, name, newname, number = None):
    contacts = findAll(phonebook, name, number)
    
    if len(contacts) > 1:
        print("Serveral contacts with that name exists, please enter a number aswell.")
            
    elif len(contacts) == 1:
        
        if(contacts[0].isAliasTo == None):
            cont = contact(newname, contacts[0].number, contacts[0])
            phonebook.append(cont)
            contacts[0].alias.append(cont)

        else:
            cont = contact(newname, contacts[0].number, contacts[0].isAliasTo)
            phonebook.append(cont)
            contacts[0].isAliasTo.alias.append(cont)
            
            
    else:
        print("Contact dosn't exist!")

    return phonebook
    

def change(phonebook, name, newNumber, oldNumber = None):
    
    if findAll(phonebook, None, newNumber):
        print("contact with that number already exist!")
        
    else:
        contacts = findAll(phonebook, name, oldNumber)
        
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

    return phonebook


def save(phonebook, filename):
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

    return phonebook

def load(phonebook, filename): 
    try:
        file = open(filename)
        lines = [line.rstrip(';\n') for line in file]

        oldPhonebook = phonebook
        phonebook = []

        try:
            for contacts in lines:
                cont = contacts.split(';')
                
                add(phonebook, cont[1], cont[0])
                
                if len(cont) > 2:
                    for element in cont[2:]: #börjar på cont[2]
                        alias(phonebook, cont[1], element, cont[0])
        except:
            print("corrupt file!")
            phonebook = oldPhonebook
            
        file.close()
    
    except:
        print("Can't open/find file")
            

    return phonebook


def remove(phonebook, name, number = None):
    contacts = findAll(phonebook, name, number)
    
    if len(contacts) > 1:
        print("Serveral contacts with that name exists, please enter a number aswell.")
            
    elif len(contacts) == 1:
        if(contacts[0].isAliasTo == None):
            for elements in contacts[0].alias:
                phonebook.remove(elements)
                
            phonebook.remove(contacts[0])
        else:
            for elements in contacts[0].isAliasTo.alias:
                phonebook.remove(elements)
                
            phonebook.remove(contacts[0].isAliasTo)
            
    else:
        print("Contact dosn't exist!")

    return phonebook


def printAll(phonebook,emty):
    for a in phonebook:
        print (a.name + ": " + a.number)
    return phonebook


def promt():
    phonebook = []
    command = input("telebok> ")

    while command != "quit":
        
        command += ('")') 
        command = command.replace(' ', '(phonebook,"', 1)
        command = command.replace(' ', '", "')
        
        #try:
        phonebook = eval(command)
        #except:
         #   print("Command failed!")
        
        command = input("telebok> ")
        #Tar bort alla vittecken som inte är ett mellanslag
        while '  ' in command:
            command = command.replace('  ', ' ')


#---main---#

promt()

