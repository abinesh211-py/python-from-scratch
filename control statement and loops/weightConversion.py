weight = input("Enter your weight: ")  # Taking input as a string
unit = input("Is this in Pounds (lbs) or Kilograms (kg)? Type 'pounds' or 'kg': ").strip().lower()

# Check if weight is a valid number
if weight.replace('.', '', 1).isdigit():  # Allows decimal numbers
    weight = float(weight)  # Convert to float for calculations

    if unit == "pounds" or unit == "lbs":
        converted = weight * 0.45  # Convert pounds to kg
        print(f"Your weight in Kilograms: {converted:.2f} kg")

    elif unit == "kg":
        converted = weight / 0.45  # Convert kg to pounds
        print(f"Your weight in Pounds: {converted:.2f} lbs")

    else:
        print("Invalid unit. Please enter 'pounds' or 'kg'.")

else:
    print("Invalid input. Please enter a number for weight.")
