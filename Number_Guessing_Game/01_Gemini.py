
import os
import random
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(sound_type):
    try:
        if sound_type == "win":
            for _ in range(3):
                sys.stdout.write('\a')
                sys.stdout.flush()
                time.sleep(0.15)
        elif sound_type in ["hint", "lose"]:
            sys.stdout.write('\a')
            sys.stdout.flush()
    except Exception:
        pass

def generate_hint(secret, guess, min_val, max_val):
    play_sound("hint")
    parity = "EVEN" if secret % 2 == 0 else "ODD"
    divisors = [i for i in [3, 5, 7, 10] if secret % i == 0]
    div_str = f", divisible by {random.choice(divisors)}" if divisors else ""
    
    diff = abs(secret - guess)
    span = max_val - min_val
    if diff <= span * 0.05:
        temp = "BOILING HOT (within 5%)"
    elif diff <= span * 0.15:
        temp = "WARM (within 15%)"
    else:
        temp = "COLD"

    return f"Target is {parity}{div_str}. Closeness: {temp}."

def play_game():
    clear_screen()
    print("=============================================")
    print("    🎯 ULTIMATE NUMBER GUESSING GAME 🎯      ")
    print("=============================================\n")
    
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")
    
    choice = input("\nSelect difficulty (1-3) [default: 2]: ").strip() or "2"
    
    modes = {
        "1": ((1, 50), 10),
        "2": ((1, 100), 7),
        "3": ((1, 200), 5)
    }
    
    (min_val, max_val), max_attempts = modes.get(choice, ((1, 100), 7))
    secret_number = random.randint(min_val, max_val)
    attempts_remaining = max_attempts
    guessed_numbers = []
    
    clear_screen()
    print(f"Game Started! Guess between {min_val} and {max_val}.\n")

    start_time = time.time()
    while attempts_remaining > 0:
        print(f"Previous Guesses: {guessed_numbers if guessed_numbers else 'None'}")
        raw_input = input(f"Attempt ({max_attempts - attempts_remaining + 1}/{max_attempts}) - Enter guess: ")
        
        try:
            guess = int(raw_input)
        except ValueError:
            print("❌ Invalid input! Enter a valid integer.\n")
            continue
            
        if guess < min_val or guess > max_val:
            print(f"❌ Pick a number within {min_val}-{max_val} range.\n")
            continue
            
        if guess in guessed_numbers:
            print("⚠️ You already guessed that number! Try again.\n")
            continue

        guessed_numbers.append(guess)
        attempts_remaining -= 1

        if guess == secret_number:
            elapsed_time = round(time.time() - start_time, 2)
            play_sound("win")
            print("\n" + "★" * 45)
            print(f"🎉 VICTORY! You guessed {secret_number} correctly!")
            print(f"Time Taken: {elapsed_time}s | Attempts Used: {max_attempts - attempts_remaining}")
            print("★" * 45)
            break
        else:
            direction = "TOO HIGH ⬆️" if guess > secret_number else "TOO LOW ⬇️"
            print(f"Result: {direction}")
            if attempts_remaining > 0:
                hint = generate_hint(secret_number, guess, min_val, max_val)
                print(f"💡 Hint: {hint}")
                print(f"Attempts left: {attempts_remaining}\n")
    else:
        play_sound("lose")
        print("\n" + "❌" * 25)
        print(f"GAME OVER! The number was: {secret_number}")

def main():
    while True:
        play_game()
        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()