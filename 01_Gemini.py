import random
import time
import sys

# ANSI Color Codes for Terminal Styling
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Visual ASCII Art for Moves
ASCII_ART = {
    'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" ,
    'paper': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

WINNING_RULES = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

class RockPaperScissorsEngine:
    def __init__(self, mode='normal'):
        self.mode = mode
        self.user_history = []
        self.scores = {'user': 0, 'computer': 0, 'ties': 0}

    def get_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        
        # Hard Mode: Dynamic counter based on player frequency
        if self.mode == 'hard' and len(self.user_history) >= 2:
            most_frequent = max(set(self.user_history), key=self.user_history.count)
            counter_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
            # 70% chance to counter player's most frequent move, 30% random
            if random.random() < 0.7:
                return counter_moves[most_frequent]
        
        return random.choice(choices)

    def resolve_round(self, user_move, comp_move):
        self.user_history.append(user_move)
        if user_move == comp_move:
            self.scores['ties'] += 1
            return 'tie'
        elif WINNING_RULES[user_move] == comp_move:
            self.scores['user'] += 1
            return 'user'
        else:
            self.scores['computer'] += 1
            return 'computer'


def print_banner():
    print(f"{Colors.HEADER} {Colors.BOLD}")
    print("==========================================")
    print("   ROCK  •  PAPER  •  SCISSORS : ULTIMATE ")
    print("==========================================")
    print(f"{Colors.RESET}")


def select_difficulty():
    print("Select Difficulty Mode:")
    print(f"[{Colors.GREEN}1{Colors.RESET}] Normal (Pure Random Computer)")
    print(f"[{Colors.RED}2{Colors.RESET}] Hard (Adaptive AI counter-strategy)")
    choice = input("Enter choice (1/2): ").strip()
    return 'hard' if choice == '2' else 'normal'


def show_countdown():
    print()
    for word in ["ROCK...", "PAPER...", "SCISSORS...", "SHOOT!"]:
        print(f"{Colors.YELLOW}{Colors.BOLD}{word}{Colors.RESET}", end=" ", flush=True)
        time.sleep(0.35)
    print("\n")


def play_game():
    print_banner()
    mode = select_difficulty()
    engine = RockPaperScissorsEngine(mode=mode)
    
    print(f"\n{Colors.CYAN}Mode set to:: {mode.upper()}{Colors.RESET}")
    print("Type 'r' (rock), 'p' (paper), 's' (scissors), or 'q' to exit.\n")

    input_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    while True:
        raw_input = input(f"{Colors.BOLD}Your turn [r/p/s/q]: {Colors.RESET}").lower().strip()
        
        if raw_input == 'q':
            break
        
        if raw_input in input_map:
            user_choice = input_map[raw_input]
        elif raw_input in input_map.values():
            user_choice = raw_input
        else:
            print(f"{Colors.RED}Invalid input! Please enter 'r', 'p', 's', or 'q'.{Colors.RESET}\n")
            continue

        comp_choice = engine.get_computer_choice()
        show_countdown()

        # Display Moves Side by Side / Sequentially
        print(f"{Colors.BLUE}You played: {user_choice.upper()}{Colors.RESET}")
        print(ASCII_ART[user_choice])
        
        print(f"{Colors.RED}Computer played: {comp_choice.upper()}{Colors.RESET}")
        print(ASCII_ART[comp_choice])

        # Result Evaluation
        result = engine.resolve_round(user_choice, comp_choice)
        
        if result == 'tie':
            print(f"{Colors.YELLOW}{Colors.BOLD}>>> ROUND RESULT: IT'S A TIE! <<<{Colors.RESET}\n")
        elif result == 'user':
            print(f"{Colors.GREEN}{Colors.BOLD}>>> ROUND RESULT: YOU WIN! <<<{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}{Colors.BOLD}>>> ROUND RESULT: COMPUTER WINS! <<<{Colors.RESET}\n")

        # Scoreboard Display
        s = engine.scores
        print(f"{Colors.HEADER}---------------- SCOREBOARD ----------------{Colors.RESET}")
        print(f"  Player: {Colors.GREEN}{s['user']}{Colors.RESET} | Computer: {Colors.RED}{s['computer']}{Colors.RESET} | Ties: {Colors.YELLOW}{s['ties']}{Colors.RESET}")
        print(f"{Colors.HEADER}--------------------------------------------{Colors.RESET}\n")

    # Final Summary
    print(f"\n{Colors.BOLD}=== FINAL RESULTS ==={Colors.RESET}")
    print(f"Total Rounds Played: {len(engine.user_history)}")
    print(f"Final Score -> You: {engine.scores['user']} | Computer: {engine.scores['computer']} | Ties: {engine.scores['ties']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    play_game()