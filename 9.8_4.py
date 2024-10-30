origlist = [45, 32, 88]
print(origlist)
print(id(origlist))

newList = origlist + ['cat']
print(newList)
print(id(newList))

origlist.append('Cat')
print(origlist)
print(id(origlist))