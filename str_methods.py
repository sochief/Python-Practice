name = 'Turkey' #String object

if name.startswith('Tur'):
    print('\n\nString starts with Tur')
if 'e' in name:
    print('\n\nString has a letter e')
if name.find('key') != -1:
    print('\n\nString has the string "key"\n\n')

razdelitel = ' '
myList = ['Brazil','China','Russia','India']
print(razdelitel.join(myList))
