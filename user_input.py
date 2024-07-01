import sys
import random
from enum import Enum

class RPS(Enum):
    # Enums are user defined data types which contains named-constants called enumerator that are associated with integer values
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print(str(RPS(2)).replace("RPS.", ""))

userName = input("Enter your name: ")
userChoice = int(input("Enter...\n1. Rock\n2. Paper\n3. Scissors\n\n"))

if userChoice < 1 or userChoice > 3:
    sys.exit("You must enter 1, 2 or 3")

computerChoice = random.choice("123")
computerChoice = int(computerChoice)

print("You chose: " + str(userChoice))
print("Python chose: " + str(computerChoice))

if (userChoice == 1 and computerChoice == 3) :
    print(userName + " wins..🎇🎇")
elif (userChoice == 2 and computerChoice == 1) :
    print(userName + " wins..🎇🎇")
elif (userChoice == 3 and computerChoice == 2) :
    print(userName + " wins..🎇🎇")
elif (userChoice == computerChoice) :
    print("Game tie...🥱🥱")
else :
    print("Python wins...😔😔")


# The absolute value (or modulus) | x | of a real number x is the non-negative value of x without regard to its sign.

