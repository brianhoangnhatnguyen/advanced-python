# import random
# def gomugomuno():
#     blud = random.randint(1, 100)
#     attempts = 0
#
#     while True:
#         userinput = int(input("Guess a number between 1 and 100. "))
#         attempts += 1
#         if userinput < blud:
#             print("Too low, try again.")
#
#         elif userinput > blud:
#             print("Too high, try again.")
#
#         else:
#             print(f"You got it! The number was {blud} and took you {attempts} tries to get it.")
#             break
#
# gomugomuno()

array = [1, 2, 3, 4, 5]

print(array[2])

array[1] = 'a'
print(array)

array.append(6)
print(array)

array.pop(0)
print(array)

print(len(array))

check = 3 in array
print(check)

