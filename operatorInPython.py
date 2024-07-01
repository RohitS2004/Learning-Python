# Ternary operator

a = 20 
b = 10

print("Hello") if 10 > 5 else print("World")
print(("a is minimum", "b is minimum")[a < b])
print({True:'a is minimum', False:'b is minimum'}[a < b])

# 'and' logical operator looks for the last true value
# 'or' logical operator looks for the first true value
