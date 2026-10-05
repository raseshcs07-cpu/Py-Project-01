import string
import secrets
import pyperclip
from datetime import datetime


class PasswordGenerator:

    def __init__(self):
        self.password_history = []

        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        self.ambiguous = "O0Il1"

    # -----------------------------------------
    # DISPLAY BANNER
    # -----------------------------------------

    def banner(self):
        print("\n" + "=" * 60)
        print("             🔐 ADVANCED PASSWORD GENERATOR")
        print("=" * 60)

    # -----------------------------------------
    # CREATE CHARACTER POOL
    # -----------------------------------------

    def create_pool(self, use_lower, use_upper, use_numbers, use_special,
                    avoid_ambiguous):

        pool = ""

        if use_lower:
            pool += self.lowercase

        if use_upper:
            pool += self.uppercase

        if use_numbers:
            pool += self.numbers

        if use_special:
            pool += self.special

        if avoid_ambiguous:
            pool = "".join(
                character
                for character in pool
                if character not in self.ambiguous
            )

        return pool

    # -----------------------------------------
    # GENERATE PASSWORD
    # -----------------------------------------

    def generate_password(
        self,
        length,
        use_lower=True,
        use_upper=True,
        use_numbers=True,
        use_special=True,
        avoid_ambiguous=False
    ):

        if length < 4:
            print("\n❌ Password length must be at least 4.")
            return None

        pool = self.create_pool(
            use_lower,
            use_upper,
            use_numbers,
            use_special,
            avoid_ambiguous
        )

        if not pool:
            print("\n❌ No character types selected.")
            return None

        required_characters = []

        if use_lower:
            chars = self.lowercase
            if avoid_ambiguous:
                chars = "".join(
                    c for c in chars if c not in self.ambiguous
                )

            if chars:
                required_characters.append(secrets.choice(chars))

        if use_upper:
            chars = self.uppercase
            if avoid_ambiguous:
                chars = "".join(
                    c for c in chars if c not in self.ambiguous
                )

            if chars:
                required_characters.append(secrets.choice(chars))

        if use_numbers:
            chars = self.numbers
            if avoid_ambiguous:
                chars = "".join(
                    c for c in chars if c not in self.ambiguous
                )

            if chars:
                required_characters.append(secrets.choice(chars))

        if use_special:
            chars = self.special
            if avoid_ambiguous:
                chars = "".join(
                    c for c in chars if c not in self.ambiguous
                )

            if chars:
                required_characters.append(secrets.choice(chars))

        if length < len(required_characters):
            print("\n❌ Length is too small for selected options.")
            return None

        remaining = length - len(required_characters)

        password = required_characters

        for _ in range(remaining):
            password.append(secrets.choice(pool))

        secrets.SystemRandom().shuffle(password)

        final_password = "".join(password)

        self.password_history.append({
            "password": final_password,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return final_password

    # -----------------------------------------
    # PASSWORD STRENGTH CHECKER
    # -----------------------------------------

    def check_strength(self, password):

        score = 0

        if len(password) >= 8:
            score += 1

        if len(password) >= 12:
            score += 1

        if len(password) >= 16:
            score += 1

        if any(c.islower() for c in password):
            score += 1

        if any(c.isupper() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(c in self.special for c in password):
            score += 1

        if score <= 2:
            return "🔴 WEAK"

        elif score <= 4:
            return "🟠 MEDIUM"

        elif score <= 6:
            return "🟢 STRONG"

        else:
            return "🔵 VERY STRONG"

    # -----------------------------------------
    # GENERATE MULTIPLE PASSWORDS
    # -----------------------------------------

    def generate_multiple(self, count, length):

        passwords = []

        for _ in range(count):

            password = self.generate_password(
                length=length,
                use_lower=True,
                use_upper=True,
                use_numbers=True,
                use_special=True
            )

            if password:
                passwords.append(password)

        return passwords

    # -----------------------------------------
    # COPY PASSWORD
    # -----------------------------------------

    def copy_password(self, password):

        try:
            pyperclip.copy(password)
            print("\n📋 Password copied to clipboard!")

        except Exception:
            print("\n⚠️ Clipboard feature unavailable.")

    # -----------------------------------------
    # SAVE PASSWORD
    # -----------------------------------------

    def save_password(self, password):

        with open("password_history.txt", "a") as file:

            time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            file.write(
                f"[{time}] {password}\n"
            )

        print("\n💾 Password saved successfully!")

    # -----------------------------------------
    # SHOW HISTORY
    # -----------------------------------------

    def show_history(self):

        if not self.password_history:

            print("\n📭 No passwords generated in this session.")

            return

        print("\n" + "=" * 60)
        print("                 PASSWORD HISTORY")
        print("=" * 60)

        for index, item in enumerate(
            self.password_history,
            start=1
        ):

            print(
                f"{index}. {item['password']} "
                f"({item['time']})"
            )

    # -----------------------------------------
    # CLEAR HISTORY
    # -----------------------------------------

    def clear_history(self):

        self.password_history.clear()

        print("\n🗑️ Session history cleared!")


# =====================================================
# MAIN PROGRAM
# =====================================================


def main():

    generator = PasswordGenerator()

    while True:

        generator.banner()

        print("""
1. 🔐 Generate Password
2. 🔢 Generate Multiple Passwords
3. 💪 Check Password Strength
4. 📋 Show Password History
5. 🗑️ Clear Session History
6. ❌ Exit
""")

        choice = input("Enter your choice: ").strip()

        # -----------------------------------------
        # OPTION 1
        # -----------------------------------------

        if choice == "1":

            print("\n" + "-" * 60)
            print("              PASSWORD SETTINGS")
            print("-" * 60)

            try:
                length = int(
                    input("Enter password length: ")
                )

            except ValueError:

                print("\n❌ Please enter a valid number.")
                continue

            print("\nCharacter Options:")

            use_lower = input(
                "Include lowercase? (y/n): "
            ).lower() == "y"

            use_upper = input(
                "Include uppercase? (y/n): "
            ).lower() == "y"

            use_numbers = input(
                "Include numbers? (y/n): "
            ).lower() == "y"

            use_special = input(
                "Include special characters? (y/n): "
            ).lower() == "y"

            avoid_ambiguous = input(
                "Avoid ambiguous characters? (y/n): "
            ).lower() == "y"

            password = generator.generate_password(
                length,
                use_lower,
                use_upper,
                use_numbers,
                use_special,
                avoid_ambiguous
            )

            if password:

                print("\n" + "=" * 60)
                print("              GENERATED PASSWORD")
                print("=" * 60)

                print(f"\n🔑 {password}")

                print(
                    f"\n💪 Strength: "
                    f"{generator.check_strength(password)}"
                )

                print("\nOptions:")
                print("1. 📋 Copy")
                print("2. 💾 Save")
                print("3. ↩️ Back")

                action = input(
                    "\nChoose option: "
                ).strip()

                if action == "1":

                    generator.copy_password(password)

                elif action == "2":

                    generator.save_password(password)

        # -----------------------------------------
        # OPTION 2
        # -----------------------------------------

        elif choice == "2":

            try:

                count = int(
                    input("\nHow many passwords? ")
                )

                length = int(
                    input("Password length: ")
                )

            except ValueError:

                print("\n❌ Enter valid numbers.")
                continue

            if count <= 0:

                print("\n❌ Count must be greater than 0.")
                continue

            print("\n" + "=" * 60)
            print("              GENERATED PASSWORDS")
            print("=" * 60)

            passwords = generator.generate_multiple(
                count,
                length
            )

            for index, password in enumerate(
                passwords,
                start=1
            ):

                print(
                    f"\n{index}. {password}"
                )

        # -----------------------------------------
        # OPTION 3
        # -----------------------------------------

        elif choice == "3":

            print("\n" + "-" * 60)

            password = input(
                "Enter password to check: "
            )

            if password:

                strength = generator.check_strength(
                    password
                )

                print(
                    f"\nPassword Strength: {strength}"
                )

                print(
                    f"Password Length: {len(password)}"
                )

            else:

                print("\n❌ Password cannot be empty.")

        # -----------------------------------------
        # OPTION 4
        # -----------------------------------------

        elif choice == "4":

            generator.show_history()

        # -----------------------------------------
        # OPTION 5
        # -----------------------------------------

        elif choice == "5":

            generator.clear_history()

        # -----------------------------------------
        # OPTION 6
        # -----------------------------------------

        elif choice == "6":

            print("\n" + "=" * 60)
            print("       🔐 Thank you for using Password Generator!")
            print("=" * 60)

            break

        # -----------------------------------------
        # INVALID OPTION
        # -----------------------------------------

        else:

            print("\n❌ Invalid choice!")

        input("\nPress Enter to continue...")


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":
    main()