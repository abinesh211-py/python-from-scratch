n = int(input("Enter the number to be in the series "))
a, b = 0, 1  # Step 1: Initialize first two numbers

print("Fibonacci Sequence:")
for i in range(n):  # Step 2: Generate sequence
    print(a, end=" ")  # Print the current number
    a, b = b, a + b  # Step 3: Update a and b
