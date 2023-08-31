# Classes:
class Fruit:
    color = ""
    price = ""
    # def setvalues(self, color, price):
    #     self.color = color
    #     self.price = price
    def __init__(self, color, price):
        self.color = color
        self.price = price
    def display(self):
        print(f"Color: {self.color}, Price: {self.price}")

# If we want to use common properties/variables that is defined in the class, we need to create Object.

apple = Fruit("red", 2.99) # Define object; here "apple" is an object
apple.display()

banana = Fruit("yellow", 1.99)
banana.display()

orange = Fruit("orange", 3.99)
orange.display()

class Triangle:
    base = ""
    height = ""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def areaTriangle(self):
        print(self.base * self.height / 2)

t1 = Triangle(10,20)
t1.areaTriangle()

t2 = Triangle(20,30)
t2.areaTriangle()

t3 = Triangle(30,40)
t3.areaTriangle()
