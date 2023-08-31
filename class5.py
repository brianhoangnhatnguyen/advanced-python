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