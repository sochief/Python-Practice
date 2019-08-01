poem = '''\
    Programming is fun
    When work is done
    if you wanna make your work also fun:
            use Python!'''

f = open('poem.txt','w') #open for 'w' writing
f.write(poem) #write text to file
f.close() #close the file

f = open('poem.txt') #if no mode is specified 'r'ead mode is assumed by default

while True:
    line = f.readline()
    if len(line) == 0: # Zero lenght indicated End of file
        break
    print(line, end = ' ')
f.close() #close the file