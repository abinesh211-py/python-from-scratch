age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

# Checking voting eligibility using comparison operators
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Checking discount eligibility using logical operators
if age < 18 or age >= 60 or is_student:
    print("You are eligible for a discount!")
else:
    print("Sorry, no discount available.")

# Checking if a number is both positive and even
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print(f"{num} is a positive even number.")
else:
    print(f"{num} is not a positive even number.")

# Demonstrating 'not' operator
password = input("Enter your password: ")
if not password:
    print("Password cannot be empty!")
else:
    print("Password set successfully.")
