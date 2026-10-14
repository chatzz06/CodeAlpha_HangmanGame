
import random

def play_hangman():
    words = ["python", "computer", "program", "developer", "keyboard"]
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME")
    print("=" * 40)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_attempts} incorrect guesses allowed.")

    while incorrect_guesses < max_attempts:
        # Display the word with unguessed letters hidden
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")

        # Check whether the player has guessed the word
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print(f"The word was: {secret_word}")
            return

        guess = input("Enter a single letter: ").strip().lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    print("\nGame over! You have used all your attempts.")
    print(f"The correct word was: {secret_word}")


def main():
    while True:
        play_hangman()

        choice = input("\nWould you like to play again? (yes/no): ")
        if choice.strip().lower() not in ("yes", "y"):
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
