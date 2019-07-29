def printMax(x,y):
    '''Prints the maximmum of two numbers.
The two values must be integers.'''
    x=int(x) #converts to integers, if possible
    y=int(y)
    
    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")

printMax(3,5)
print(printMax.__doc__)