import time
import random
import os 
import sys

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear" )

def play_sound():
   os.system("afplay /System/Library/Sounds/Glass.aiff")
   sys.stdout.write('\a')
   sys.stdout.flush()

def show_banner():
    print("""
╔══════════════════════════════════════╗
║        🎯 NUMBER GUESSING GAME       ║
║             ~RASESH                  ║
╚══════════════════════════════════════╝
""")

def play_game():

   show_banner()
   clear_screen()
   score = 0

   print("\n\nSelect your Difficulty! ◎\n")
   print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
   print("1.Easy     (1-250, 10 attempts) ♝ ")
   print("2.Medium   (1-500, 7 attempts) ♔")
   print("3.Hard     (1-500, 5 attempts) ♛")
   print("4.Extreme  (1-200, 3 attempts) ♠︎")
   print("5.Exit   »»«« ")
   print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
   choice = input("Enter your choice! (1-5) :")
   
   if choice == "1":
      min_val = 1
      max_val = 250
      max_attempts = 10
      print("You selected Easy Mode! ♝")
   
   elif choice == "2":
      min_val = 1
      max_val = 500
      max_attempts = 7
      print("You selected Medium Mode! ♔")
   
   elif choice == "3":
      min_val = 1
      max_val = 500
      max_attempts = 5
      print("You selected Hard Mode! ♛")
   
   elif choice == "4":
      min_val = 1
      max_val = 200
      max_attempts = 3
      print("You selected Extreme Mode! ♠︎")
   
   elif choice == "5":
      print("\nContinue! Later on.👋 \n Thank You! ✨\n")
      exit()
   
   else:
      print("Invalid Key! Nightmare🛐 Mode Activated ⚓.")
      min_val = 1
      max_val = 1000
      max_attempts = 3
   
   
   secret_number = random.randint(min_val, max_val)
   print("\n" + "━" * 45)
   print(f"🎯 Guess a number between {min_val} and {max_val}")
   print(f"❤️  Attempts available: {max_attempts}")
   print("━" * 45)
   # print(f"\n»Game started!🎮Guess a number between {min_val} and {max_val}.")
   
   
   attempts = 0
   guessed_numbers = []
   start_time = time.time()
   
   
   def is_prime(number):
      """Return True if number is prime, otherwise False."""
      if number < 2:
         return False
   
      for i in range(2 , int(number ** 0.5) +1 ):
         if number % i ==0:
          return False
   
      return True
   
   
   divisors = [3, 5, 7, 10]
   valid_divisors = [i for i in divisors if secret_number % i== 0]
   if valid_divisors:
      print(f"💡 Hint:: The target is divisible by {valid_divisors[0]}")
   
   
   while attempts < max_attempts:
   
       print(f"Previous Guesses« : {guessed_numbers if guessed_numbers else 'None'}  ")
   
       try:
           guess = int(input(f"\n🐾Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
       except ValueError:
           print("Invalid Input! Enter a Number between {min_val} to {max_val}!.")
           continue
   
       if guess < min_val or guess > max_val :
          print(f"Please enter a number between {min_val} to {max_val} !")
          continue
   
       if guess in guessed_numbers:
          print("You already guessed that number! Try again.")
          continue
   
       guessed_numbers.append(guess)
       
       attempts +=1
       
       if guess == secret_number:
          print("\nGame Over!🎯\n»»»Congratulations 🥂!\n")
          print("╔══════════════════════════════════════╗")
          print("║          🎉 YOU WON! 🎉              ║")
          print("╚══════════════════════════════════════╝")
          play_sound()

          elapsed_time = round(time.time() - start_time , 2)
          print(f"⏱️Time Taken: {elapsed_time} seconds\n")

          score = max(0 , 10000 - ((attempts*500) + int(elapsed_time*10)))
          print(f"🏆 Score: {score}")

          break
       
       elif guess > secret_number:
          print("→Too high !")
   
       else :
          print("→Too low!")
   
       difference = abs(secret_number - guess)
       span = max_val - min_val 
   
       parity = "EVEN" if secret_number % 2 == 0 else "ODD"
       prime_status = "PRIME!" if is_prime(secret_number) else "Not PRIME!"
   
   
       if difference <= span * 0.005:
        print("♨︎An inch away!\n")
   
       elif difference <= span * 0.015:
        print("🔥 BOILING HOT! You are extremely close!\n")
   
       elif difference <= span * 0.05:
        print("🌡️ WARM! You are Bit close.\n")
   
       else:
        print("❄️ COLD! You are far from the number.\n")
   
       print(f"💡 Hint : The Target number is »» {parity} and {prime_status}.\n")
   
   
   if attempts == max_attempts and guess != secret_number :
      elapsed_time = round(time.time() - start_time , 2)
   
      print(f"Game Over!👾 \n The number was {secret_number}")
      print(f"⏱️ime Taken: {elapsed_time} seconds")
      print(f"📊 Attempts Used: {attempts}/{max_attempts}")
      print("\n╔══════════════════════════════════════╗")
      print("  ║             💀 GAME OVER             ║")
      print("  ╚══════════════════════════════════════╝")

def main():

 while True:
   play_game()

   replay = input("\nPlay Again❓ (y/n):").strip().lower()
   
   if replay == "y":
      print("Starting a New Game .....")
      continue
   else :
      print("Goodbye! 🫡, \n Exiting.....")
      exit()

if __name__ == "__main__":
   main()