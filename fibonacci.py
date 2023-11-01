number = int(input("Enter a number: "))
n1, n2 = 0, 1
count = 0

if number <= 0:
    print("Number must be a positive number.")
elif number == 1:
    print(f"Fibonacci series is up to {number}: ", n1)
else:
    print("Fibonacci series: ")
    while count < number:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1