# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print ("Done")
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))  
    guess_count += 1 

    if guess == secret_number:
        print("You Won!")
        break
    else:
        print(f"Wrong guess! {guess_limit - guess_count} attempts left.")

else:
    print( "Sorry, You Lost! The correct number was:", secret_number)

    print("Sorry You Lost")





