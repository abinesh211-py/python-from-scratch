list1 = list(map(int,input("Enter the numbers seperated by spaces: ").split()))
num = int(input("Enter the number to be checked: "))
if num in list1:
    print(f"The number {num} is found in {list1}")
else:
    print(f"The number {num} is not found in {list1}")