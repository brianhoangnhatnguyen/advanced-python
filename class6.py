class one:
    def display(self):
        print("yup")

class two:
    def display(self):
        print("mhm")

class three(two, one):
    def display(self):
        print("no")

tres = three()
tres.display()