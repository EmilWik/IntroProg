def menuPromt():
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit programy")
    return input("Choose alternative: ")





def insert1(words, desc):
    word = input("Word to insert: ")

    #Kollar om word finns i words
    if(word in words):
        print("word already in dictionary!")
        
    else: #om inte så läggs det till
        words.append( word )
        #ber om, samt lägger till beskrivning
        desc.append ( input("Description of word: ") ) 
        

def lookup1(words, desc):
    word = input("Word to lookup: ")

    #Kollar om word finns i words
    if(word in words):
        #beskrivningen och ordet har samma index.
        #kollar efter ordets index för att hitta beskrivningen
        print( desc[words.index(word)] ) 
    else:
        print("Word not found")
        

def ordLista1():
    words = []
    desc  = []
    i = menuPromt()

    while(i != "3"): #avslutar programloopen om kommandot är 3
        print("") 

        if(i == "1"): #insert
            insert1(words,desc)

        elif(i == "2"): #lookup
            lookup1(words, desc)
              
        else:
            print("Unknown command, please try again.","")
            

        print("","")
        i = menuPromt()






def insert2(words): 
    word = input("Word to insert: ")

    #finns inga ord, bara att lägga till
    if len(words) == 0:
            desc = input("Description of word: ")
            words.append( (word, desc) )
    else:
        #kollar om ordet finns
        for i in words:
            #jämför ordet med alla ord i words
            if i[0] == word:
                print("word already in dictionary!")
                break
            #kollar om det är sista loopen, altså har den inte hittat ordet
            elif words.index(i) == len(words) - 1: 
                desc = input("Description of word: ")
                words.append( (word, desc) )
                break #annars kör loopen igen för att words blir en större


def lookup2(words):
    word = input("Word to lookup: ")
    for i in words:
        if(i[0] == word):
            print(i[1])
            break
        elif(words.index(i) == len(words) - 1): #i = tupeln. index(i) = positionen
            print("Word not found")


def ordLista2():
    words = []
    i = menuPromt()

    while(i != "3"): #avslutar programloopen om kommandot är 3
        print("")

        if(i == "1"): #insert
            insert2(words)
            
        elif(i == "2"): #lookup
            lookup2(words)
            
        else:
            print("Unknown command, please try again.","")


        print("","")
        i = menuPromt()






def insert3(dic):
    word = input("Word to insert: ")

    #kollar om ordet finns i ordboken
    if(word in dic):
        print("word already in dictionary!")
        
    #annars lägger den till den
    else:
        dic[word] = input("Description of word: ")
                

def lookup3(dic):
    word = input("Word to lookup: ")

     #kollar om ordet finns i ordboken
    if(word in dic):
        print( dic[word] )
    else:
        print("Word not found")


def ordLista3():
    dic = {}
    i = menuPromt()

    while(i != "3"): #avslutar programloopen om kommandot är 3
        print("")

        if(i == "1"): #insert
            insert3(dic)

        elif(i == "2"): #lookup
            lookup3(dic)

        else:
            print("Unknown command, please try again.","")
            

        print("","")
        i = menuPromt()
