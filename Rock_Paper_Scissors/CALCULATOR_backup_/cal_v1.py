"""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Modulus
7. Exit


For version 1:

Language : Python
Api = None 
Interface = Terminal 
Database = none 
Library = none
"""

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
    return num1 ** num2

def modulus(num1 , num2):
       if num2 == 0:
          return None
       return num1 % num2


def main():
 while True:

  print("\n\n===^==^====\n Calculator\n===#==#====\n")
  print("1.Addition ","(+) ")
  print("2.Subtraction ","(-) ")
  print("3.Multiplication ","(*) ")
  print("4.Division "," (÷)")
  print("5.Power", " (^) ")
  print("6.Modulus")
  print("7.Exit","»\n")


  choice = input("Enter your Choice: ")
  
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
      print("Thank you! \n" "Try Me anytime🧠")
      break
  
  else:
     #  if choice not in ["1","2","3","4","5","6"]:
          print("Invalid choice. Please try again.")
          continue
 
 
  try:
           num1 = float(input("Enter the first Number:"))
           num2 = float(input("Enter the second Number:"))
  except ValueError:
      print("Please! Enter vaild numbers")
      continue 
 
  
  if choice == "1":
     result = add(num1, num2)
     print("Result:", result)
 
  elif choice == "2":
     result = subtract(num1, num2)
     print("Result:", result)
 
  elif choice == "3":
     result = multiply(num1, num2)
     print("Result:", result)
 
  elif choice == "4":
     result = divide(num1, num2)
 
     if result is None:
         print("Cannot divide by zero.")
     else:
         print("Result:", result)
 
  elif choice == "5":
     result = power(num1, num2)
     print("Result:", result)
 
  elif choice == "6":
     result = modulus(num1, num2)
 
     if result is None:
         print("Cannot calculate modulus with zero.")
     else:
         print("Result:", result)
 
if __name__ == "__main__":
    main()