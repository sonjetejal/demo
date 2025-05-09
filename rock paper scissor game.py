import random

options = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\nChoose: rock, paper, or scissors (or type 'exit' to quit)")
    player_choice = input("Your choice: ").lower()

    if player_choice == "exit":
        print("Thanks for playing! Goodbye!")
        break
    elif player_choice not in options:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(player_choice, computer_choice)
    print(result)
