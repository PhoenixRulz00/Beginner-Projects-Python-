import random

minimum = int(input("Specify the minimum number you want to guess: "))
maximum = int(input("Specify the maximum number you want to guess: "))

number_to_guess = random.randint(minimum, maximum)
number_of_guesses =0

while True:
    number_of_guesses+=1
    try:
        guess = int(input(f"Guess the number between {minimum} and {maximum}: "))

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
