# number = int(input("Enter a number: "))
# n1, n2 = 0, 1
# count = 0
#
# if number <= 0:
#     print("Number must be a positive number.")
# elif number == 1:
#     print(f"Fibonacci series is up to {number}: ", n1)
# else:
#     print("Fibonacci series: ")
#     while count < number:
#         print(n1)
#         sum = n1 + n2
#         n1 = n2
#         n2 = sum
#         count += 1

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n_length = int(input("Enter a number: "))

if n_length <= 0:
    print("The length can't be negative.")
else:
    print(f"Fibonacci series: ")

    for i in range(n_length):
        print(fibonacci(i))