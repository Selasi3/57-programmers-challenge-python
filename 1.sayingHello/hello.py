def getName():
    while(True):
        
        name = input("What is your name?\n")
        return name
          


def greeting(myname):
    
    print(f"Hello {myname}, nice to meet you!")

def run():
    
    myname = getName()
    greeting(myname)
    
    


if __name__=="__main__":
    run()
    
    
