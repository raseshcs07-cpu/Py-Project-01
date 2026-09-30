import time


def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "C",
        },
        {
            "question": "What is the primary gas found in Earth's atmosphere?",
            "options": [
                "A) Oxygen",
                "B) Carbon Dioxide",
                "C) Nitrogen",
                "D) Hydrogen",
            ],
            "answer": "C",
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "answer": "C",
        },
    ]

    score = 0
    total = len(questions)

    print("========================================")
    print("      WELCOME TO THE PYTHON QUIZ!      ")
    print("========================================\n")
    time.sleep(1)

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        # Get and validate user input
        user_answer = ""
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = (
                input("\nYour answer (A, B, C, or D): ").strip().upper()
            )
            if user_answer not in ["A", "B", "C", "D"]:
                print("Invalid input. Please choose A, B, C, or D.")

        # Check answer
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.\n")

        print("-" * 40)
        time.sleep(0.5)

    # Final Score
    percentage = (score / total) * 100
    print("\n========================================")
    print("             GAME OVER!                 ")
    print(f" Your final score: {score}/{total} ({percentage:.0f}%)")
    print("========================================\n")


if __name__ == "__main__":
    run_quiz()