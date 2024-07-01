band = {
    'vocals': "Bands"
}

band2 = dict(vocals="Plant", guitar="Page") # using the dict constructor

# ? ACCESS ITEMS
# print(band.get('vocals'))
# print(band2["vocals"])

# ? LIST ALL KEYS
# print(band2.keys())

# ? LIST ALL VALUES
# print(band.values())

# ? LIST OF KEY, VALUE AS TUPLE
# print(band2.items())

# ? VERIFY A KEY EXISTS IN A DICTIONARY
# print("Lime" in band2) # * Using the membership test operator we can check if a key is present in the Dictionary or not

# ? CHANGE VALUES
band2["vocals"] = "Felix"
band2.update({"bass": "MP4"}) 
# * Adding another key, value pair in the dictionary
band2.update({"vocals": "Hamper"})
 # * Changing an existing key, value pair using the update method

# ? REMOVING FROM THE DICTIONARY
# print(band2.pop("vocals"))
# Returns the value of the popped key

band2["drums"] = "Bahamas"
# print(band2.popitem())
# * popitem() method removes the last item added and returns a tuple containing the (key, value) pair

# ? DELETE AND CLEAR ITEMS
band2["singer"] = "kapi"
del band2["singer"]
# print(band2)

band.clear()
# clear() method clears out the whole dictionary leaving a empty dictionary
# print(band)
del band
# del band deletes the entire dictionary


# ? COPY DICTIONARIES
band3 = band2 # creates a reference, not a copy
band = band2.copy() # create a copy
band4 = dict(band2) # using the constructor function we can also make a copy of the dictionary


# ? NESTED DICTIONARIES
member1 = {
    "name" : "John",
    "position" : "Deck"
}

member2 = {
    "name" : "Sarah",
    "position" : "Captain"
}

members = {
    'member1' : member1,
    'member2' : member2
}
# print(members["member2"]['name'])


# ! SETS
# No duplicates are allowed in the sets

nums = {1,2,3,4}
num2 = set((6,7,8,9))
num3 = {9,9,9,8}
num4 = {1, True, True, False, 0}
# Number 1 is in the first order so it ignores the dupe True and since false is in the first order so it ignores the Number 2
# print(type(num2))
# print(len(num2))
# print(nums)
# print(num3)
# print(num4)
# print(2 in nums)
# You cannot refer to an element in a set with an index position or a key 

# Add a new element to the set
nums.add(5)
# print(nums)
# Add elements from one set to another
nums.update(num2)
# print(nums)
# * NOTE: You can use update with list, tuples and dictionaries too
l = [11, 12, 13, 14]
nums.update(l)
# print(nums)
t = (15, 16, 17, 18, 19)
nums.update(t)
# print(nums)
d = {
    20: "twenty",
    21: "twenty-one"
}
nums.update(d) 
# * NOTE: When you try to add a dictionary into the set only the keys would be added not the values
# print(nums)

# Merge two sets to create a new set
one = {1,2,3}
two = {4,5,6}
three = one.union(two)
# print(three)

# keep only duplicate
d1 = {1, 2, 3, 4, 5, 6, 7}
d2 = {4, 5, 6, 7, 8, 9}
print(d1.intersection(d2))
print(d1.issuperset(d2))
print(d2.issubset(d1))
print(d1.difference(d2))
print(d1.symmetric_difference(d2))






