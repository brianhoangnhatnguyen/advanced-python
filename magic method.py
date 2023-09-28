class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return (f"name: {self.name}, id: {self.id}")

    def display(self):
         print(f"{self.name}, {self.id}")

studne1 = student("brian", 123123)
studne2 = student("halalalalalalala", 99999999)

print(studne1)
print(studne2)

class addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self,other):
        return addition(self.num1 + other.num1, self.num2 + other.num2)



add1 = addition(1, 2)
add2 = addition(3,5)
result = add1 + add2
print(result.num1, result.num2)
