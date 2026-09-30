"""v1

                    ┌───────────────┐
                    │     START     │
                    └───────┬───────┘
                            ↓
                    ┌────────────────┐
                    │ import random  │
                    └───────┬────────┘
                            ↓
              ┌──────────────────────────┐
              │ Initialize Scores        │
              │ User = 0                 │
              │ Computer = 0             │
              │ Ties = 0                 │
              └────────────┬─────────────┘
                           ↓
                    ┌──────────────┐
                    │  while True  │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │ show_banner()│
                    └──────┬───────┘
                           ↓
              ┌──────────────────────────┐
              │   Get User Choice        │
              │   r / p / s / q           │
              └────────────┬─────────────┘
                           ↓
                 ┌──────────────────┐
                 │ Is input valid?  │
                 └───────┬─────┬────┘
                       NO│     │YES
                         ↓     ↓
              ┌──────────────┐ │
              │ Invalid      │ │
              │ Choice       │ │
              └──────┬───────┘ │
                     │          │
                     └────↩─────┘
                                ↓
                       ┌────────────────┐
                       │ Is choice 'q'? │
                       └───────┬────┬───┘
                             YES│    │NO
                                ↓    ↓
                       ┌──────────┐  ┌────────────────────┐
                       │  break   │  │ Computer Choices   │
                       └────┬─────┘  │ rock/paper/scissor│
                            │        └─────────┬──────────┘
                            │                  ↓
                            │        ┌────────────────────┐
                            │        │ random.choice()    │
                            │        │ → Computer Choice │
                            │        └─────────┬──────────┘
                            │                  ↓
                            │        ┌────────────────────┐
                            │        │ Display Choices    │
                            │        └─────────┬──────────┘
                            │                  ↓
                            │        ┌────────────────────┐
                            │        │ determine_winner() │
                            │        └─────────┬──────────┘
                            │                  ↓
                            │        ┌────────────────────┐
                            │        │      Result?       │
                            │        └──────┬───┬───┬─────┘
                            │             WIN LOSE TIE
                            │              ↓    ↓    ↓
                            │        ┌─────┐ ┌─────┐ ┌─────┐
                            │        │User │ │Comp │ │Ties │
                            │        │ +1  │ │ +1  │ │ +1  │
                            │        └──┬──┘ └──┬──┘ └──┬──┘
                            │           └────┬──┴───┬───┘
                            │                ↓
                            │        ┌────────────────────┐
                            │        │ Display Score      │
                            │        └─────────┬──────────┘
                            │                  ↓
                            │             ↩ Next Round
                            │                  │
                            └──────────────────┘
                            
                            ↓
                   ┌─────────────────────┐
                   │    FINAL SCORE      │
                   │ User / Computer /  │
                   │ Ties                │
                   └──────────┬──────────┘
                              ↓
                       ┌─────────────┐
                       │     END     │
                       └─────────────┘
"""


