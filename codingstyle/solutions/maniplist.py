# The first example
# List comprehension

a = [3, 4, 5]
b = [i for i in a if i > 4]
print(b)

# Or:
a = [3, 4, 5]
b = list(filter(lambda x: x > 4, a))
print(b)

# The second example
# List comprehension
a = [3, 4, 5]
a = [ i + 3 for i in a]
print(a)

# Or:
a = [3, 4, 5]
a = list(map(lambda x: x + 3, a))
print(a)