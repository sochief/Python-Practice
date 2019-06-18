number = 23
running = True
while running:
    guess = int(input('Enter an integer: '))
    
    
    if guess == number:
        print('Congatulations!')
        running = False
    elif guess < number:
        print('Guess is less than number')
    else:
        print('Guess is more than number')
else:
    print('The loop is over')

print('Done')