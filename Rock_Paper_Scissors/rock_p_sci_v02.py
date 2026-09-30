import time 
import random 
import os 
import sys


# ==================== ASCII ART ====================

ASCII_ART = {
    'rock 🪨': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" ,
    'paper 📄': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    'scissors ✂️': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# ==================== COUNTDOWN ====================

def show_countdown():
     for word in ["Rock...","Paper..." , "Scissor...","Shoot🎯"]:
          print(word,end=" ",flush=True)
          time.sleep(0.25)
     print()

# ==================== CLEAR SCREEN ====================

def clear_screen():
     os.system("cls" if os.name == "nt" else "clear")

# ==================== SOUNDS ====================

def win_sound():
     os.system("afplay /System/Library/Sounds/Glass.aiff")
     sys.stdout.write('\a')
     sys.stdout.flush()

def lose_sound():
     os.system("afplay /System/Library/Sounds/Basso.aiff")

def tie_sound():
     os.system("afplay /System/Library/Sounds/Basso.aiff &")

# ==================== BANNER ====================

def show_banner(round_number):
       print(f"""
╔══════════════════════════════════════╗
║        🎯 ROC🪨PAPE📄SCISSO✂️         ║
║             ~RASESH                  ║
║          MODE : Normal              ║
║         »» ROUND {round_number}                    ║
╚══════════════════════════════════════╝
""")
       
# ==================== USER CHOICE ====================

def get_user_choice():


       choices = {
             'r':'rock 🪨' , 
             'p':'paper 📄' , 
             's':'scissors ✂️' , 
             'q' : 'quit 👋'
             }
       
       while True:
           clear_screen()
           show_banner(round_number)

           user_input = input("\nEnter (r)ock , (p)aper , (s)cissors  (or 'q' to quit):").lower().strip()

           if user_input == 'q' :
                return 'quit'
                       
           if user_input in choices:
                return choices[user_input]
           
           if user_input in choices.values():
                return user_input
           
           print("Invald Choice! Please enter r , p , s or q")

# ==================== WINNER ====================

def determine_winner(user,computer):

        if user == computer :
              return 'tie ⧓'
        if user == 'rock 🪨' and computer == 'scissors ✂️' :
              return 'win 🏆'
        if user == 'paper 📄' and computer == 'rock 🪨':
              return 'win 🏆'
        if user == 'scissors ✂️' and computer == 'paper 📄':
              return 'win 🏆'
        else:
              return 'lose ⧒'

# ==================== SCORE ====================

user_score = 0
computer_score = 0
ties = 0

win_streak = 0
best_streak = 0
# target_score = 3

# ==================== MAIN GAME ====================

round_number = 1 
game_id = random.randint(1000, 9999)

while True :

    clear_screen()

    user_choice = get_user_choice()

    if user_choice == 'quit':
           print("\nExiting game... 🫡")
           break
    
    computer_choice = ['rock 🪨', 'paper 📄', 'scissors ✂️']
    computer_choose = random.choice(computer_choice)

    show_countdown()

    print("\nYou chose »»", user_choice)
    print(ASCII_ART[user_choice])

    print("\n","-"*50,"\n")

    print("Computer chose »»", computer_choose, "\n")
    print(ASCII_ART[computer_choose])


    print("\n","-"*50,"\n")    
    result = determine_winner(user_choice, computer_choose)
    print("\n╔════════════════════════════════╗")
    print(f"║          {result}              ║")
    print("╚════════════════════════════════╝")

    if result == 'win 🏆':
       user_score += 1
       win_streak += 1

       if win_streak > best_streak:
            best_streak = win_streak

       print("\nDisplaying Score.....")
       win_sound()

    if result == 'lose ⧒':
       computer_score += 1
       win_streak = 0

       print("\nDisplaying Score.....")
       lose_sound()

    if result == 'tie ⧓':
       ties += 1
       print("\nDisplaying Score.....")
       tie_sound()

    print("\n╔══════════════════════════════════════╗")
    print("║              SCOREBOARD📊           ║")
    print(f"║     🎮 Game ID: {game_id}                 ║")
    # print("║                                      ║")
    print(f"║     You: {user_score}   Computer: {computer_score}   Ties: {ties}  ║")
    print(f"║     🔥 Win Streak: {win_streak}                 ║")
    print(f"║     🔥 Best Streak: {best_streak}              ║")
    print("╚══════════════════════════════════════╝")

#     if user_score == target_score or computer_score == target_score:
#          print("\n🏁 Target score reached!")
#          break

    quit_game = False
    while True:

     continue_game = input(
        "\nPress Enter to continue playing | Q to quit: ").lower().strip()

     if continue_game == "":
        round_number += 1
        break

     elif continue_game == "q":
         print("\nExiting game... 🫡")
         quit_game = True
         break

     else:
        print("\nInvalid choice! Press Enter to continue or Q to quit.")

    if quit_game:
      break



print("\n╔══════════════════════════════════════╗")
print("║         THANKS FOR PLAYING! 🎮      ║")
print("║                                      ║")

if user_score > computer_score:
    print("║          YOU WON! 🏆                ║")
elif computer_score > user_score:
    print("║       COMPUTER WON! 🤖              ║")
else:
    print("║          IT'S A TIE! 🤝             ║")

print("║                                      ║")
print(f"║     You: {user_score}   Computer: {computer_score}   Ties: {ties}  ║")
print("║                                      ║")
print("║          See you next time! 👋       ║")
print("╚══════════════════════════════════════╝")

input("\nPress Enter to exit...")