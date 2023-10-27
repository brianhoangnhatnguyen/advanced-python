number = int(input("Enter a number: "))
def factorial(num):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

result = factorial(number)

print(result)