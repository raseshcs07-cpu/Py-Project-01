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

        self.history_file = Path("password_history.json")
        self.load_history()

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
         
          password =  "".join(password)

          strength = self.check_strenght(password)

          history_record = {
            "password": password,
            "strength": strength,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          } 

          self.password_history.append(history_record)
          self.save_history()

          return password

    
    def check_strength(self,password):

        score = 0 
        if len(password) >= 8:
            score += 1

        if len(password) >= 12:
            score += 1

        if len(password) >= 16:
            score += 1

        if any(char.islower() for char in password):
         score += 1

        if any(char.isupper() for char in password):
         score += 1

        if any(char.isdigit() for char in password):
         score += 1

        if any(char in self.special for char in password):
         score += 1

        if len(password) > 0:

         repeated = False

        for i in range(len(password) - 1):

         if password[i] == password[i + 1]:
             repeated = True
             break

         if repeated:
            score -= 1

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


    def show_history(self):

        if not self.password_history:
            print("\nNO password history!")
            return

        print("\n" + "=" * 55)
        print("             PASSWORD HISTORY")
        print("=" * 55)

        for number,record in enumerate(self.password_history,1):

            print(f"\n{number}. Password : {record['password']}")
            print(f"   Strength  : {record['strength']}")
            print(f"   Generated : {record['time']}")

        print("\n" + "=" * 55)


    def clear_history(self):

        if not self.password_history:
            print("\nNo password history to clear.")
            return

        confirm = input("\nAre you sure you want to clear history? (y/n): ").strip().lower()

        if confirm == "y":

            self.password_history.clear()
            self.save_history()
            print("\n✓ Password history cleared.")

        else:

            print("\nHistory was not cleared.")


    def copy_password(self, password):

        try:
            pyperclip.copy(password)
            print("\n✓ Password copied to clipboard!")

        except Exception:
            print("\n✗ Unable to copy password.")


    def save_history(self):

        try:
            with open(self.history_file,"w") as file:
                json.dump(self.password_history,file,indent=4,)

        except OSError as error:
            print(f"\n✗ Could not save history: {error}")



    def load_history(self):

        if not self.history_file.exists():

           self.password_history = []
           return

        try:
            with open(self.history_file,"r") as file:
                content = file.read().strip()

                if content:
                    data = json.loads(content)

                    if isinstance(data, list):
                        self.password_history = data

                    else:
                        self.password_history = []

                else:
                    self.password_history = []

        except (json.JSONDecodeError,OSError ):
            self.password_history = []


    def regenerate_password(
        self,
        length,
        use_lower,
        use_upper,
        use_numbers,
        use_special):

        return self.generate_password(
            length,
            use_lower,
            use_upper,
            use_numbers,
            use_special)



generator = Pass_Generator()

def get_password_settings():

    while True:

        try:
            length = int(
                input("\nEnter password length: "))

            if length < 4:
                print( "\n✗ Password length must be at least 4.")
                continue

            if length > 256:
                print("\n✗ Password length cannot exceed 256.")
                continue
            break

        except ValueError:
            print( "\n✗ Please enter a valid number.")


    while True:

        try:
            count = int(input("How many passwords do you want? "))

            if count < 1:
                print("\n✗ Enter at least 1 password.")
                continue

            if count > 100:
                print("\n✗ Maximum 100 passwords at once.")
                continue
            break

        except ValueError:
            print("\n✗ Please enter a valid number.")


    print("\nCharacter Options")
    print("-" * 25)

    use_lower = (
        input("Include lowercase? (y/n): ")
        .strip()
        .lower() == "y"
    )

    use_upper = (
        input("Include uppercase? (y/n): ")
        .strip()
        .lower() == "y"
    )

    use_numbers = (
        input("Include numbers? (y/n): ")
        .strip()
        .lower() == "y"
    )

    use_special = (
        input("Include special characters? (y/n): ")
        .strip()
        .lower() == "y"
    )


    selected_types = sum([
        use_lower,
        use_upper,
        use_numbers,
        use_special])


    if selected_types == 0:
        print("\n✗ You must select at least one character type.")
        return None


    if length < selected_types:
        print(f"\n✗ Password length must be at least "f"{selected_types}.")
        return None

    return (
        length,
        count,
        use_lower,
        use_upper,
        use_numbers,
        use_special
    )


