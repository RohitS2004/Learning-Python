message = "%s is %s years old" %("Dave", 40)
print(message)

message2 = "{} lives in {}".format("John", "Chicago")
print(message2)

message3 = "{1} is {0} years old".format(40, "Kelly")
print(message3)

person = "Niger"
occupation = "Scientist"
message4 = "{person} is a {occupation}".format(person=person, occupation=occupation)
print(message4)

info = {
    "name" : "Lambert",
    "coins" : 100
}
message5 = "{name} has {coins}".format(**info)
print(message5)

# * F-STRINGS

msg = f"{person} is a {occupation}"
print(msg)

msg2 = f"{info.get("name")} has {info.get("coins")}"
print(msg2)


# You can also pass the formaatting options
num = 10
print(f"2.25 time {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"2.25 time {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 2 is {num / 2.0:.2%}")

