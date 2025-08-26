
import random

def play():
    target = random.randint(1, 100)
    attempts = 0
    print("=== Number Guessing Game (1 to 100) ===")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please guess between 1 and 100.")
                continue
        except ValueError:
            print("Enter a valid integer.")
            continue

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"🎉 Correct! The number was {target}. Attempts: {attempts}")
            break

def main():
    while True:
        play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