"""v2

                    ┌─────────────────────┐
                    │        START        │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌──────────────────────────────┐
              │ Import required modules      │
              │ random, time, os, sys        │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │ Define ASCII ART             │
              │ Rock / Paper / Scissors      │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │ Define game functions        │
              │ • clear_screen()             │
              │ • show_countdown()           │
              │ • sound functions             │
              │ • show_banner()              │
              │ • get_user_choice()          │
              │ • determine_winner()         │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │ Initialize variables         │
              │                              │
              │ user_score = 0               │
              │ computer_score = 0           │
              │ ties = 0                     │
              │ win_streak = 0               │
              │ best_streak = 0              │
              │ round_number = 1             │
              │ quit_game = False            │
              └──────────────┬───────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   START ROUND   │
                    └────────┬────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Clear Screen         │
                  │ Show Banner          │
                  │ Show Round Number    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Ask Player for       │
                  │ Rock / Paper /       │
                  │ Scissors / Quit      │
                  └──────────┬───────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Player chose Q? │
                    └───────┬─────┬───┘
                            │Yes  │No
                            ▼     ▼
                 ┌────────────┐   ┌───────────────────┐
                 │ Quit Game  │   │ Computer chooses  │
                 └─────┬──────┘   │ random move       │
                       │          └─────────┬─────────┘
                       │                    │
                       │                    ▼
                       │          ┌───────────────────┐
                       │          │ Countdown         │
                       │          │ Rock... Paper...  │
                       │          │ Scissors...Shoot  │
                       │          └─────────┬─────────┘
                       │                    │
                       │                    ▼
                       │          ┌───────────────────┐
                       │          │ Display Player    │
                       │          │ Move + ASCII Art  │
                       │          └─────────┬─────────┘
                       │                    │
                       │                    ▼
                       │          ┌───────────────────┐
                       │          │ Display Computer  │
                       │          │ Move + ASCII Art  │
                       │          └─────────┬─────────┘
                       │                    │
                       │                    ▼
                       │          ┌───────────────────┐
                       │          │ Determine Winner  │
                       │          └─────────┬─────────┘
                       │                    │
                       │                    ▼
                       │             ┌──────────────┐
                       │             │ Result?      │
                       │             └───┬──┬───┬───┘
                       │                 │  │   │
                       │               WIN LOSE TIE
                       │                 │  │   │
                       │                 ▼  ▼   ▼
                       │              ┌────┐┌────┐┌────┐
                       │              │+1  ││+1  ││+1  │
                       │              │User││Comp││Tie │
                       │              └─┬──┘└─┬──┘└─┬──┘
                       │                │     │      │
                       │                ▼     ▼      ▼
                       │          ┌─────────────────────┐
                       │          │ Update Win Streak   │
                       │          │                     │
                       │          │ WIN → streak +1     │
                       │          │ LOSE → streak = 0   │
                       │          │ TIE → unchanged     │
                       │          └──────────┬──────────┘
                       │                     │
                       │                     ▼
                       │          ┌─────────────────────┐
                       │          │ Update Best Streak  │
                       │          │                     │
                       │          │ If current streak   │
                       │          │ > best streak       │
                       │          │ → update best       │
                       │          └──────────┬──────────┘
                       │                     │
                       │                     ▼
                       │          ┌─────────────────────┐
                       │          │ Display Result      │
                       │          │ + Scoreboard        │
                       │          └──────────┬──────────┘
                       │                     │
                       │                     ▼
                       │          ┌─────────────────────┐
                       │          │ Continue playing?   │
                       │          └──────────┬──────────┘
                       │                     │
                       │              ┌──────┴──────┐
                       │              │             │
                       │           ENTER           Q
                       │              │             │
                       │              ▼             ▼
                       │      ┌──────────────┐  ┌────────────┐
                       │      │ round_number │  │ quit_game  │
                       │      │    += 1      │  │   = True   │
                       │      └──────┬───────┘  └─────┬──────┘
                       │             │                │
                       │             │                ▼
                       │             │         ┌─────────────┐
                       │             │         │ Exit Loop   │
                       │             │         └──────┬──────┘
                       │             │                │
                       │             ▼                │
                       │      ┌──────────────┐        │
                       │      │ Start Next   │        │
                       │      │ Round        │        │
                       │      └──────┬───────┘        │
                       │             │                │
                       │             └───────┐        │
                       │                     │        │
                       │                     ▼        │
                       │              ┌────────────┐  │
                       │              │   LOOP     │  │
                       │              │ Next Round │  │
                       │              └────────────┘  │
                       │                              │
                       └──────────────┬───────────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │     FINAL SCREEN       │
                         │                        │
                         │ Final Scores           │
                         │ Winner                 │
                         │ Total Ties             │
                         │ Best Win Streak        │
                         │                        │
                         │ "See you next time!"   │
                         └────────────┬───────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │   Press Enter to Exit  │
                         └────────────┬───────────┘
                                      │
                                      ▼
                              ┌──────────────┐
                              │     END      │
                              └──────────────┘




                              


                USER WINS
                    │
                    ▼
             win_streak += 1
                    │
                    ▼
        Is win_streak > best_streak?
              /              \
            YES               NO
             │                 │
             ▼                 │
      best_streak =            │
        win_streak             │
             │                 │
             └────────┬────────┘
                      ▼
                 Continue Game

"""

"""
Add Win Percentage 📊
total_rounds = user_score + computer_score + ties
win_percentage = (user_score / total_rounds) * 100

Add Accuracy / Stats Section 📊

Add Game Duration ⏱️
start_time = time.time()
game_duration = round(time.time() - start_time, 2)

Add a Game ID 🎮
game_id = random.randint(1000, 9999)
print(f"║     🎮 Game ID: {game_id}                 ║")

Add a Player Name 👤
player_name = input("Enter your name: ").strip()
if player_name == "":
    player_name = "Player"
print(f"║       {player_name} WON! 🏆             ║")
print(f"║     {player_name}: {user_score}   Computer: {computer_score}   Ties: {ties}  ║")

Add a Personalized Welcome Message 👋

Add a Game Mode Selection 🎯
while True:
    game_mode = input(
        "\nSelect Game Mode:\n"
        "1. Normal 🎯\n"
        "2. Hard 🤖\n"
        "Enter 1 or 2: "
    ).strip()

    if game_mode == "1":
        game_mode = "Normal"
        break
    elif game_mode == "2":
        game_mode = "Hard"
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")

Make Hard Mode Actually Different 🤖
if game_mode == "Normal":
    computer_choose = random.choice(computer_choice)

elif game_mode == "Hard":
    if user_choice == "rock 🪨":
        computer_choose = random.choice(["paper 📄", "scissors ✂️"])

    elif user_choice == "paper 📄":
        computer_choose = random.choice(["scissors ✂️", "rock 🪨"])

    elif user_choice == "scissors ✂️":
        computer_choose = random.choice(["rock 🪨", "paper 📄"])

Show the Selected Mode in the Welcome Message 🎯

Add a Mode-Based Target Score 🎯
if user_score == target_score or computer_score == target_score:

Show Target Score in the Welcome Message 🎯
🎮 Welcome, Alex!
🔥 Hard Mode selected!
🎯 First to 5 wins!


"""