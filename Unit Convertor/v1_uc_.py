

print("╔══════════════════════════╗")
print("║       UNIT CONVERTER     ║")
print("╚══════════════════════════╝")

print("1. Length: ")
print("2. Weight: ")
print("3. Temperature: ")
print("4. Exit()\n")

choice = int(input("Choose An Option: "))

if choice == 1:
    print("\nYou selected Length!")

elif choice == 2:
    print("\nYou selected Weight!")

elif choice == 3:
    print("\nYou selected Temperature!")

elif choice == 4:
    print("\nExiting Unit Converter. Goodbye!")

else:
    print("\nInvalid choice! Please try again.!")