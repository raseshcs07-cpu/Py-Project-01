import random

def get_user_choice():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    while True:
        user_input = input("Enter (r)ock, (p)aper, or (s)cissors (or 'q' to quit): ").lower().strip()
        if user_input == 'q':
            return 'quit'
        if user_input in choices:
            return choices[user_input]
        if user_input in choices.values():
            return user_input
        print("Invalid choice. Please enter r, p, s, or q.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    
    winning_combos = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combos[user] == computer:
        return "user"
    return "computer"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    scores = {'user': 0, 'computer': 0, 'ties': 0}

    print("==== Rock, Paper, Scissors ===")
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break
            
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("Result: It's a tie!")
            scores['ties'] += 1
        elif winner == "user":
            print("Result: You win this round!")
            scores['user'] += 1
        else:
            print("Result: Computer wins this round!")
            scores['computer'] += 1
            
        print(f"Score -> You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['ties']}\n")
        
    print("\n=== Final Score ===")
    print(f"You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()