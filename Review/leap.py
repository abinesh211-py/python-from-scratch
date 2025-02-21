year = int(input("Enter the year:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 ):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")

# year = int(input("Enter the year to check :"))
# if (year % 4 == 0 and year % 100 != 0) :
#     print(f"{year} is a leap year")
# elif (year % 400 == 0):
#     print(f"{year} is a leap year")
# else :
#     print(f"{year} is not a leap year")