import random

emoji={"r":"🧱","p":"📄","s":"✂️"}
choices =('r', 'p', 's')

print("ROCK, PAPER, SCISSORS GAME!!!\n")

def get_user_choice():
    while True:
        player_choice = input("Enter your choice (r,p,s): ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print('\nInvalid Choice!\n')

def display_choices(player_choice, computer_choice):
    print(f"\nPlayer chose: {emoji[player_choice]} ")
    print(f"\nComputer chose: {emoji[computer_choice]} ")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("\nTie!")
    elif player_choice == 'r' and computer_choice == 's':
        print("\nRock Crushed Scissors! You Win!")
    elif player_choice =='p' and computer_choice == 'r':
        print("\nPaper Coverd the Rock! You Win!")
    elif  player_choice =='s' and computer_choice == 'p':
        print("\nScissor Cuts the Paper! You Win!")
    else:
        print("\nYou Lose!")

def play_game():
    while True: 
        rounds = int(input("How many rounds you want to play? : "))

        player_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(player_choice, computer_choice)

        determine_winner(player_choice, computer_choice)

        reply = input("\nPlay again? (y/n): ").lower()
        if reply == 'n':
            break

play_game()
