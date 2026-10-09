import random
items=['rock','paper','scissors']
def get_user_choice():
    player_choice=input('Choose rock,paper or scissors:')
    if player_choice in items:
        return player_choice
    else:
        print("Invalid input")
def get_computer_choice():
    computer_choice=random.choice(items)
    return computer_choice
def display_choices(player_choice,computer_choice):
    print(f"You choose {player_choice}")
    print(f"Computer chooses {computer_choice}")
def determine_winner(player_choice,computer_choice):
    if player_choice==computer_choice:
        print("It's a tie!")
    elif ((player_choice=='rock' and computer_choice=='scissors' or
          player_choice=='paper' and computer_choice=='rock' or
          player_choice=='scissors' and computer_choice=='paper')):
          print (f"{player_choice} beats {computer_choice}, You win!")
    else:
        print("Computer wins!")
def play_game():
    while True:
        player_choice=get_user_choice()
        computer_choice=get_computer_choice()
        display_choices(player_choice,computer_choice)
        determine_winner(player_choice,computer_choice)
        shd_continue=input("Continue(y/n)?")
        if shd_continue=='n':
            break
play_game()


        