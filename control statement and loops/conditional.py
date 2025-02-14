price = 1000000
credit=input("How is the credit (good / bad):").lower()
if credit == "good" :
    downPayment = 0.1 * price
else:
    downPayment = 0.2 * price
print(f"The Downpayment of {credit} is Rs.{downPayment}")