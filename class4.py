from abc import ABC, abstractmethod
# Inheritance:
class yes:
    def asdlfj(self):
        print("hello hello")

    def fjfjfj(self):
        print("1233454567")



class no(yes):
    def onetwothree(self):
        print("qwerty")

    def hi(self):
        print("hi")

object = no()
object.fjfjfj()
object.asdlfj()

# Method Overloading:
class iphone:
    def __init__(self):
        print("ios device")

class samsung(iphone):
    def __init__(self):
        super().__init__()
        print("android device")

sam = samsung()

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        print(self.dim1 * self.dim2 * 0.5)


class Rectangle(Shape):
    def area(self):
        print(self.dim1 * self.dim2)

shape1 = Triangle(10, 20)   
shape1.area()

shape2 = Rectangle(30, 100)
shape2.area()

object = Shape(dim1=123, dim2=123)
object.area()