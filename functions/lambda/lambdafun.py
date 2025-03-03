from functools import reduce

# 1. Square a Number
square = lambda x: x ** 2
print(square(5))  # Output: 25

# 2. Find the Maximum of Two Numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 15))  # Output: 15

# 3. Check if a Number is Even or Odd
is_even = lambda x: x % 2 == 0
print(is_even(8))  # Output: True
print(is_even(7))  # Output: False

# 4. Convert Temperature from Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_to_fahrenheit(25))  # Output: 77.0

# 5. Get the First Character of a String
first_char = lambda s: s[0]
print(first_char("Python"))  # Output: P

# 6. Double Each Number in a List (map())
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# 7. Filter Even Numbers (filter())
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evans = list(filter(lambda x: x % 2 == 0, numbers))
print(evans)  # Output: [2, 4, 6, 8]

# 8. Find the Product of All Numbers (reduce())
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# 9. Sort a List of Tuples by the Second Element
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(4, 1), (2, 2), (1, 3)]

# 10. Find the Longest Word in a List
words = ["apple", "banana", "strawberry"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest)  # Output: "strawberry"
