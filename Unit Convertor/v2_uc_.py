"""
=====================================================================
          ULTIMATE UNIT CONVERTER  v2.0  
=====================================================================
FEATURES
  1. Convert units in 30 categories (length, mass, force, electricity ...)
  2. Quick convert in one line        ->  5 feet to inches, 150 lb to kg
  3. Popular conversions list         ->  pounds to kg, feet to inches ...
  4. Convert one value to ALL units of a category
  5. Height converter                 ->  5 ft 9 in  <->  cm
  6. Physics quantity finder          ->  "unit of force" -> newton (N)
                                          + dimensional formula, CGS unit,
                                          formula, same-dimension quantities
  7. Browse 11th/12th physics quantities topic-wise (units + dimensions)
  8. Dimension calculator             ->  Force x Length = [M L^2 T^-2]
  9. Physics units & dimensions quiz
 10. Show all conversion units
 11. History (view / clear / save to file)
 12. Adjustable precision

Concepts used: classes, inheritance, method overriding, dictionaries,
lists, tuples, loops, functions, exceptions, file handling.
"""

import math
import random

# --------------------------------------------------------------------
#  DATA
# =====================================================================

# words , Symbols people use , instead of full names.[shortforms]
ALIASES = {
    "feet": "ft",  "inches": "in", "lbs": "lb", "kilo": "kg", "kilos": "kg",
    "kmph": "km/h", "kph": "km/h", "kmh": "km/h", "meter": "m", "meters": "m",
    "liter": "l", "liters": "l", "seconds": "s", "second": "s", "sec": "s",
    "secs": "s", "min": "m", "mins": "m", "hour": "h", "hours": "h", "hr": "h", "hrs": "h",
    "tonne": "t", "ton": "t", "tonnes": "t", "centigrade": "c", "sq m": "m2", "sq ft": "ft2"
}

# Popular conversions:[label: from_unit : to_unit]
POPULAR = [
    ("pounds to kilograms" , "lb" , "kg" ),
    ("kilograms  to pounds " , "kg" , "lb" ),
    ("feet to inches  " , "in" , "ft" ),
    ("inches  to feet " , "ft" , "in" ),
    ("centimeters  to inches " , "cm" , "in" ),
    ("inches  to centimeters " , "in" , "cm" ),
    (" meters to feet " , "m" , "ft" ),
    ("feet  to meters " , "ft" , "m" ),
    ("kilometers  to miles " , "km" , "mi" ),
    ("miles  to kilometers " , "mi" , "km" ),
    ("celsius  to fahrenheit " , "c" , "f" ),
    ("fahrenheit  to celsius " , "f" , "c" ),
    ("celsius  to kelvin " , "c" , "k" ),
    ("liters  to gallons " , "l" , "gal" ),
    ("gallons  to liters " , "gal" , "l" ),
    ("ounces  to grams " , "oz" , "g" ),
    ("grams  to ounces " , "g" , "oz" ),
    ("stone  to kilograms " , "st" , "kg" ),
    ("km/h  to mph " , "km/h" , "mph" ),
    ("mph  to km/h " , "mph" , "km/h" ),
    ("hours  to minutes " , "h" , "min" ),
    ("days  to hours " , "day" , "h" ),
    ("MB  to GB " , "mb" , "gb" ),
    ("GB  to MB " , "gb" , "mb" ),
    ("Degree  to Radians " , "deg" , "rad" ),
    ("Radians  to Degree " , "rad" , "deg" ),
    ("Acres  to Hectares " , "acre" , "ha" ),
    ("Atmosphere  to Pascal " , "atm" , "pa" ),
    ("Newton  to Dyne " , "n" , "dyne" ),
    ("Kcal  to KJ " , "kcal" , "kj" ),
    ("Horsepower  to kilowatt " , "hp" , "kw" ),
    ("eV  to Joule " , "ev" , "j" ),
]


# =====================================================================
#  PART 1 :  UNIT CONVERSION CLASSES
# =====================================================================
class convertor:
    """
    One category of units (Length, Mass, ...)
    units = { "symbol": ("Full Name", factor_to_base_unit) }
    Example: "km": ("Kilometer", 1000)  ->  1 km = 1000 m (base unit)
    """

    def __init__(self,category,base_unit,units):
        self.category=category
        self.base_unit=base_unit
        self.units=units


    def find_symbol(self, text):
        """Understands symbols (km), names (kilometer), plurals (feet, inches)."""

        text = text.strip().lower()
        candidates = [text]

        if text.endswith("s"):
            candidates.append(text[:-1])

        if text.endswith("es"):
            candidates.append(text[:-2])

        for word in candidates:
            if word in self.units:
                return word
            
            for symbol, data in self.units.items():
                short_name = data[0].split("(")[0].strip().lower()
                if short_name == word:
                    return symbol
                
            if word in ALIASES and ALIASES[word] in self.units:
                return ALIASES[word]
            
        return None


    def get_name(self,symbol):
        return self.units[symbol][0]


    def convert(self,value,from_unit,to_unit):

        if from_unit not in self.units or to_unit not in self.units:
            raise KeyError("Unit Not Found in this categort. ")

        value_in_base = value* self.units[from_unit][1]
        return value_in_base / self.units[to_unit][1]


    def convert_to_all(self,value,from_unit):
        results = {}

        for symbol in self.units:
            if symbol != from_unit:
                results[symbol] = self.convert(value,from_unit,symbol)
        return results


    def show_units(self):
        print(f"\n {self.category}  (base unit : {self.base_unit})")
        print(" " + "-" * 44)
        for symbol , data in self.units.items():
            print(f"     {symbol:<10} »» {data[0]}")



class TemperatureConverter(convertor):
    """Temperature needs formulas, so it overrides convert()."""

    def __init__(self):
        units = {
            "c": ("Celsius", None),
            "f": ("Fahrenheit",None),
            "k": ("Kelvin",None),
            "r": ("Rankine",None),
        }
        super().__init__("Temperature", "Celsius", units)


    def to_celsius(self, value, unit):

        if unit =="c":
            return value
        if unit =="f":
            return (value - 32)* 5 / 9
        if unit =="k":
            return (value - 273.15)
        return (value - 491.67) * 5 / 9

    def from_celsius(self, value, unit):

        if unit == "c":
            return value
        if unit == "f":
            return 9/5 * value + 32
        if unit == "k":
            return value + 273.15
        return (value + 273.15) * 9/5


    def convert(self, value , from_unit, to_unit):

        if from_unit not in self.units or to_unit not in self.units:
           raise KeyError("Unit not found in this category.")
        celsius = self.to_celsius(value, from_unit)

        if celsius < -273.15:
            raise ValueError("Temperature is below absolute zero!")
        return self.from_celsius(celsius,to_unit)



class ConverterLibrary:
    """Holds all 30 converters and can search through them."""