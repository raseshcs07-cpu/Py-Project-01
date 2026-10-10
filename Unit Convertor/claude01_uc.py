"""
=====================================================
        ULTIMATE UNIT CONVERTER  (Python + OOP)
=====================================================
Features:
  1. Convert between units in 11 categories
  2. Quick convert  (type:  25 km to mi)
  3. Convert one value to ALL units of a category
  4. View all supported units
  5. Conversion history (view / clear / save to file)
  6. Adjustable result precision
  7. Input validation and error handling

Concepts used: classes, inheritance, method overriding,
dictionaries, lists, loops, functions, exceptions, file handling.
"""


# ---------------------------------------------------------
# BASE CLASS  -  works for any category that has a
#                "multiply by a factor" relationship
# ---------------------------------------------------------
class Converter:
    """
    units = { "symbol": ("Full Name", factor_to_base_unit) }
    Example (length): "km": ("Kilometer", 1000)  -> 1 km = 1000 m (base)
    """

    def __init__(self, category, base_unit, units):
        self.category = category
        self.base_unit = base_unit
        self.units = units

    def has_unit(self, symbol):
        return symbol.lower() in self.units

    def get_name(self, symbol):
        return self.units[symbol.lower()][0]

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in self.units or to_unit not in self.units:
            raise KeyError("Unit not found in this category.")

        # Step 1: convert to base unit, Step 2: base -> target unit
        value_in_base = value * self.units[from_unit][1]
        return value_in_base / self.units[to_unit][1]

    def convert_to_all(self, value, from_unit):
        results = {}
        for symbol in self.units:
            if symbol != from_unit.lower():
                results[symbol] = self.convert(value, from_unit, symbol)
        return results

    def show_units(self):
        print(f"\n  {self.category} (base unit: {self.base_unit})")
        print("  " + "-" * 40)
        for symbol, data in self.units.items():
            print(f"    {symbol:<8} -> {data[0]}")


# ---------------------------------------------------------
# CHILD CLASS  -  Temperature (needs formulas, not factors)
# ---------------------------------------------------------
class TemperatureConverter(Converter):
    def __init__(self):
        units = {
            "c": ("Celsius", None),
            "f": ("Fahrenheit", None),
            "k": ("Kelvin", None),
            "r": ("Rankine", None),
        }
        super().__init__("Temperature", "Celsius", units)

    def to_celsius(self, value, unit):
        if unit == "c":
            return value
        if unit == "f":
            return (value - 32) * 5 / 9
        if unit == "k":
            return value - 273.15
        if unit == "r":
            return (value - 491.67) * 5 / 9

    def from_celsius(self, value, unit):
        if unit == "c":
            return value
        if unit == "f":
            return value * 9 / 5 + 32
        if unit == "k":
            return value + 273.15
        if unit == "r":
            return (value + 273.15) * 9 / 5

    # Method overriding: temperature uses its own logic
    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in self.units or to_unit not in self.units:
            raise KeyError("Unit not found in this category.")

        celsius = self.to_celsius(value, from_unit)
        if celsius < -273.15:
            raise ValueError("Temperature is below absolute zero!")
        return self.from_celsius(celsius, to_unit)


# ---------------------------------------------------------
# HISTORY CLASS
# ---------------------------------------------------------
class History:
    def __init__(self):
        self.records = []

    def add(self, text):
        self.records.append(text)

    def show(self):
        if not self.records:
            print("\n  No history yet.")
            return
        print("\n  ----- CONVERSION HISTORY -----")
        for number, record in enumerate(self.records, start=1):
            print(f"  {number}. {record}")

    def clear(self):
        self.records.clear()
        print("\n  History cleared.")

    def save_to_file(self, filename="conversion_history.txt"):
        if not self.records:
            print("\n  Nothing to save.")
            return
        with open(filename, "w") as file:
            for record in self.records:
                file.write(record + "\n")
        print(f"\n  History saved to '{filename}'")


