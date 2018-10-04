class contact:
    def __init__(self, name, number, isAliasTo = None):
        self.alias = [] #Lista med alla alias till kontakten
        self.isAliasTo = isAliasTo #Kontakten som den är alias till. (None om inte ett alias)
        self.name = name
        self.number = number



#Skriver ut alla kontakter i telefonboken
def printAll(phonebook,emty):
    for a in phonebook:
        print (a.name + ": " + a.number)
    return phonebook



#Returerar en lista med alla kontakter med det namet/numret
def findAll(phonebook, name, number = None):    
    retVal = []
    #Använder numbret om det ät angivet, annars namnet
    if(number == None):
        for contacts in phonebook:
            if contacts.name == name:
                retVal.append(contacts)
    #Använder numret
    else:
        for contacts in phonebook:
            #Kollar att kontakten har rätt nummer och inte är ett alias
            if contacts.number == number and contacts.isAliasTo == None:
                retVal.append(contacts)
                
    return retVal



def add(phonebook, name, number):
    #Kollar om numret är upptaget
    if findAll(phonebook, name, number) == []:
        phonebook.append( contact(name, number))
    else:
        print("contact with that number already exist!")

    return phonebook
        


def lookup(phonebook, name):
    contacts = findAll(phonebook, name) #Lista med alla kontaker med det namnet
    
    if len(contacts) > 0:
        for element in contacts:
            print(element.number)
    else:
        print("Contact dosn't exist!")

    return phonebook
        


def alias(phonebook, name, newname, number = None):
    contacts = findAll(phonebook, name, number) #Lista med alla kontaker med det namnet/numret
    
    if len(contacts) > 1:
        print("Serveral contacts with that name exists, please enter a number aswell.")
            
    elif len(contacts) == 1:
        
        
        if(contacts[0].isAliasTo == None):
            #Skapar en ny kontakt som är ett alias till orginal kontakten
            cont = contact(newname, contacts[0].number, contacts[0])
            phonebook.append(cont)
            contacts[0].alias.append(cont) #Lägger in aliaset i orginal kontaktens alias lista

        #Om kontakten redan är ett alias så blir nya kontakten ett alias till orginalet.
        #Altså kan inte ett alias ha ett alias utan orginal kontakten får ett extra alias istället
        else:
            cont = contact(newname, contacts[0].number, contacts[0].isAliasTo)
            phonebook.append(cont)
            contacts[0].isAliasTo.alias.append(cont)
            
            
    else:
        print("Contact dosn't exist!")

    return phonebook
    


def change(phonebook, name, newNumber, oldNumber = None):
    
    #Kollar om numret är upptaget
    if findAll(phonebook, None, newNumber):
        print("contact with that number already exist!")
        
    else:
        contacts = findAll(phonebook, name, oldNumber) #Lista med alla kontaker med det namnet/numret
        
        if len(contacts) > 1:
            print("Serveral contacts with that name exists, please enter a number aswell.")
                
        elif len(contacts) == 1:
            contacts[0].number = newNumber
            
            #Ändrar nummret på alla alias till kontakten
            if(contacts[0].isAliasTo == None):
                
                for elements in contacts[0].alias:
                    elements.number = newNumber

            #Om kontaken är ett alias så ändrar den orginalkontaktens nummret och
            #nummret på orginalkontaktens alias
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
        #Sparar bara orginalkontakter
        if contacts.isAliasTo == None:
           s =  contacts.number + ';'
           s += contacts.name   + ';'

           #Appenderar alla alias till orginalkontaken
           for x in contacts.alias:
               s += x.name + ';'
               
           s += "\n"
           file.write(s)
    
    file.close()

    return phonebook



def load(phonebook, filename): 
    try:
        file = open(filename)

        #Tar bort sista semikolonet i raden samt tar bort ny rads tecknet
        lines = [line.rstrip(';\n') for line in file] 

        oldPhonebook = phonebook #Sparar den gammla telefonboken utifall något går fel.
        phonebook = []

        try:
            for contacts in lines:
                cont = contacts.split(';') #Delar upp raden i en lista. cont[0];cont[1];...
                
                add(phonebook, cont[1], cont[0]) #Lägger in kontakten

                #Lägger in alla alias om de finns några
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
    contacts = findAll(phonebook, name, number) #Lista med alla kontaker med det namnet/numret
    
    if len(contacts) > 1:
        print("Serveral contacts with that name exists, please enter a number aswell.")
            
    elif len(contacts) == 1:
        #Tar bort kontakten samt alla alias till kontakten
        if(contacts[0].isAliasTo == None):
            for elements in contacts[0].alias:
                phonebook.remove(elements)
                
            phonebook.remove(contacts[0])

        #Om kontakten är ett alias så tar den bort orginalet samt dess alias.
        else:
            for elements in contacts[0].isAliasTo.alias:
                phonebook.remove(elements)
                
            phonebook.remove(contacts[0].isAliasTo)
            
    else:
        print("Contact dosn't exist!")

    return phonebook



def promt():
    phonebook = []
    command = input("telebok> ")

    while command != "quit":
        #Tar bort alla vittecken som inte är ett mellanslag. Ser till att inga dubbel mellanslag finns
        while '  ' in command:
            command = command.replace('  ', ' ')

        command = command.rstrip() #Tar bort sista karaktären om den är ett whitespace

        #Formanterar om kommandot så att så att blir som en funktion
        #ex: add test 123 -> add(phonebook,test,123)
        command += ('")') 
        command = command.replace(' ', '(phonebook,"', 1) #byter ut första mellanslaget
        command = command.replace(' ', '","') #byter ut resten av mellanslagen
        
        try:
            phonebook = eval(command)
        except:
            print("Command failed!")
        
        command = input("telebok> ")


#---main---#

promt()

