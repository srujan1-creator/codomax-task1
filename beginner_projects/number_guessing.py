"""
=============================================================================
Project 2: Smart Number Guessing Game
Module: 02_beginner_projects / project2_number_guessing.py
Description: An interactive guessing game featuring multiple difficulty levels,
             dynamic high/low hints, attempt tracking, score calculation,
             and automated simulation testing.
=============================================================================
"""

import random
import sys


class NumberGuessingGame:
    DIFFICULTIES = {
        "1": ("Easy", 10, 50),     # 10 attempts, range 1-50
        "2": ("Medium", 7, 100),   # 7 attempts, range 1-100
        "3": ("Hard", 5, 200)      # 5 attempts, range 1-200
    }

    def __init__(self, difficulty_key: str = "2"):
        diff_info = self.DIFFICULTIES.get(difficulty_key, self.DIFFICULTIES["2"])
        self.mode_name = diff_info[0]
        self.max_attempts = diff_info[1]
        self.max_range = diff_info[2]
        self.secret_number = random.randint(1, self.max_range)
        self.attempts_taken = 0
        self.has_won = False

    def evaluate_guess(self, guess: int) -> str:
        self.attempts_taken += 1
        diff = abs(guess - self.secret_number)

        if guess == self.secret_number:
            self.has_won = True
            return "CORRECT"
        elif guess < self.secret_number:
            proximity = " (Very close!)" if diff <= 3 else ""
            return f"TOO LOW{proximity}"
        else:
            proximity = " (Very close!)" if diff <= 3 else ""
            return f"TOO HIGH{proximity}"

    def calculate_score(self) -> int:
        if not self.has_won:
            return 0
        remaining_attempts = self.max_attempts - self.attempts_taken
        return 100 + (remaining_attempts * 25)


def run_demo():
    print("=" * 60)
    print(" RUNNING NUMBER GUESSING GAME SIMULATION (BINARY SEARCH BOT) ")
    print("=" * 60)
    game = NumberGuessingGame("2")  # Range 1-100, 7 attempts
    print(f"Target Secret Number: {game.secret_number} (Hidden from player)")
    print(f"Difficulty: {game.mode_name} (Max attempts: {game.max_attempts}, Range: 1-{game.max_range})")

    low = 1
    high = game.max_range

    while game.attempts_taken < game.max_attempts and not game.has_won:
        guess = (low + high) // 2
        feedback = game.evaluate_guess(guess)
        print(f"  Attempt {game.attempts_taken}/{game.max_attempts}: Bot guessed {guess:>3} -> Feedback: {feedback}")

        if feedback == "CORRECT":
            break
        elif "LOW" in feedback:
            low = guess + 1
        elif "HIGH" in feedback:
            high = guess - 1

    if game.has_won:
        print(f"\n[VICTORY] Number found in {game.attempts_taken} attempts! Score: {game.calculate_score()} pts.")
    else:
        print(f"\n[GAME OVER] Bot ran out of attempts. Secret was {game.secret_number}.")


def play_game():
    print("=" * 50)
    print("    WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 50)
    print("Select Difficulty:")
    print("  1. Easy   (Range 1-50,  10 Attempts)")
    print("  2. Medium (Range 1-100,  7 Attempts)")
    print("  3. Hard   (Range 1-200,  5 Attempts)")

    choice = input("Enter choice (1-3) [default 2]: ").strip() or "2"
    game = NumberGuessingGame(choice)

    print(f"\nGame started on [{game.mode_name}] mode! Guess the number between 1 and {game.max_range}.")

    while game.attempts_taken < game.max_attempts:
        remaining = game.max_attempts - game.attempts_taken
        print(f"\nAttempts remaining: {remaining}")
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Please enter a valid integer.")
            continue

        result = game.evaluate_guess(guess)
        if result == "CORRECT":
            print(f"\n[WIN] Congratulations! You guessed the number {game.secret_number} in {game.attempts_taken} attempts!")
            print(f"Your Final Score: {game.calculate_score()} points")
            return
        else:
            print(f"Hint: {result}")

    print(f"\n[GAME OVER] You've run out of attempts. The number was {game.secret_number}.")


if __name__ == "__main__":
    if "--demo" in sys.argv or not sys.stdin.isatty():
        run_demo()
    else:
        play_game()
