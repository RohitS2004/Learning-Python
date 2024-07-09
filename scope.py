name = "Sarah" # Global scope
num = 20

def printName (name) : # Parameter
    global num # Accessing the global num which has a value 20
    num += 10
    color = "lime"

    # name is local scope 
    def greeting () :
        nonlocal color # Changing the parent function scope variable
        color = "aqua"
        print(color)



printName("Dave") # Argument

# scoping works for functions too
def dupPrintUser () :
    printName('Kelly')

dupPrintUser()
