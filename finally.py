import time

try:
    f = open('poem.txt')
    while True: # our usual file reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end = ' ')
        time.sleep(2) #To make sure it runs for a while
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    f.close()
    print('(Cleaning up: Closed the file)')