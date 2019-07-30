print('\n\n\n\n\n\n\nSimple Assigment\n')
shopList = ['apple','mango','carrot','banana']
myList  = shopList #myList is just another name pointing to the same object
del shopList[0]

print('shoplist is ',shopList,"\n")
print('myList is ',myList,"\n")

print('Copy by making a full slice\n')
myList = shopList[:]#make a copy by doing a full slice
del myList[0]#remove first item

print('ShopList is ',shopList,'\n')
print('MyList is ',myList,'\n')
print('Notice, that now the two lists are different')