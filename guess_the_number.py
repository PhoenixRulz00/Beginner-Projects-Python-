import random

number_to_guess = random.randint(1,100)
number_of_guesses =0

while True:
    number_of_guesses+=1
    guess = int(input("Guess the number between 1 and 100: "))

    if guess<number_to_guess:
        print("Too Low!")
    elif guess>number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {number_of_guesses} guesses")
