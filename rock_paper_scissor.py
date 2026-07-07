import random

emoji={"r":"🧱","p":"📄","s":"✂️"}
choices =('r', 'p', 's')

print("ROCK, PAPER, SCISSORS GAME!!!\n")

while True:
    player_choice = input("Enter your choice (r,p,s): ").lower()
    if player_choice not in choices:
        print('\nInvalid Choice!\n')
        continue

    computer_choice = random.choice(choices)

    print(f"\nPlayer chose: {emoji[player_choice]} ")
    print(f"\nComputer chose: {emoji[computer_choice]} ")

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

    reply = input("\nPlay again? (y/n): ").lower()
    if reply == 'n':
        break
