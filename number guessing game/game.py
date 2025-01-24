import random

def play_game():
    # Form a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # User input
            guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1

            # Provide feedback
            if guess < number_to_guess:
                print("It'sToo low! Try again.")
            elif guess > number_to_guess:
                print("It's Too high! Try again.")
            else:
                print(f"Correct! The number was {number_to_guess}. You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        play_game()
        # Ask user whether they want to play another round
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    main()
