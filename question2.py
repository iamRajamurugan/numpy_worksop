def is_palindrome(number):
    str_number = str(number)
    reversed_str = str_number[::-1]
    return str_number == reversed_str

number = int(input("Enter a number:"))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
