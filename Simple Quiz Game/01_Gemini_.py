import json
import os
import random
import sys
import time

# Optional cross-platform key press import for timed input
try:
    import msvcrt  # Windows
except ImportError:
    import select  # Unix/Linux/macOS


def input_with_timeout(prompt, timeout=15):
    """Gets user input with a countdown timer."""
    print(prompt, end="", flush=True)
    start_time = time.time()
    input_chars = []

    # Check platform for timed input
    if "msvcrt" in sys.modules:
        while time.time() - start_time < timeout:
            if msvcrt.kbhit():
                char = msvcrt.getwche()
                if char in ("\r", "\n"):
                    print()
                    return "".join(input_chars).strip()
                elif char == "\b":  # Backspace
                    if input_chars:
                        input_chars.pop()
                        sys.stdout.write(" \b")
                        sys.stdout.flush()
                else:
                    input_chars.append(char)
            time.sleep(0.05)
    else:
        # Unix implementation
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().strip()

    print("\n⏰ Time's up!")
    return None


class QuizGame:

    def __init__(self):
        self.score = 0
        self.streak = 0
        self.lifelines = {"50/50": True, "Hint": True}
        self.questions = self.load_default_questions()
        self.leaderboard_file = "leaderboard.json"

    def load_default_questions(self):
        """Loads extended question pool with categories and difficulty levels."""
        return [
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": [
                    "A) Gold",
                    "B) Oxygen",
                    "C) Osmium",
                    "D) Hydrogen",
                ],
                "answer": "B",
                "difficulty": "Easy",
                "points": 100,
                "hint": "It is essential for human breathing.",
            },
            {
                "question": "How many states make up the United States?",
                "options": ["A) 48", "B) 50", "C) 52", "D) 46"],
                "answer": "B",
                "difficulty": "Easy",
                "points": 100,
                "hint": "Half a century.",
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": [
                    "A) Elephant",
                    "B) Blue Whale",
                    "C) Giraffe",
                    "D) Colossal Squid",
                ],
                "answer": "B",
                "difficulty": "Easy",
                "points": 100,
                "hint": "It lives in the ocean.",
            },
            {
                "question": "In what year did the Apollo 11 moon landing occur?",
                "options": ["A) 1965", "B) 1969", "C) 1971", "D) 1975"],
                "answer": "B",
                "difficulty": "Medium",
                "points": 200,
                "hint": "Late 1960s, same year as Woodstock.",
            },
            {
                "question": "Which programming language is known as the language of the web?",
                "options": [
                    "A) Python",
                    "B) C++",
                    "C) JavaScript",
                    "D) Java",
                ],
                "answer": "C",
                "difficulty": "Medium",
                "points": 200,
                "hint": "Runs inside browsers natively.",
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": [
                    "A) Gold",
                    "B) Diamond",
                    "C) Titanium",
                    "D) Quartz",
                ],
                "answer": "B",
                "difficulty": "Medium",
                "points": 200,
                "hint": "Made purely of carbon under high pressure.",
            },
            {
                "question": "What is the velocity of light in a vacuum (approximate)?",
                "options": [
                    "A) 300,000 km/s",
                    "B) 150,000 km/s",
                    "C) 1,000,000 km/s",
                    "D) 30,000 km/s",
                ],
                "answer": "A",
                "difficulty": "Hard",
                "points": 300,
                "hint": "3 x 10^8 meters per second.",
            },
            {
                "question": "Which country invented the paper currency?",
                "options": [
                    "A) Greece",
                    "B) China",
                    "C) Egypt",
                    "D) Italy",
                ],
                "answer": "B",
                "difficulty": "Hard",
                "points": 300,
                "hint": "During the Tang Dynasty.",
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
                "answer": "C",
                "difficulty": "Medium",
                "points": 200,
                "hint": "It is the only even prime number.",
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": [
                    "A) Vincent van Gogh",
                    "B) Leonardo da Vinci",
                    "C) Pablo Picasso",
                    "D) Michelangelo",
                ],
                "answer": "B",
                "difficulty": "Easy",
                "points": 100,
                "hint": "Italian Renaissance polymath.",
            },
        ]

    def use_50_50(self, question, current_options):
        """Removes two incorrect answers."""
        if not self.lifelines["50/50"]:
            print("\n❌ You have already used your 50/50 lifeline!")
            return current_options

        correct_key = question["answer"]
        incorrect = [
            opt
            for opt in current_options
            if not opt.startswith(correct_key)
        ]
        removed = random.sample(incorrect, 2)
        filtered_options = [
            opt for opt in current_options if opt not in removed
        ]

        self.lifelines["50/50"] = False
        print("\n✨ 50/50 Lifeline Activated! Two incorrect options removed.")
        return filtered_options

    def use_hint(self, question):
        """Displays a hint for the current question."""
        if not self.lifelines["Hint"]:
            print("\n❌ You have already used your Hint lifeline!")
            return

        self.lifelines["Hint"] = False
        print(f"\n💡 HINT: {question['hint']}")

    def display_header(self, q_num, total_q, question):
        """Displays formatted HUD per question."""
        print("\n" + "=" * 50)
        print(
            f"Question {q_num}/{total_q} | Difficulty: {question['difficulty']} | Score: {self.score}"
        )
        print(f"Streak Bonus: {self.streak}x")
        lifeline_status = [
            k for k, v in self.lifelines.items() if v
        ]
        print(
            f"Available Lifelines: {', '.join(lifeline_status) if lifeline_status else 'None'}"
        )
        print("=" * 50)

    def save_high_score(self, player_name):
        """Saves current score to a local JSON file."""
        leaderboard = []
        if os.path.exists(self.leaderboard_file):
            try:
                with open(self.leaderboard_file, "r") as f:
                    leaderboard = json.load(f)
            except json.JSONDecodeError:
                leaderboard = []

        leaderboard.append({"name": player_name, "score": self.score})
        leaderboard = sorted(
            leaderboard, key=lambda x: x["score"], reverse=True
        )[:5]

        with open(self.leaderboard_file, "w") as f:
            json.dump(leaderboard, f, indent=4)

    def display_leaderboard(self):
        """Displays top scores."""
        if not os.path.exists(self.leaderboard_file):
            return

        print("\n🏆 TOP 5 HIGH SCORES 🏆")
        print("-" * 30)
        try:
            with open(self.leaderboard_file, "r") as f:
                scores = json.load(f)
                for rank, entry in enumerate(scores, 1):
                    print(
                        f"{rank}. {entry['name']:<15} - {entry['score']} pts"
                    )
        except Exception:
            print("No high scores recorded yet.")
        print("-" * 30)

    def play(self):
        print("==========================================")
        print("   🌟 ULTIMATE PYTHON QUIZ SHOW 🌟   ")
        print("==========================================")
        player_name = (
            input("Enter your player name: ").strip() or "Player 1"
        )

        random.shuffle(self.questions)
        total_questions = len(self.questions)

        for i, q in enumerate(self.questions, start=1):
            current_options = list(q["options"])

            while True:
                self.display_header(i, total_questions, q)
                print(f"\n{q['question']}\n")
                for opt in current_options:
                    print(f"  {opt}")

                print("\nCommands: Answer [A/B/C/D] | [1] 50/50 | [2] Hint")

                # 15 second timer per question
                user_input = input_with_timeout(
                    "\nYour choice (15s limit): ", timeout=15
                )

                if user_input is None:
                    print(f"\n❌ Correct answer was: {q['answer']}")
                    self.streak = 0
                    break

                user_input = user_input.upper()

                # Lifeline handlers
                if user_input == "1":
                    current_options = self.use_50_50(q, current_options)
                    time.sleep(1)
                    continue
                elif user_input == "2":
                    self.use_hint(q)
                    time.sleep(1)
                    continue

                valid_keys = [opt[0] for opt in current_options]
                if user_input in valid_keys:
                    if user_input == q["answer"]:
                        # Points calculation with streak multiplier
                        base_pts = q["points"]
                        multiplier = 1 + (self.streak * 0.2)
                        pts_earned = int(base_pts * multiplier)
                        self.score += pts_earned
                        self.streak += 1
                        print(
                            f"\n✅ CORRECT! Earned {pts_earned} points (Streak: {self.streak}x)!"
                        )
                    else:
                        print(
                            f"\n❌ INCORRECT! The right answer was {q['answer']}."
                        )
                        self.streak = 0
                    break
                else:
                    print("\n⚠️ Invalid option. Choose from available choices.")
                    time.sleep(1)

            time.sleep(1.5)

        print("\n==========================================")
        print(f"🎉 GAME OVER, {player_name.upper()}!")
        print(f"Final Score: {self.score} points")
        print("==========================================")

        self.save_high_score(player_name)
        self.display_leaderboard()




if __name__ == "__main__":
    game = QuizGame()
    game.play()