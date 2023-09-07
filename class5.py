class A:
    def displayMot(self):
        print("Class A")

class B(A):
    def displayHai(self):
        print("Class B")

class C(B):
    def displayBa(self):
        print("Class C")
        super().displayHai()
        super().displayMot()


printC = C()
printC.displayBa()