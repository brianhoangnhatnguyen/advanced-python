# Classes:
class Fruit:
    color = ""
    price = ""

# If we want to use common properties/variables that is defined in the class, we need to create Object.

apple = Fruit() # Define object; here "apple" is an object
banana = Fruit()
orange = Fruit()

apple.color = "Red"
apple.price = 2.99

banana.color = "Yellow"
banana.price = 5.99

orange.color = "Orange"
orange.price = 1.99

# print(isinstance(apple, Fruit))  Variable -> Instance, Property, Attribute
print(f"Color: {apple.color}, Price: {apple.price}") # {placeholder/container/variable}
print(f"Color: {banana.color}, Price: {banana.price}")
print(f"Color: {orange.color}, Price: {orange.price}")
