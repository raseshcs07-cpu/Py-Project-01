import string
import secrets
import pyperclip
from datetime import datetime
from pathlib import Path
import json

class Pass_Generator:

    def __init__(self):
        self.password_history= []
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    def create_pool(self, use_lower, use_upper, use_numbers, use_special):
   
        pool = ""                                                                                          #pool ka simple meaning hai: password banane ke liye available characters ka collection.
       
        if use_lower:
            pool += self.lowercase
        if use_upper:
            pool += self.uppercase
        if use_numbers:
            pool += self.numbers
        if use_special:
            pool += self.special

        return pool

    def generate_password(self,length,use_lower, use_upper, use_numbers, use_special):

          required_chars = []

          if use_lower:
              required_chars.append(secrets.choice(self.lowercase))
          if use_upper:
              required_chars.append(secrets.choice(self.uppercase))
          if use_numbers:
              required_chars.append(secrets.choice(self.numbers))
          if use_special:
              required_chars.append(secrets.choice(self.special))

          pool = self.create_pool(
              use_lower,
              use_upper,
              use_numbers,
              use_special
    )
          password = required_chars

          for _ in range(length - len(required_chars)):
              password.append(secrets.choice(pool))

          secrets.SystemRandom().shuffle(password)                                                                                                                       # Securely shuffle the password
         
          return "".join(password)

    
    def check_strength(self,password):

        score = 0 

        if len(password) >=12:
         score += 1 

        if any(char.islower() for char in password):
         score += 1

        if any(char.isupper() for char in password):
         score += 1

        if any(char.isdigit() for char in password):
         score += 1

        if any(char in self.special for char in password):
         score += 1

        if score <= 2:
            return "week"

        elif score==3:
            return "medium"

        elif score == 4:
            return "strong"

        else :
            return "Very storng"


    def generate_multiple(
            self,
            count,
            length,
            use_lower,
            use_upper,
            use_numbers,
            use_special
            ):

      passwords = []

      for _ in range(count):

        password = self.generate_password(
            length,
            use_lower,
            use_upper,
            use_numbers,
            use_special
        )

        passwords.append(password)

      return passwords

generator = Pass_Generator()


def main():

    while True:

        print("\n" + "=" * 45)
        print("       🔐 PASSWORD GENERATOR")
        print("=" * 45)

        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            while True:
                try:

                    length = int(input("\nEnter password length: ") )

                    if length < 4:
                        print("Password length must be at least 4.")
                        continue
                    break

                except ValueError:
                    print("Please enter a valid number")

            while True:
                try:

                    count = int(input("How many passwords do you want? "))

                    if count < 1:
                        print( "Enter at least 1 password.")
                        continue
                    break
    
                except ValueError:
                        print("Please enter a valid number.")
    
    
            use_lower = input("Include lowercase ? (y/n): ").lower() == "y"
            use_upper = input("Include uppercase ? (y/n): ").lower() == "y"
            use_numbers = input("Include numbers ? (y/n): ").lower() == "y"
            use_special = input("Include special Characters ? (y/n): ").lower() == "y"
            
            if not any([
                use_lower,
                use_upper,
                use_numbers,
                use_special]):
            
                print("\n❌ You must select at least one ""character type.")
                continue
    
    
            selected_types = sum([
                    use_lower,
                    use_upper,
                    use_numbers,
                    use_special])
    
            if length < selected_types:
                print(f"\n❌ Password length must be at least "f"{selected_types}.")
                continue
    
    
            passwords = generator.generate_multiple(
                    count,
                    length,
                    use_lower,
                    use_upper,
                    use_numbers,
                    use_special)
            
    
            print("\n" + "=" * 45)
            print("          GENERATED PASSWORDS")
            print("=" * 45)
    
            for number, password in enumerate(passwords, 1):
    
                    strength = generator.check_strength(password)
    
                    print(f"\n{number}. {password}")
                    print(f"   Strength: {strength}")
    
            print("\n" + "=" * 45)
    

        elif choice == "2":
            password = input( "\nEnter password to check: " )
            strength = generator.check_strength(password)
            
            print(f"\nPassword Strength: {strength}")


        elif choice == "3":
            print("\nThank you for using ""Password Generator! 🔐")
            break

        else:
            print("\nInvalid choice. Please try again.")


# pool = generator.create_pool(True,True,True,True)
# password = generator.generate_password(
#     length,
#     True, 
#     True, 
#     True, 
#     True
#     )
# print(password)

# strenght = generator.check_strength(password)
# print("Strength: ", strenght)


if __name__ == "__main__":
    main()