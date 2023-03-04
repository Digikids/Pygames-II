myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myList)
print('The length is:', len(myList))

myLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(myLetters[4])
print(myLetters[1])
print('The length is:', len(myLetters))

myBread = ['slice1', 'slice2', 'slice3', 'slice4',
           'slice5', 'slice6', 'slice7', 'slice8', 'slice9']
print(myBread[1:4])  # list slicing
print(myBread[2:6])  # list slicing
print('The length is:', len(myBread))


myData = [1, 3.4, 'hello', [1, 2, 3], True]
print(myData)
print(myData[-1])
print('The length is:', len(myData))


# list Methods
# the append() method
# the append() method adds an item to the end of a list
myFriends = ['John', 'Paul', 'George', 'Ringo']
myFriends.append('Brian')
print(myFriends)

# the insert() method
# the insert() method adds an item at the specified index
myFlowers = ['rose', 'tulip', 'daisy', 'lily']
myFlowers.insert(2, 'sunflower')
print(myFlowers)

# the remove() method
# the remove() method removes the specified item
myFruits = ['apple', 'banana', 'cherry', 'orange']
myFruits.remove('banana')
print(myFruits)

# the sort() method
# the sort() method sorts the list in ascending order
myNumbers = [5, 3, 8, 6, 7, 2]
myNumbers.sort()
print(myNumbers)