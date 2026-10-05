"""A simple, interactive password generator for the command line."""

import secrets
import string


def ask_yes_no(prompt):
    """Ask until the user enters y or n, then return a boolean."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter Y for yes or N for no.")


def generate_password(length, use_uppercase, use_digits, use_symbols):
    """Generate a strong password and include every selected character type."""
    groups = [string.ascii_lowercase]
    required_characters = [secrets.choice(string.ascii_lowercase)]

    if use_uppercase:
        groups.append(string.ascii_uppercase)
        required_characters.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        groups.append(string.digits)
        required_characters.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+[]{}?"
        groups.append(symbols)
        required_characters.append(secrets.choice(symbols))

    # Start with one character from each selected group, then securely shuffle.
    all_characters = "".join(groups)
    password_characters = required_characters[:]
    password_characters.extend(
        secrets.choice(all_characters)
        for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def get_password_length(minimum_length):
    """Ask for a valid length that can fit the selected character types."""
    while True:
        raw_length = input("Password length (8-128): ").strip()
        try:
            length = int(raw_length)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if length < 8 or length > 128:
            print("Choose a length between 8 and 128 characters.")
        elif length < minimum_length:
            print("That length is too short for all the character types you selected.")
        else:
            return length


def main():
    print("=" * 36)
    print("       PASSWORD GENERATOR")
    print("=" * 36)
    print("Lowercase letters are always included.")

    while True:
        use_uppercase = ask_yes_no("Include uppercase letters? (Y/N): ")
        use_digits = ask_yes_no("Include numbers? (Y/N): ")
        use_symbols = ask_yes_no("Include symbols? (Y/N): ")

        minimum_length = 1 + int(use_uppercase) + int(use_digits) + int(use_symbols)
        length = get_password_length(minimum_length)
        password = generate_password(length, use_uppercase, use_digits, use_symbols)

        print("\nYour password is:")
        print(password)
        print("\nKeep it somewhere secure and don't share it.")

        if not ask_yes_no("Generate another password? (Y/N): "):
            print("\nThanks for using Password Generator. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
