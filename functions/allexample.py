from functools import reduce

def max_of_three(a, b, c):
    return max(a, b, c)

def is_even(n):
    return n % 2 == 0

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def double_numbers(nums):
    return list(map(lambda x: x * 2, nums))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(nums):
    return list(filter(is_prime, nums))

def product_of_list(nums):
    return reduce(lambda x, y: x * y, nums)

def to_uppercase(words):
    return list(map(str.upper, words))

def longest_word(words):
    return reduce(lambda a, b: a if len(a) > len(b) else b, words)

# Test cases
print(max_of_three(3, 7, 5))  # Output: 7
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
print(count_vowels("hello world"))  # Output: 3
print(factorial(5))  # Output: 120
print(fibonacci(6))  # Output: 8
print(double_numbers([1, 2, 3, 4]))  # Output: [2, 4, 6, 8]
print(filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [2, 3, 5, 7]
print(product_of_list([1, 2, 3, 4]))  # Output: 24
print(to_uppercase(["hello", "world"]))  # Output: ["HELLO", "WORLD"]
print(longest_word(["apple", "banana", "strawberry"]))  # Output: "strawberry"
