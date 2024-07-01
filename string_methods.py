import math

firstName = "Rohit"

print(firstName.lower())
print(firstName.upper())
print(firstName)

multiLine = '''
Hello there, 
My name is Jarvis
'''

print(multiLine.title()) # converts the string to proper case replacing all the first letter of the words with a uppercase 
print(multiLine.replace("Hello", "Hi")) # replace the word with a given word
print(multiLine) # all the string methods does not affect the original string 

sentence = '          Hello     '
print(len(sentence.strip()))
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))

print("")


value = "CodeVerse"
print(value.center(30, "=")) # center the string value, 30 is the total length that we want and = is the value by which we want to fill the empty space
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Croissant".ljust(16, ".") + "$50".rjust(4))


print(firstName[0])
print(firstName[-1])
print(firstName[0:-1])

print(firstName.startswith("R"))
print(firstName.endswith("t"))

boolValue = bool("Hello")
print(boolValue)

print("")

price = 100
bestPrice = int(100)
print(isinstance(price, int))
print(isinstance(bestPrice, int))

cgpa = 3.89
perc = float(10.9)
print(type(cgpa))

comp = 2 + 3j
print(type(comp))
print(comp.real)
print(comp.imag)

print(abs(cgpa)) # absolute value
print(round(cgpa))
print(round(cgpa, 1)) # round one value up

print(math.sqrt(4))
print(math.pi)
print(math.pow(2, 10))

# ! In python / is used for regular division means it will give the answer with decimal values in it

# ! And // is used for floor division to give only the integer part 

print(cgpa)
print(math.ceil(cgpa))
print(math.floor(cgpa))

print(ord('A')) # returns the ASCII value of the given character



