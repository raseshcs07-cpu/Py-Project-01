"""
#  we willfocus on 

✅ Calculation history
✅ Multiple calculations without restarting
✅ Clear history
✅ Better navigation
✅ Clear screen
✅ Expression-style calculations later
✅ V1 ke existing functions reuse honge
"""
import os 
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue\n")


def add(num1 , num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
       if num2 == 0:
           return None
       return num1 / num2

def power(num1 , num2):
    try:
      return num1 ** num2
    except OverflowError:
        return None


def modulus(num1 , num2):
       if num2 == 0:
          return None
       return num1 % num2


def main():
 
 history = []

 while True:

  clear_screen()

  print("\n\n=^==^==Calculator==#==#=\n")
  print("1. Addition ","(+) ")
  print("2. Subtraction ","(-) ")
  print("3. Multiplication ","(*) ")
  print("4. Division "," (÷)")
  print("5. Power", " (^) ")
  print("6. Modulus")
  print("--------------------------")
  print("7.View History","ˆˆ")
  print("8.Clear history")
  print("9.Exit","»\n")
  print("ˆ========================ˆ\n")



  choice = input("Enter your Choice: ").strip()
  
  if choice == "1":
      print("You selected Addition")
  
  elif choice == "2":
      print("You selected Subtraction")
  
  elif choice == "3":
      print("You selected Multiplication")
  
  elif choice == "4":
      print("You selected Division")
  
  elif choice == "5":
      print("You selected Power")
  
  elif choice == "6":
      print("You selected Modulus")

  elif choice == "7":
         print("\n--- Calculation History ---")

         if not history:
             print("No history yet!")
         else:
            for i, item in enumerate(reversed(history) , start=1):
              print(f"{i}. {item}")

         pause()
         continue

  elif choice == "8":
      history.clear()
      print("History Cleared✅")
      pause()
      continue
  
  elif choice == "9":
      print("\nThank you! \n" "Try Me anytime🧠")
      break
  
  else:
     #  if choice not in ["1","2","3","4","5","6"]:
          print("\nInvalid choice. Please try again.")
          pause()
          continue
 
 
  try:
           num1 = float(input("Enter the first Number:").strip())
           num2 = float(input("Enter the second Number:").strip())
  except ValueError:
      print("\nPlease! Enter vaild numbers")
      pause()
      continue 
 
  
  if choice == "1":
     result = add(num1, num2)
     print("Result:", result)

     history.append(f"{num1} + {num2} = {result}")
     pause()
 
  elif choice == "2":
     result = subtract(num1, num2)
     print("Result:", result)

     history.append(f"{num1} - {num2} = {result}")
     pause()
 
  elif choice == "3":
     result = multiply(num1, num2)
     print("Result:", result)

     history.append(f"{num1} * {num2} = {result}")
     pause()
 
  elif choice == "4":
     result = divide(num1, num2)
 
     if result is None:
         print("\nCannot divide by zero.")
         pause()
     else:
         print("Result:", result)
         history.append(f"{num1} ÷ {num2} = {result}")
         pause()
 
  elif choice == "5":
     result = power(num1, num2)

     if result is None:
         print("\nResult is to large to calculate")
         pause()
     else:
         print("Result:", result)
         history.append(f"{num1} ^ {num2} = {result}")
         pause()

  elif choice == "6":
     result = modulus(num1, num2)
 
     if result is None:
         print("\nCannot calculate modulus with zero.")
         pause()
     else:
         print("Result:", result)
         history.append(f"{num1} % {num2} = {result}")
         pause()


if __name__ == "__main__":
    main()