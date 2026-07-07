import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emoji={"r":"🧱","p":"📄","s":"✂️"}
choices = tuple(emoji.keys())

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

def determine_winner(player_choice, computer_choice, player_score, computer_score):

    if player_choice == computer_choice:
        print("\nTie!")
    elif player_choice == 'r' and computer_choice == 's':
        print("\nRock Crushed Scissors! You Win!")
        player_score+=1
    elif player_choice =='p' and computer_choice == 'r':
        print("\nPaper Covered the Rock! You Win!")
        player_score+=1
    elif  player_choice =='s' and computer_choice == 'p':
        print("\nScissor Cuts the Paper! You Win!")
        player_score+=1
    else:
        print("\nYou Lose!")
        computer_score+=1
    
    return player_score, computer_score

def play_game():
    while True:

        rounds = int(input("How many rounds you want to play?(Best of 3 or 5) : "))

        if rounds%2==0:
            print("\nTry Odd number of rounds!\n")
            rounds=3
            print("Automatically assigning the smallest playable odd number! (3)")

        current_round=1
        player_score = 0
        computer_score = 0

        while rounds>0: 
            print(f"\nROUND {current_round} STARTS!\n")

            player_choice = get_user_choice()
            computer_choice = random.choice(choices)

            display_choices(player_choice, computer_choice)

            player_score, computer_score = determine_winner(player_choice, computer_choice, player_score, computer_score)

            rounds-=1
            current_round+=1

        print("\n==============================")
        print("          GAME OVER!          ")
        print(f"Final Score -> Player: {player_score} | Computer: {computer_score}")
        print("==============================")
        if player_score>computer_score:
            print("\n🏆 Congratulations! You are the Champion!")
        elif computer_score>player_score:
            print("\n💻 The Computer wins the match. Better luck next time!")
        else:
            print("\n🤝 It's a draw! A hard-fought battle!")

        reply = input("\nPlay again? (y/n): ").lower()
        if reply == 'n':
            print("\nThanks for playing! Goodbye! 👋")
            break
play_game()
