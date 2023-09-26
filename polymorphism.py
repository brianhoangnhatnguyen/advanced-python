# Predefined Polymorphism:
# Len: calculates the length of something.


print(len(['H', 'ell', 'o', 'Wo', 'r', 'ld!']))
print(len("Hello World!"))
print('')

def add(a, b, c = 0):
    return a + b + c

print(add(4, 2, 1))
print(add(4, 2))