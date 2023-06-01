import random

def guess_number():
    number = random.randint(0, 100)
    while True:
        guess = int(input("Guess a number between 0 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it right!")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                guess_number()
            else:
                print("Thank you for playing!")
                return

guess_number()