def password_action_menu(
    password,
    length,
    use_lower,
    use_upper,
    use_numbers,
    use_special
):

    while True:

        strength = generator.check_strength(password)

        print("\n" + "=" * 55)
        print("              PASSWORD GENERATED")
        print("=" * 55)

        print(f"\nPassword : {password}")
        print(f"Strength : {strength}")

        print("\n1. 📋 Copy Password")
        print("2. 🔄 Regenerate")
        print("3. 💾 Generate Another")
        print("4. ↩️ Back to Main Menu")

        choice = input(
            "\nEnter your choice: "
        ).strip()


        if choice == "1":
            generator.copy_password(password)

        elif choice == "2":
            password = generator.regenerate_password(
                length,
                use_lower,
                use_upper,
                use_numbers,
                use_special
            )

            print("\n✓ New password generated!")

        elif choice == "3":
            return "another"

        elif choice == "4":
            return "back"

        else:
            print("\n✗ Invalid choice.")



def generate_flow():

    settings = get_password_settings()

    if settings is None:

        return

    (
        length,
        count,
        use_lower,
        use_upper,
        use_numbers,
        use_special
    ) = settings


    passwords = generator.generate_multiple(
        count,
        length,
        use_lower,
        use_upper,
        use_numbers,
        use_special
    )


    print("\n" + "=" * 55)
    print("              GENERATED PASSWORDS")
    print("=" * 55)


    for number, password in enumerate(passwords,1):

        strength = generator.check_strength(password)
        print(f"\n{number}. {password}")
        print(f"   Strength: {strength}")


    # Action menu for the last generated password
    last_password = passwords[-1]

    password_action_menu(
        last_password,
        length,
        use_lower,
        use_upper,
        use_numbers,
        use_special
    )


def main():

    while True:

        print("\n")
        print("╔" + "═" * 53 + "╗")
        print("║" + "       🔐 PASSWORD GENERATOR".center(53) + "║")
        print("╚" + "═" * 53 + "╝")

        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. View Password History")
        print("4. Clear Password History")
        print("5. Exit")


        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
          generate_flow()

        elif choice == "2":

            password = input("\nEnter password to check: ")

            if not password:
                print("\n✗ Password cannot be empty.")
                continue
            strength = generator.check_strength(password)
            print(f"\nPassword Strength: {strength}")

        elif choice == "3":
            generator.show_history()

        elif choice == "4":
            generator.clear_history()



        elif choice == "5":
            print("\nThank you for using ""Password Generator! 🔐")
            break

        else:
            print("\n✗ Invalid choice. Please try again.")

            
# def main():

#     while True:

#         print("\n" + "=" * 45)
#         print("       🔐 PASSWORD GENERATOR")
#         print("=" * 45)

#         print("1. Generate Password")
#         print("2. Check Password Strength")
#         print("3. Exit")

#         choice = input("\nEnter your choice: ").strip()

#         if choice == "1":

#             while True:
#                 try:

#                     length = int(input("\nEnter password length: ") )

#                     if length < 4:
#                         print("Password length must be at least 4.")
#                         continue
#                     break

#                 except ValueError:
#                     print("Please enter a valid number")

#             while True:
#                 try:

#                     count = int(input("How many passwords do you want? "))

#                     if count < 1:
#                         print( "Enter at least 1 password.")
#                         continue
#                     break
    
#                 except ValueError:
#                         print("Please enter a valid number.")
    
    
#             use_lower = input("Include lowercase ? (y/n): ").lower() == "y"
#             use_upper = input("Include uppercase ? (y/n): ").lower() == "y"
#             use_numbers = input("Include numbers ? (y/n): ").lower() == "y"
#             use_special = input("Include special Characters ? (y/n): ").lower() == "y"
            
#             if not any([
#                 use_lower,
#                 use_upper,
#                 use_numbers,
#                 use_special]):
            
#                 print("\n❌ You must select at least one ""character type.")
#                 continue
    
    
#             selected_types = sum([
#                     use_lower,
#                     use_upper,
#                     use_numbers,
#                     use_special])
    
#             if length < selected_types:
#                 print(f"\n❌ Password length must be at least "f"{selected_types}.")
#                 continue
    
    
#             passwords = generator.generate_multiple(
#                     count,
#                     length,
#                     use_lower,
#                     use_upper,
#                     use_numbers,
#                     use_special)
            
    
#             print("\n" + "=" * 45)
#             print("          GENERATED PASSWORDS")
#             print("=" * 45)
    
#             for number, password in enumerate(passwords, 1):
    
#                     strength = generator.check_strength(password)
    
#                     print(f"\n{number}. {password}")
#                     print(f"   Strength: {strength}")
    
#             print("\n" + "=" * 45)
    

#         elif choice == "2":
#             password = input( "\nEnter password to check: " )
#             strength = generator.check_strength(password)
            
#             print(f"\nPassword Strength: {strength}")


#         elif choice == "3":
#             print("\nThank you for using ""Password Generator! 🔐")
#             break

#         else:
#             print("\nInvalid choice. Please try again.")


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