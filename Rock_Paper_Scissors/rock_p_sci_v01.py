import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("--- Rock, Paper, Scissors ---")
    print("Type 'exit' to quit the game.")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors: ").strip().lower()

        if user_choice == "exit":
            print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in options:
            print("Invalid input! Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
