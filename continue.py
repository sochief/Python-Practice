while True:
    s = input("Enter something: ")
    if s == 'quit':
        break
    if len(s)<11:
        print("Too small")
    continue
print("Input is of sufficient lenght")