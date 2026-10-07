import string
import secrets
import pyperclip
from datetime import datetime


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

generator = Pass_Generator()


while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.") 


use_lower = input("Include lowercase ? (y/n): ").lower() == "y"
use_upper = input("Include uppercase ? (y/n): ").lower() == "y"
use_numbers = input("Include numbers ? (y/n): ").lower() == "y"
use_special = input("Include special Characters ? (y/n): ").lower() == "y"


# pool = generator.create_pool(True,True,True,True)
password = generator.generate_password(
    length,
    True, 
    True, 
    True, 
    True
    )
print(password)