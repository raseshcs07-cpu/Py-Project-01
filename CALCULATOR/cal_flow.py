"""
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
     if num2 == 0:
        print("Cannot calculate modulus with zero.")
 
 elif choice == "7":
     print("Thank you! \n" "Try Me anytime🧠")
     break
 
 else:
     if choice not in ["1","2","3","4","5","6"]:
         print("Invalid choice. Please try again.")
         continue
 
 num1 =float(input("Enter the first Number:"))
 num2 =float(input("Enter the second Number:"))
 
 
 if choice == "1":
     result = num1 + num2
     print("Result:", result)
 
 if choice == "2":
     result = num1 - num2
     print("Results:",result)
 
 if choice == "3":
     result = num1 * num2
     print("Result:",result)
 
 if choice == "4":
      
      if num2 == 0:
       print("Undefined")
      else:
       result = num1 / num2
       print("Result",result)
 
 if choice == "5":
     result = num1 ** num2
     print("Result",result)
 
 if choice == "6":
     result = num1 % num2
     print("Result",result)

 
 try:
     num1 = float(input("Enter the first Number:"))
     num2 = float(input("Enter the second Number:"))
 except ValueError:
     print("Please! Enter vaild numbers")
     continue 

 """


"""
while True
    ↓
Show menu
    ↓
Get choice
    ↓
7?
 ├─ Yes → break
 └─ No
      ↓
Valid choice?
 ├─ No → continue
 └─ Yes
      ↓
Get numbers
      ↓
Valid numbers?
 ├─ No → continue
 └─ Yes
      ↓
Perform selected operation
      ↓
Show result
      ↓
Back to menu

"""

"""
calculator.py

Functions 
   ↓
while True
   ↓
Menu
   ↓
Choice validation
   ↓
Number validation
   ↓
Function call
   ↓
Result
"""