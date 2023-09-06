class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def display(self):
        print("Class C")


printC = C()
printC.display()