# FUNCTIONS are reuasbale block of code which we can call anywhere in our program 

def greet():
    print("Good morning")

# parameters never change but arguments changes with every function call
def sum(number_one, number_two): 
    if (type(number_one) is not int or type(number_two) is not int):
        return 
    return (number_one + number_two)

value = sum(100, 200)
string_value = sum("Hello", "World")
print(string_value)
print(value)

# type(number_one) is not int --> This is used to check if the type is int or not and 'is not'operator is used to check the IDENTITY of two objects

# * NOTE: In python everything is an object 

# def values_default (val, age = 10, name):
    # You cannot have a non-default parameter after a default parameter
    # print(f'{name} {age} {val}')

# values_default(10, 19, "Rohit")


# * SUPPOSE WE DO NOT KNOW HOW MANY ARGUMENTS WILL BE PASSED TO THE FUNCTION SO IN THAT CASE WE CAN USE THE BELOW FUNCTION DEFINITION

def multiple_params (*params):
    print(params)
    print(type(params)) # tuple

multiple_params("Dave", 40, "United States")


# ? When we do not know how many arguments we will pass to the function and also we want the passed arguments to be refered by some keyword so in that case we can use kwargs which are keyword arguments and they are stored in the form of dictionary and can be accessed by their keyword
def mul_named_args (**kwargs):
    print(kwargs)
    print(type(kwargs)) # dictionary

mul_named_args(first="Dave", last="Grey")

