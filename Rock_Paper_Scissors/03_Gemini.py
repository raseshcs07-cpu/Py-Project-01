import random
import tkinter as tk
from tkinter import ttk, messagebox

# Visual ASCII Art for Moves
ASCII_ART = {
    'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
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
        if self.mode == 'hard' and len(self.user_history) >= 2:
            most_frequent = max(set(self.user_history), key=self.user_history.count)
            counter_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
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

    def reset_game(self):
        self.user_history.clear()
        self.scores = {'user': 0, 'computer': 0, 'ties': 0}


class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors : Ultimate")
        self.geometry("800x650")
        self.configure(bg="#1e1e2e")

        self.engine = RockPaperScissorsEngine(mode='normal')

        self.setup_ui()

    def setup_ui(self):
        # Header Title
        title_label = tk.Label(
            self, text="ROCK • PAPER • SCISSORS", 
            font=("Consolas", 20, "bold"), fg="#cba6f7", bg="#1e1e2e"
        )
        title_label.pack(pady=10)

        # Mode Selection Frame
        mode_frame = tk.Frame(self, bg="#1e1e2e")
        mode_frame.pack(pady=5)

        tk.Label(
            mode_frame, text="Difficulty Mode:", 
            font=("Consolas", 12), fg="#cdd6f4", bg="#1e1e2e"
        ).pack(side=tk.LEFT, padx=5)

        self.mode_var = tk.StringVar(value="normal")
        normal_radio = tk.Radiobutton(
            mode_frame, text="Normal", variable=self.mode_var, value="normal",
            font=("Consolas", 11), fg="#a6e3a1", bg="#1e1e2e", selectcolor="#313244",
            activebackground="#1e1e2e", activeforeground="#a6e3a1", command=self.change_mode
        )
        normal_radio.pack(side=tk.LEFT, padx=10)

        hard_radio = tk.Radiobutton(
            mode_frame, text="Hard (Adaptive AI)", variable=self.mode_var, value="hard",
            font=("Consolas", 11), fg="#f38ba8", bg="#1e1e2e", selectcolor="#313244",
            activebackground="#1e1e2e", activeforeground="#f38ba8", command=self.change_mode
        )
        hard_radio.pack(side=tk.LEFT, padx=10)

        # Scoreboard Frame
        score_frame = tk.Frame(self, bg="#313244", bd=2, relief=tk.RIDGE)
        score_frame.pack(fill=tk.X, padx=20, pady=10)

        self.lbl_score_user = tk.Label(score_frame, text="Player: 0", font=("Consolas", 14, "bold"), fg="#a6e3a1", bg="#313244")
        self.lbl_score_user.pack(side=tk.LEFT, expand=True, pady=10)

        self.lbl_score_ties = tk.Label(score_frame, text="Ties: 0", font=("Consolas", 14, "bold"), fg="#f9e2af", bg="#313244")
        self.lbl_score_ties.pack(side=tk.LEFT, expand=True, pady=10)

        self.lbl_score_comp = tk.Label(score_frame, text="Computer: 0", font=("Consolas", 14, "bold"), fg="#f38ba8", bg="#313244")
        self.lbl_score_comp.pack(side=tk.LEFT, expand=True, pady=10)

        # Display Frame for ASCII Art
        art_frame = tk.Frame(self, bg="#1e1e2e")
        art_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        # User Move Box
        user_box = tk.LabelFrame(art_frame, text=" YOUR MOVE ", font=("Consolas", 11, "bold"), fg="#89b4fa", bg="#1e1e2e")
        user_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.lbl_user_art = tk.Label(user_box, text="\n\nSelect a move\nto play", font=("Courier", 10), fg="#cdd6f4", bg="#181825", justify=tk.LEFT)
        self.lbl_user_art.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Computer Move Box
        comp_box = tk.LabelFrame(art_frame, text=" COMPUTER MOVE ", font=("Consolas", 11, "bold"), fg="#f38ba8", bg="#1e1e2e")
        comp_box.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

        self.lbl_comp_art = tk.Label(comp_box, text="\n\nWaiting...", font=("Courier", 10), fg="#cdd6f4", bg="#181825", justify=tk.LEFT)
        self.lbl_comp_art.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Round Result Display Banner
        self.lbl_result = tk.Label(
            self, text="Choose Rock, Paper, or Scissors to Start!", 
            font=("Consolas", 13, "bold"), fg="#89dceb", bg="#1e1e2e"
        )
        self.lbl_result.pack(pady=10)

        # Control / Move Buttons
        btn_frame = tk.Frame(self, bg="#1e1e2e")
        btn_frame.pack(pady=10)

        self.btn_rock = tk.Button(
            btn_frame, text="🪨 ROCK", font=("Consolas", 12, "bold"), bg="#45475a", fg="#ffffff",
            width=12, height=2, command=lambda: self.play_round('rock')
        )
        self.btn_rock.pack(side=tk.LEFT, padx=10)

        self.btn_paper = tk.Button(
            btn_frame, text="📄 PAPER", font=("Consolas", 12, "bold"), bg="#45475a", fg="#ffffff",
            width=12, height=2, command=lambda: self.play_round('paper')
        )
        self.btn_paper.pack(side=tk.LEFT, padx=10)

        self.btn_scissors = tk.Button(
            btn_frame, text="✂️ SCISSORS", font=("Consolas", 12, "bold"), bg="#45475a", fg="#ffffff",
            width=12, height=2, command=lambda: self.play_round('scissors')
        )
        self.btn_scissors.pack(side=tk.LEFT, padx=10)

        # Bottom Bar Buttons (Reset / Quit)
        bottom_frame = tk.Frame(self, bg="#1e1e2e")
        bottom_frame.pack(fill=tk.X, padx=20, pady=10)

        btn_reset = tk.Button(bottom_frame, text="Reset Game", font=("Consolas", 10), bg="#fab387", fg="#11111b", command=self.reset_game)
        btn_reset.pack(side=tk.LEFT)

        btn_quit = tk.Button(bottom_frame, text="Quit Game", font=("Consolas", 10), bg="#f38ba8", fg="#11111b", command=self.quit_game)
        btn_quit.pack(side=tk.RIGHT)

    def change_mode(self):
        self.engine.mode = self.mode_var.get()

    def play_round(self, user_choice):
        comp_choice = self.engine.get_computer_choice()
        
        # Display moves and ASCII art
        self.lbl_user_art.config(text=f"Choice: {user_choice.upper()}\n" + ASCII_ART[user_choice])
        self.lbl_comp_art.config(text=f"Choice: {comp_choice.upper()}\n" + ASCII_ART[comp_choice])

        # Resolve round
        result = self.engine.resolve_round(user_choice, comp_choice)

        # Update Result text & colors
        if result == 'tie':
            self.lbl_result.config(text=">>> ROUND RESULT: IT'S A TIE! <<<", fg="#f9e2af")
        elif result == 'user':
            self.lbl_result.config(text=">>> ROUND RESULT: YOU WIN! <<<", fg="#a6e3a1")
        else:
            self.lbl_result.config(text=">>> ROUND RESULT: COMPUTER WINS! <<<", fg="#f38ba8")

        # Update Scoreboard
        s = self.engine.scores
        self.lbl_score_user.config(text=f"Player: {s['user']}")
        self.lbl_score_ties.config(text=f"Ties: {s['ties']}")
        self.lbl_score_comp.config(text=f"Computer: {s['computer']}")

    def reset_game(self):
        self.engine.reset_game()
        self.lbl_score_user.config(text="Player: 0")
        self.lbl_score_ties.config(text="Ties: 0")
        self.lbl_score_comp.config(text="Computer: 0")
        self.lbl_user_art.config(text="\n\nSelect a move\nto play")
        self.lbl_comp_art.config(text="\n\nWaiting...")
        self.lbl_result.config(text="Game Reset. Choose a move!", fg="#89dceb")

    def quit_game(self):
        total_rounds = len(self.engine.user_history)
        s = self.engine.scores
        summary = (
            f"Total Rounds Played: {total_rounds}\n\n"
            f"Player Wins: {s['user']}\n"
            f"Computer Wins: {s['computer']}\n"
            f"Ties: {s['ties']}\n\n"
            "Thanks for playing!"
        )
        messagebox.showinfo("Final Results", summary)
        self.destroy()


if __name__ == "__main__":
    app = RPSApp()
    app.mainloop()