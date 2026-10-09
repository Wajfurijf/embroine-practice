import random
computer_choice=random.randint(1,100)
while True:
    try:
        player_choice=int(input("Enter a number between 1 and 100:"))
        if player_choice==computer_choice:
            print("You guessed the number")
            break
        elif player_choice>computer_choice:
            print("Too high")
        else:
            print("Too low")
    except ValueError:
        print("Please enter a valid input")
    


