def getString():
    string = ""
    while(True):
        string = input("What is the input string?\n")
        return string

def getStringLength(name): 
    return len(name)

def sentence(string , length):
    print(f"{string} has {length} characters. ")

def run():
    word = getString()
    length = getStringLength(word)
    sentence(word, length)







if __name__=="__main__":
    run()
    
    
