def findmissingdigits(number):
    digits = set("0123456789")
    mobile_number = set(number)
    missing = digits - mobile_number

    return (missing)

number = input("input number: ")

number = ''.join(filter(str.isdigit, number))

missing_digits = findmissingdigits(number)

if missing_digits:
    print("missing digits: ", ''.join(sorted(missing_digits)))
else:
    print("no missing digits")