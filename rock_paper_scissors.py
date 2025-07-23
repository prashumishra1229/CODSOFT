import random

choices = ["rock", "paper", "scissors"]

print("=== ROCK PAPER SCISSORS GAME ===")
print("Type 'quit' to exit anytime.\n")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Decide winner
    if user == computer:
        print("It's a draw!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!\n")
    else:
        print("Computer wins!\n")
