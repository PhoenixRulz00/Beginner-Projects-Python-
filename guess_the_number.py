import random

number_to_guess = random.randint(1, 100)
number_of_guesses =0

while True:
    number_of_guesses+=1
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess<number_to_guess:
            if number_to_guess-guess > 10:
                print("Too Low!")
            else:
                print("Low!")
        elif guess>number_to_guess:
            if guess-number_to_guess > 10:
                print("Too High!")
            else:
                print("High!")
        else:
            print(f"Congratulations! The Secret number is {number_to_guess}.")
            print(f"You guessed the number in {number_of_guesses} guesses!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
