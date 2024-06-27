import random

def guess_number_game():
    while True:
        secret_number = random.randint(1, 10)
        guess = int(input("Guess the secret number (between 1 and 10): "))

        match guess:
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
            case secret_number:
                print("Congratulations, you guessed it!")
            

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    guess_number_game()
