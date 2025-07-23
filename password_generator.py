import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        return None

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return winner

def rock_paper_scissors():
    print("===== ROCK PAPER SCISSORS =====")
    rounds = int(input("How many rounds do you want to play? (e.g., 3): "))
    user_score, computer_score = 0, 0

    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        result = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

    print("\n===== FINAL RESULT =====")
    if user_score > computer_score:
        print(f"You win the game! Final Score: {user_score}-{computer_score}")
    elif user_score < computer_score:
        print(f"Computer wins the game! Final Score: {user_score}-{computer_score}")
    else:
        print(f"It's a tie! Final Score: {user_score}-{computer_score}")

if __name__ == "__main__":
    rock_paper_scissors()
