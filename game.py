import random

def print_welcome():
    print("=" * 40)
    print("Number Guessing Game")
    print("=" * 40)
    print("I am thinking of a number between 1 and 100.")
    print("You have limited attempts to guess it.\n")

def get_difficulty():
    print("Select difficulty level:")
    print("1. Easy   (10 attempts)")
    print("2. Normal (7 attempts)")
    print("3. Hard   (5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    target = random.randint(1, 100)
    attempts = get_difficulty()
    guesses_taken = 0

    print(f"\nOkay! I have chosen a number. You have {attempts} attempts.\n")

    while guesses_taken < attempts:
        try:
            guess = int(input(f"Attempt {guesses_taken + 1}/{attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        guesses_taken += 1

        if guess < target:
            print("Too low! Try a higher number.\n")
        elif guess > target:
            print("Too high! Try a lower number.\n")
        else:
            print(f"\nCongratulations! You guessed it in {guesses_taken} attempts.")
            break
    else:
        print(f"\nOut of attempts! The number was {target}.")

def main():
    print_welcome()

    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
