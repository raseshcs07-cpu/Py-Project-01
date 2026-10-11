
while True:


    try:
        print("\n╔══════════════════════════╗")
        print("║       UNIT CONVERTER     ║")
        print("╚══════════════════════════╝")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = int(input("Choose An Option: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue


    if choice == 4:
        print("\nExiting Unit Converter. Goodbye! 🫡")
        break

    if choice not in (1, 2, 3):
        print("Invalid choice! Please try again.")
        continue


    if choice == 1:
        print("""
╔══════════════════════════╗
║      LENGTH CONVERTER    ║
╚══════════════════════════╝
1. Meters to Kilometers
2. Kilometers to Meters
3. Meters to Centimeters
4. Centimeters to Meters
5. Back to Main Menu
""")


    elif choice == 2:
        print("""
╔══════════════════════════╗
║      WEIGHT CONVERTER    ║
╚══════════════════════════╝
1. Kilograms to Grams
2. Grams to Kilograms
3. Kilograms to Pounds
4. Pounds to Kilograms
5. Back to Main Menu
""")


    elif choice == 3:
        print("""
╔══════════════════════════╗
║   TEMPERATURE CONVERTER  ║
╚══════════════════════════╝
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Back to Main Menu
""")



    try:
        selected = int(input("Select an option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if selected == 5:
        print("Returning to the main menu...")
        continue

    if selected not in (1, 2, 3, 4):
        print("Invalid choice! Please try again.")
        continue

    try:
        if choice == 1:
            if selected == 1:
                value = float(input("Enter meters: "))
                result = value / 1000
                unit = "kilometers"

            elif selected == 2:
                value = float(input("Enter kilometers: "))
                result = value * 1000
                unit = "meters"

            elif selected == 3:
                value = float(input("Enter meters: "))
                result = value * 100
                unit = "centimeters"

            else:
                value = float(input("Enter centimeters: "))
                result = value / 100
                unit = "meters"

        elif choice == 2:
            if selected == 1:
                value = float(input("Enter kilograms: "))
                result = value * 1000
                unit = "grams"

            elif selected == 2:
                value = float(input("Enter grams: "))
                result = value / 1000
                unit = "kilograms"

            elif selected == 3:
                value = float(input("Enter kilograms: "))
                result = value * 2.20462
                unit = "pounds"

            else:
                value = float(input("Enter pounds: "))
                result = value / 2.20462
                unit = "kilograms"

        else:
            if selected == 1:
                value = float(input("Enter Celsius: "))
                result = (value * 9 / 5) + 32
                unit = "Fahrenheit"

            elif selected == 2:
                value = float(input("Enter Fahrenheit: "))
                result = (value - 32) * 5 / 9
                unit = "Celsius"

            elif selected == 3:
                value = float(input("Enter Celsius: "))
                result = value + 273.15
                unit = "Kelvin"

            else:
                value = float(input("Enter Kelvin: "))
                result = value - 273.15
                unit = "Celsius"

        print(f"\nResult: {result:.2f} {unit}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")