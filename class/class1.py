# Student Class
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print(f"\nStudent Details:\nName: {self.name}, Age: {self.age}, Marks: {self.marks}")

# Employee Class
class Employee:
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus
    
    def total_salary(self):
        return self.salary + self.bonus

    def display_salary(self):
        print(f"\nTotal Salary: {self.total_salary()}")

# Bank Class
class Bank:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance!")
    
    def get_balance(self):
        return self.balance

# Animal Inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"

# Interactive Part
if __name__ == "__main__":
    # Student Class Interaction
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))
    student = Student(name, age, marks)
    student.display()
    
    # Employee Class Interaction
    salary = float(input("\nEnter employee salary: "))
    bonus = float(input("Enter employee bonus: "))
    employee = Employee(salary, bonus)
    employee.display_salary()
    
    # Bank Class Interaction
    bank = Bank()
    while True:
        print("\nBank Menu:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            bank.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(amount)
        elif choice == 3:
            print(f"Current Balance: {bank.get_balance()}")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")
    
    # Animal Class Interaction
    animal_type = input("\nEnter animal type (Dog/Cat): ").strip().lower()
    if animal_type == "dog":
        animal = Dog()
    elif animal_type == "cat":
        animal = Cat()
    else:
        print("Unknown animal!")
        animal = None
    if animal:
        print(f"Animal sound: {animal.speak()}")
    
    # Calculator Class Interaction
    calc = Calculator()
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Addition: {calc.add(num1, num2)}")
    print(f"Subtraction: {calc.subtract(num1, num2)}")
    print(f"Multiplication: {calc.multiply(num1, num2)}")
    print(f"Division: {calc.divide(num1, num2)}")
