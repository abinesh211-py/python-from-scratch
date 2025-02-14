print("Welcome to the Car Game!")
print("Commands: start | stop | accelerate | exit")

car_started = False
while True:
    command = input("> ").lower()
    
    if command == "start":
        if car_started:
            print("The car is already started!")
        else:
            car_started = True
            print("Car started. Ready to go!")
    
    elif command == "stop":
        if not car_started:
            print("The car is already stopped.")
        else:
            car_started = False
            print("Car stopped.")
    
    elif command == "accelerate":
        if car_started:
            print("Car is accelerating! Vroom Vroom!")
        else:
            print("You need to start the car first!")
    
    elif command == "exit":
        print("Exiting the game. Thanks for playing!")
        break
    
    else:
        print("Invalid command! Try again.")
