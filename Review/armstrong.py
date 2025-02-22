num = int(input("Enter the number: "))  # Convert input to integer
t = len(str(num))  # Count number of digits
total_sum = 0  # Correct variable name
temp = num  # Store original number in temp

while temp > 0:
    digit = temp % 10  # Extract last digit
    total_sum += digit ** t  # Add power of digit to sum
    temp //= 10  # Remove last digit

if total_sum == num:  # Compare sum with original number
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is NOT an Armstrong Number")