# ---------------------------------------------------------
# MAIN APPLICATION CLASS
# ---------------------------------------------------------
class UnitConverterApp:
    def __init__(self):
        self.history = History()
        self.precision = 6  # significant digits
        self.converters = self.build_converters()

    # ---------- build all categories ----------
    def build_converters(self):
        length = Converter("Length", "Meter", {
            "mm": ("Millimeter", 0.001),
            "cm": ("Centimeter", 0.01),
            "m": ("Meter", 1),
            "km": ("Kilometer", 1000),
            "in": ("Inch", 0.0254),
            "ft": ("Foot", 0.3048),
            "yd": ("Yard", 0.9144),
            "mi": ("Mile", 1609.344),
            "nmi": ("Nautical Mile", 1852),
        })

        mass = Converter("Mass / Weight", "Kilogram", {
            "mg": ("Milligram", 0.000001),
            "g": ("Gram", 0.001),
            "kg": ("Kilogram", 1),
            "t": ("Metric Tonne", 1000),
            "oz": ("Ounce", 0.028349523125),
            "lb": ("Pound", 0.45359237),
            "st": ("Stone", 6.35029318),
        })

        area = Converter("Area", "Square Meter", {
            "mm2": ("Square Millimeter", 0.000001),
            "cm2": ("Square Centimeter", 0.0001),
            "m2": ("Square Meter", 1),
            "km2": ("Square Kilometer", 1000000),
            "in2": ("Square Inch", 0.00064516),
            "ft2": ("Square Foot", 0.09290304),
            "yd2": ("Square Yard", 0.83612736),
            "acre": ("Acre", 4046.8564224),
            "ha": ("Hectare", 10000),
        })

        volume = Converter("Volume", "Liter", {
            "ml": ("Milliliter", 0.001),
            "l": ("Liter", 1),
            "m3": ("Cubic Meter", 1000),
            "tsp": ("Teaspoon (US)", 0.00492892),
            "tbsp": ("Tablespoon (US)", 0.0147868),
            "cup": ("Cup (US)", 0.236588),
            "pt": ("Pint (US)", 0.473176),
            "qt": ("Quart (US)", 0.946353),
            "gal": ("Gallon (US)", 3.78541),
        })

        time = Converter("Time", "Second", {
            "ms": ("Millisecond", 0.001),
            "s": ("Second", 1),
            "min": ("Minute", 60),
            "h": ("Hour", 3600),
            "day": ("Day", 86400),
            "week": ("Week", 604800),
            "month": ("Month (30 days)", 2592000),
            "year": ("Year (365 days)", 31536000),
        })

        speed = Converter("Speed", "Meter/second", {
            "m/s": ("Meter per second", 1),
            "km/h": ("Kilometer per hour", 0.277778),
            "mph": ("Miles per hour", 0.44704),
            "ft/s": ("Feet per second", 0.3048),
            "knot": ("Knot", 0.514444),
            "mach": ("Mach (approx)", 343),
        })

        data = Converter("Digital Storage", "Byte", {
            "bit": ("Bit", 0.125),
            "byte": ("Byte", 1),
            "kb": ("Kilobyte", 1024),
            "mb": ("Megabyte", 1024 ** 2),
            "gb": ("Gigabyte", 1024 ** 3),
            "tb": ("Terabyte", 1024 ** 4),
            "pb": ("Petabyte", 1024 ** 5),
        })

        pressure = Converter("Pressure", "Pascal", {
            "pa": ("Pascal", 1),
            "kpa": ("Kilopascal", 1000),
            "bar": ("Bar", 100000),
            "atm": ("Atmosphere", 101325),
            "psi": ("Pound per sq inch", 6894.757),
            "mmhg": ("Millimeter of Mercury", 133.322),
        })

        energy = Converter("Energy", "Joule", {
            "j": ("Joule", 1),
            "kj": ("Kilojoule", 1000),
            "cal": ("Calorie", 4.184),
            "kcal": ("Kilocalorie", 4184),
            "wh": ("Watt-hour", 3600),
            "kwh": ("Kilowatt-hour", 3600000),
            "btu": ("British Thermal Unit", 1055.06),
        })

        power = Converter("Power", "Watt", {
            "w": ("Watt", 1),
            "kw": ("Kilowatt", 1000),
            "mw": ("Megawatt", 1000000),
            "hp": ("Horsepower", 745.7),
        })

        angle = Converter("Angle", "Degree", {
            "deg": ("Degree", 1),
            "rad": ("Radian", 57.29577951308232),
            "grad": ("Gradian", 0.9),
            "turn": ("Full Turn", 360),
        })

        temperature = TemperatureConverter()

        return [length, mass, temperature, area, volume, time,
                speed, data, pressure, energy, power, angle]

    # ---------- helper methods ----------
    def format_number(self, number):
        return format(number, f".{self.precision}g")

    def get_number(self, message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("  Invalid number. Please try again.")

    def choose_category(self):
        print("\n  Choose a category:")
        for number, conv in enumerate(self.converters, start=1):
            print(f"    {number:>2}. {conv.category}")

        while True:
            choice = input("  Enter number: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(self.converters):
                return self.converters[int(choice) - 1]
            print("  Invalid choice.")

    def choose_unit(self, converter, message):
        while True:
            unit = input(message).strip().lower()
            if converter.has_unit(unit):
                return unit
            print("  Unit not found. Type 'list' to see units.")
            if unit == "list":
                converter.show_units()

    def find_converter_for(self, unit1, unit2):
        for conv in self.converters:
            if conv.has_unit(unit1) and conv.has_unit(unit2):
                return conv
        return None

    # ---------- menu options ----------
    def normal_convert(self):
        converter = self.choose_category()
        converter.show_units()

        value = self.get_number("\n  Enter value: ")
        from_unit = self.choose_unit(converter, "  From unit: ")
        to_unit = self.choose_unit(converter, "  To unit  : ")

        try:
            result = converter.convert(value, from_unit, to_unit)
        except ValueError as error:
            print(f"  Error: {error}")
            return

        text = (f"{self.format_number(value)} {from_unit} = "
                f"{self.format_number(result)} {to_unit}   [{converter.category}]")
        print("\n  RESULT -> " + text)
        self.history.add(text)

    def quick_convert(self):
        print("\n  Type like:  25 km to mi   |   100 c to f   |   2 gb to mb")
        line = input("  > ").strip().lower().split()

        if len(line) != 4 or line[2] != "to":
            print("  Wrong format. Use:  <value> <unit> to <unit>")
            return

        try:
            value = float(line[0])
        except ValueError:
            print("  The first part must be a number.")
            return

        from_unit, to_unit = line[1], line[3]
        converter = self.find_converter_for(from_unit, to_unit)

        if converter is None:
            print("  Those units are unknown or from different categories.")
            return

        try:
            result = converter.convert(value, from_unit, to_unit)
        except ValueError as error:
            print(f"  Error: {error}")
            return

        text = (f"{self.format_number(value)} {from_unit} = "
                f"{self.format_number(result)} {to_unit}   [{converter.category}]")
        print("\n  RESULT -> " + text)
        self.history.add(text)

    def convert_to_all(self):
        converter = self.choose_category()
        converter.show_units()

        value = self.get_number("\n  Enter value: ")
        from_unit = self.choose_unit(converter, "  From unit: ")

        try:
            results = converter.convert_to_all(value, from_unit)
        except ValueError as error:
            print(f"  Error: {error}")
            return

        print(f"\n  {self.format_number(value)} {from_unit} equals:")
        print("  " + "-" * 40)
        for symbol, result in results.items():
            name = converter.get_name(symbol)
            print(f"    {self.format_number(result):>16} {symbol:<6} ({name})")

        self.history.add(
            f"{self.format_number(value)} {from_unit} converted to all "
            f"{converter.category} units")

    def show_all_units(self):
        for converter in self.converters:
            converter.show_units()

    def change_precision(self):
        print(f"\n  Current precision: {self.precision} significant digits")
        try:
            new_value = int(input("  Enter new precision (1-15): "))
            if 1 <= new_value <= 15:
                self.precision = new_value
                print("  Precision updated.")
            else:
                print("  Please enter a number between 1 and 15.")
        except ValueError:
            print("  Invalid input.")

    # ---------- main loop ----------
    def show_menu(self):
        print("\n" + "=" * 46)
        print("          UNIT CONVERTER - MAIN MENU")
        print("=" * 46)
        print("  1. Convert units (step by step)")
        print("  2. Quick convert (type in one line)")
        print("  3. Convert to ALL units of a category")
        print("  4. Show all supported units")
        print("  5. View history")
        print("  6. Clear history")
        print("  7. Save history to file")
        print("  8. Change precision")
        print("  0. Exit")
        print("=" * 46)

    def run(self):
        print("\n  Welcome to the Ultimate Unit Converter!")

        while True:
            self.show_menu()
            choice = input("  Your choice: ").strip()

            if choice == "1":
                self.normal_convert()
            elif choice == "2":
                self.quick_convert()
            elif choice == "3":
                self.convert_to_all()
            elif choice == "4":
                self.show_all_units()
            elif choice == "5":
                self.history.show()
            elif choice == "6":
                self.history.clear()
            elif choice == "7":
                self.history.save_to_file()
            elif choice == "8":
                self.change_precision()
            elif choice == "0":
                print("\n  Thank you for using Unit Converter. Goodbye!\n")
                break
            else:
                print("\n  Invalid option. Please choose from the menu.")


# ---------------------------------------------------------
# PROGRAM STARTS HERE
# ---------------------------------------------------------
if __name__ == "__main__":
    app = UnitConverterApp()
    app.run()