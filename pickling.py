#Python provides a standard module called pickle 
#using which you can store any Python
#object in a file and then get it back
#later. This is called storing 
#the object persistently.

import pickle
# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of strings to buy
shoplist = ['apple','mango','carrot']

#Write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist, f)#dump the object to a file
f.close()

del shoplist #destroy the shoplist variable

#let's read it back from the storage

f = open(shoplistfile,'rb')
storedlist = pickle.load(f)#load the object from the file
print(storedlist)
