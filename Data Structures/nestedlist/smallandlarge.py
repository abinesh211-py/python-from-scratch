list2 = list(map(int,input("Enter the numbers with spaces :").split()))
largest = list2[0]
smallest = list2[0]
for numbers in list2:
    if largest < numbers :
        largest = numbers
    if smallest > numbers :
        smallest = numbers 
print(f"Largest number is : {largest}")
print(f"Smallest number is : {smallest}")