band = {
    'vocals': "Bands"
}
print(band)

band2 = dict(vocals="Plant", guitar="Page") # using the dict constructor
print(band2)

# Access Items
print(band.get('vocals'))
print(band2["vocals"])

# List all keys
print(band2.keys())

# List all values
print(band.values())

# List of key, value pairs as tuple
print(band2.items())

# Verify a key exist in the dict
print("Lime" in band2) # * Using the membership test operator we can check if a key is present in the Dictionary or not

# Change values
band2["vocals"] = "Felix"
print(band2)

band2.update({"bass": "MP4"}) # * Adding another key, value pair in the dictionary
band2.update({"vocals": "Hamper"}) # * Changing an existing key, value pair using the update method
print(band2)
