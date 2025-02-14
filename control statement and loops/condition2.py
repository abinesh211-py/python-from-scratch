name = input("Enter the name : ")
if len(name) < 3:
    print("Name should be more than three character")
elif len(name) >50 :
    print("Name should not be more than 50 character ")
else:
    print("Name looks good")
