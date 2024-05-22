def find_max(a, b):
    if a > b:
        return a
    else:
        return b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
max_number = find_max(a, b)
print(f"The maximum of {a} and {b} is {max_number}.")
