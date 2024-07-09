# Closure is a function having access to the  scope of its parent function after the parent function has returned

def parent (person, count) :

    def child () :
        nonlocal count
        count = count -1 

        if count > 1: 
            print(f'{person} has {count} coins')
        elif count ==1:
            print(f'{person} has {count} coins left')
        else:
            print(f'{person} is out of coins')

    return child # When the parent returns this child function than the whole parent function has finished executing and then we have called the child function and we can see that we are able to access its members even though it has done executingb

tommy = parent('Dave', 3)
tommy()
tommy()
