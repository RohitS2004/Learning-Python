# Lists in python are dynamic in size means that the size of the list will grow as we add more elements to it.

users = ['Dave', 'John', 'Sara']
data = ['Dave', 40, True]
emptyList = []

# print('Dave' in emptyList) # Membership test operator
# print(users[0])
# print(users[-1])
# print(users.index('Dave'))
# print(users[0:2])
# print(users[1:])
# print(len(users))
# users.append('Felix')
# print(users)

# Adding another list in the current list
# users += ['Jason', 'Harry']
# print(users)
# users.extend(['Robert', 'Saul'])
# print(users)
users.insert(0, 'Rohit')
# print(users)
users[2:2] = ['Alex', 'Eddie'] # * Adding value at the second index without removing/changing the current element at that position
# print(users)

# Replacing value
users[1:3] = ['Morgan', 'JP'] # * Replacing the values of 1 and 2 index in the list with the specified list values
# print(users)

users.remove('John') # Removes the specified element if present
val = users.pop() # Removes the last element from the list
# print(val)
# print(users)
del users[0] # Removes the element specified by the index
# print(users)
# del data # Deleting the data list 
data.clear() # Clears the whole list and the list still exists
# print(data)

# Sorting the list
users[1:2] = ['kryo']
# users.sort(key=str.lower)
# print(users)
numbers = [3,4,5,2,9,1,7]
# numbers.sort()
# numbers.sort(reverse=True) # To sort in the descending order
# print(numbers)

# print(sorted(numbers, reverse=True))
# print(numbers)

nums_copy = numbers.copy()
myNums = list(numbers)
myCopy = numbers[:]

# print(nums_copy)
myNums.sort()
# print(myNums)
# print(f'Original: {numbers}')
# print(myCopy)
# print(type(myCopy))

new_List = list([1, 'Rome', 'Dam']) # Creating a list with the list constructor
# print(new_List)


# * TUPLES
# tuples are immutable means the data inside it will not change and the order the data is in will also not change

myTuple = tuple((1,2,3,4))
# print(myTuple)

anotherTuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# print(type(anotherTuple))

# listToTuple = list(myTuple)
# print(listToTuple)
# print(type(listToTuple))
# listToTuple.append(5)
# TupleToList = tuple(listToTuple)
# print(TupleToList)
# print(type(TupleToList))

# * Unpacking
# (one, two, *hey) = anotherTuple
(one, *two, hey) = anotherTuple # First value will go in the one variable and the last value will go into the hey variable and rest of the value in between them will be stored in the form of list inside the two variable
print(one)
print(two)
print(hey)

# print(all((1,2,3,4)))
# print(all([True, True, True]))
# print(all([True,True,False]))
# print(all([0, 0, 0]))



