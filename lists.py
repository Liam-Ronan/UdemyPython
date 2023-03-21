"""
sen = 'hello %s %s, youre invited'
#print(sen%("Amy"))

arr =  ["Liam", "Amy", "Jake"]

for i in arr:
    print(sen%(i))

sen3 = "I am %s and i am %d"
print(sen3 % ("Liam", 22))
"""

shoppingList = ["Cake", "eggs", "apples", "cherries"]
shoppingList[2] = "chocolate"
del shoppingList[2]
#Looping through list
for i in shoppingList:
    print(i)

arrayOne = [2, 54, 67]
arrayTwo = [45, 277, 32]
print(len(shoppingList))

numArray = [45, 43, 10004, 1, -5]

print(max(numArray))
print(min(numArray))

shoppingList.append("Liam")
print(shoppingList)
print(shoppingList.count("Liam"))





