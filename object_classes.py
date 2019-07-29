#This is a shopping list
shopList = ['apple','mango','carrot','banana']

print('\n I have ', len(shopList), ' items to purchase. ')
print('\n These items are: ', end =' ')
for item in shopList:
    print(item, end = ' ')
    if(item == shopList[-1]):
        print("\n")


print(" I also have to buy rice. ")
shopList.append('rice')
print('\n My shopping list now ', shopList)

print('\n I will sort my list now')
shopList.sort()
print("\n My sorted list is", shopList)


print("\n My first item is ",shopList[0])
oldItem = shopList[0]
del shopList[0]
print("\n I already bought ", oldItem )
print("\n List of things left ", shopList )