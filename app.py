<<<<<<< HEAD
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get password length from user
try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        password = generate_password(length)
        print("Generated password:", password)
except ValueError:
    print("Please enter a valid number.")
=======
print("Welcome to Mini Calculator!")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator!"

print("Result:", result)
>>>>>>> dev-feature
