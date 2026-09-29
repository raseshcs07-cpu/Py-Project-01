# 
import random 

def show_banner():
    print("""
╔══════════════════════════════════════╗
║        🎯 ROC🪨PAPE📄SCISSO✂️         ║
║             ~RASESH                  ║
╚══════════════════════════════════════╝
""")

def get_user_choice():
       
       choices = {
             'r':'rock 🪨' , 
             'p':'paper 📄' , 
             's':'scissors ✂️' , 
             'q' : 'quit 👋'
             }
       
       while True:
             
           show_banner()

           user_input = input("Enter (r)ock , (p)aper , (s)cissors  (or 'q' to quit):").lower().strip()

           if user_input == 'q' :
                return 'quit'
                       
           if user_input in choices:
                return choices[user_input]
           
           if user_input in choices.values():
                return user_input
           
           print("Invald Choice! Please enter r , p , s or q")


def determine_winner(user,computer):

        if user == computer :
              return 'tie ⧓'
        if user == 'rock 🪨' and computer == 'scissors ✂️' :
              return 'win 🏆'
        if user == 'paper 📄' and computer == 'rock 🪨':
              return 'win 🏆'
        if user == 'scissors ✂️' and computer == 'paper 📄':
              return 'win 🏆'
        else :
              return 'lose ⧒\n'


user_score = 0
computer_score = 0
ties = 0


while True :
      
    user_choice = get_user_choice()

    if user_choice == 'quit':
           break
    
    
    computer_choice = ['rock 🪨', 'paper 📄', 'scissors ✂️']
    computer_choose = random.choice(computer_choice)
    
    print("\nYou chose »»", user_choice)
    print("Computer chose »»", computer_choose,"\n")
    
    
    result = determine_winner(user_choice, computer_choose)
    print(result)

    if result == 'win 🏆':
       user_score += 1

    if result == 'lose ⧒':
       computer_score += 1

    if result == 'tie ⧓':
       ties += 1

    else :
         computer_score +=1

    print("\n««========= Final Score ===========»»")
    print(f"Score »» You: {user_score} | Computer: {computer_score } | Ties: {ties}")