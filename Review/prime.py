num = int(input("Enter the numer to check for prime or not "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("prime number")
            break
        else :
            print("not a prime number")
else:
    print("Not a prime number ")