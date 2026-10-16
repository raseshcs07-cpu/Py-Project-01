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

    def __init__(self):

        self.convertors = []
        self.load_all()


    def add(self, category, base_unit, units):
        self.convertors.append(convertor(self,category,base_unit,units))


    def find_pair(self, unit1, unit2):
        """Find the category that has BOTH units. Returns (converter, sym1, sym2)."""
      
        for converter in self.convertors:
            symbol1= converter.find_symbol(unit1)
            symbol2= converter.find_symbol(unit2)
            if symbol1 is not None and symbol2 is not None:
                return converter, symbol1, symbol2
        return None, None, None


    def load_all(self):
        # ---------------- LENGTH ----------------
        self.add("Length", "Meter", {
            "nm": ("Nanometer", 1e-9),
            "um": ("Micrometer (micron)", 1e-6),
            "angstrom": ("Angstrom", 1e-10),
            "mm": ("Millimeter", 0.001),
            "cm": ("Centimeter", 0.01),
            "m": ("Meter", 1),
            "km": ("Kilometer", 1000),
            "in": ("Inch", 0.0254),
            "ft": ("Foot", 0.3048),
            "yd": ("Yard", 0.9144),
            "mi": ("Mile", 1609.344),
            "nmi": ("Nautical Mile", 1852),
            "au": ("Astronomical Unit", 1.495978707e11),
            "ly": ("Light Year", 9.4607304725808e15),
            "pc": ("Parsec", 3.0856775814914e16),
        })

        # ---------------- MASS ----------------
        self.add("Mass / Weight", "Kilogram", {
            "amu": ("Atomic Mass Unit (u)", 1.66053906660e-27),
            "ug": ("Microgram", 1e-9),
            "mg": ("Milligram", 0.000001),
            "g": ("Gram", 0.001),
            "kg": ("Kilogram", 1),
            "quintal": ("Quintal", 100),
            "t": ("Metric Tonne", 1000),
            "carat": ("Carat", 0.0002),
            "tola": ("Tola", 0.01166375),
            "grain": ("Grain", 0.00006479891),
            "oz": ("Ounce", 0.028349523125),
            "lb": ("Pound", 0.45359237),
            "st": ("Stone", 6.35029318),
            "slug": ("Slug", 14.5939029),
            "shortton": ("Short Ton (US)", 907.18474),
            "longton": ("Long Ton (UK)", 1016.0469088),
        })

        # ---------------- TEMPERATURE ----------------
        self.converters.append(TemperatureConverter())

        # ---------------- AREA ----------------
        self.add("Area", "Square Meter", {
            "mm2": ("Square Millimeter", 0.000001),
            "cm2": ("Square Centimeter", 0.0001),
            "m2": ("Square Meter", 1),
            "km2": ("Square Kilometer", 1000000),
            "in2": ("Square Inch", 0.00064516),
            "ft2": ("Square Foot", 0.09290304),
            "yd2": ("Square Yard", 0.83612736),
            "mi2": ("Square Mile", 2589988.110336),
            "acre": ("Acre", 4046.8564224),
            "ha": ("Hectare", 10000),
        })

        # ---------------- VOLUME ----------------
        self.add("Volume", "Liter", {
            "mm3": ("Cubic Millimeter", 1e-6),
            "ml": ("Milliliter", 0.001),
            "cm3": ("Cubic Centimeter", 0.001),
            "l": ("Liter", 1),
            "m3": ("Cubic Meter", 1000),
            "in3": ("Cubic Inch", 0.016387064),
            "ft3": ("Cubic Foot", 28.316846592),
            "tsp": ("Teaspoon (US)", 0.00492892),
            "tbsp": ("Tablespoon (US)", 0.0147868),
            "floz": ("Fluid Ounce (US)", 0.0295735296),
            "cup": ("Cup (US)", 0.236588),
            "pt": ("Pint (US)", 0.473176),
            "qt": ("Quart (US)", 0.946353),
            "gal": ("Gallon (US)", 3.78541),
            "ukgal": ("Gallon (UK)", 4.54609),
            "bbl": ("Oil Barrel", 158.987294928),
        })

        # ---------------- TIME ----------------
        self.add("Time", "Second", {
            "ns": ("Nanosecond", 1e-9),
            "us": ("Microsecond", 1e-6),
            "ms": ("Millisecond", 0.001),
            "s": ("Second", 1),
            "min": ("Minute", 60),
            "h": ("Hour", 3600),
            "day": ("Day", 86400),
            "week": ("Week", 604800),
            "month": ("Month (30 days)", 2592000),
            "year": ("Year (365 days)", 31536000),
            "decade": ("Decade", 315360000),
            "century": ("Century", 3153600000),
        })

        # ---------------- SPEED ----------------
        self.add("Speed / Velocity", "Meter/second", {
            "cm/s": ("Centimeter per second", 0.01),
            "m/s": ("Meter per second", 1),
            "km/h": ("Kilometer per hour", 1 / 3.6),
            "mph": ("Miles per hour", 0.44704),
            "ft/s": ("Feet per second", 0.3048),
            "knot": ("Knot", 1852 / 3600),
            "mach": ("Mach (sea level)", 343),
            "light": ("Speed of Light", 299792458),
        })

        # ---------------- ACCELERATION ----------------
        self.add("Acceleration", "Meter/second^2", {
            "m/s2": ("Meter per second squared", 1),
            "cm/s2": ("Centimeter per second squared (Gal)", 0.01),
            "ft/s2": ("Foot per second squared", 0.3048),
            "g0": ("Standard Gravity (g)", 9.80665),
        })

        # ---------------- FORCE ----------------
        self.add("Force", "Newton", {
            "dyne": ("Dyne", 1e-5),
            "gf": ("Gram-force", 0.00980665),
            "n": ("Newton", 1),
            "kn": ("Kilonewton", 1000),
            "kgf": ("Kilogram-force", 9.80665),
            "lbf": ("Pound-force", 4.4482216152605),
            "ozf": ("Ounce-force", 0.278013851),
            "tf": ("Tonne-force", 9806.65),
        })

        # ---------------- PRESSURE ----------------
        self.add("Pressure", "Pascal", {
            "barye": ("Barye (dyne/cm2)", 0.1),
            "pa": ("Pascal", 1),
            "hpa": ("Hectopascal", 100),
            "mbar": ("Millibar", 100),
            "kpa": ("Kilopascal", 1000),
            "bar": ("Bar", 100000),
            "mpa": ("Megapascal", 1e6),
            "atm": ("Atmosphere", 101325),
            "torr": ("Torr", 133.322368),
            "mmhg": ("Millimeter of Mercury", 133.322387415),
            "psi": ("Pound per sq inch", 6894.757293168),
            "kgf/cm2": ("Kilogram-force per sq cm", 98066.5),
        })

        # ---------------- ENERGY ----------------
        self.add("Energy / Work / Heat", "Joule", {
            "ev": ("Electron Volt", 1.602176634e-19),
            "mev": ("Mega Electron Volt", 1.602176634e-13),
            "erg": ("Erg", 1e-7),
            "j": ("Joule", 1),
            "kj": ("Kilojoule", 1000),
            "mj": ("Megajoule", 1e6),
            "cal": ("Calorie", 4.184),
            "kcal": ("Kilocalorie", 4184),
            "wh": ("Watt-hour", 3600),
            "kwh": ("Kilowatt-hour", 3600000),
            "btu": ("British Thermal Unit", 1055.05585262),
            "ftlb": ("Foot-pound", 1.3558179483314),
        })

        # ---------------- POWER ----------------
        self.add("Power", "Watt", {
            "erg/s": ("Erg per second", 1e-7),
            "mw": ("Milliwatt", 0.001),
            "w": ("Watt", 1),
            "kw": ("Kilowatt", 1000),
            "megaw": ("Megawatt", 1e6),
            "gw": ("Gigawatt", 1e9),
            "hp": ("Horsepower (mechanical)", 745.69987158227),
            "ps": ("Horsepower (metric)", 735.49875),
            "btu/h": ("BTU per hour", 0.29307107),
        })

        # ---------------- TORQUE ----------------
        self.add("Torque", "Newton-meter", {
            "dyne-cm": ("Dyne-centimeter", 1e-7),
            "n-m": ("Newton-meter", 1),
            "kn-m": ("Kilonewton-meter", 1000),
            "kgf-m": ("Kilogram-force meter", 9.80665),
            "lbf-ft": ("Pound-force foot", 1.3558179483314),
            "lbf-in": ("Pound-force inch", 0.1129848290276),
        })

        # ---------------- DENSITY ----------------
        self.add("Density", "kg/m^3", {
            "kg/m3": ("Kilogram per cubic meter", 1),
            "g/l": ("Gram per liter", 1),
            "g/cm3": ("Gram per cubic cm", 1000),
            "g/ml": ("Gram per milliliter", 1000),
            "kg/l": ("Kilogram per liter", 1000),
            "lb/ft3": ("Pound per cubic foot", 16.01846337),
            "lb/in3": ("Pound per cubic inch", 27679.9047),
            "lb/gal": ("Pound per gallon (US)", 119.826427),
        })

        # ---------------- VISCOSITY ----------------
        self.add("Viscosity", "Pascal-second", {
            "pa-s": ("Pascal-second", 1),
            "mpa-s": ("Millipascal-second", 0.001),
            "poise": ("Poise", 0.1),
            "cp": ("Centipoise", 0.001),
            "lb/ft-s": ("Pound per foot-second", 1.4881639),
        })

        # ---------------- FREQUENCY ----------------
        self.add("Frequency", "Hertz", {
            "hz": ("Hertz", 1),
            "khz": ("Kilohertz", 1e3),
            "mhz": ("Megahertz", 1e6),
            "ghz": ("Gigahertz", 1e9),
            "rpm": ("Revolutions per minute", 1 / 60),
        })

        # ---------------- ANGULAR VELOCITY ----------------
        self.add("Angular Velocity", "Radian/second", {
            "rad/s": ("Radian per second", 1),
            "deg/s": ("Degree per second", math.pi / 180),
            "rpm": ("Revolutions per minute", 2 * math.pi / 60),
            "rps": ("Revolutions per second", 2 * math.pi),
        })

        # ---------------- ANGLE ----------------
        self.add("Angle", "Degree", {
            "arcsec": ("Arcsecond", 1 / 3600),
            "arcmin": ("Arcminute", 1 / 60),
            "deg": ("Degree", 1),
            "rad": ("Radian", 180 / math.pi),
            "grad": ("Gradian", 0.9),
            "turn": ("Full Turn", 360),
        })

        # ---------------- DIGITAL STORAGE ----------------
        self.add("Digital Storage", "Byte", {
            "bit": ("Bit", 0.125),
            "byte": ("Byte", 1),
            "kb": ("Kilobyte", 1024),
            "mb": ("Megabyte", 1024 ** 2),
            "gb": ("Gigabyte", 1024 ** 3),
            "tb": ("Terabyte", 1024 ** 4),
            "pb": ("Petabyte", 1024 ** 5),
        })

        # ---------------- FUEL EFFICIENCY ----------------
        self.add("Fuel Efficiency", "km/liter", {
            "km/l": ("Kilometer per liter", 1),
            "mi/l": ("Mile per liter", 1.609344),
            "mpg": ("Miles per Gallon (US)", 0.425143707),
            "mpg-uk": ("Miles per Gallon (UK)", 0.35400619),
        })

        # ---------------- ELECTRIC CHARGE ----------------
        self.add("Electric Charge", "Coulomb", {
            "e": ("Elementary Charge (e)", 1.602176634e-19),
            "statc": ("Statcoulomb (esu)", 3.33564e-10),
            "nc": ("Nanocoulomb", 1e-9),
            "uc": ("Microcoulomb", 1e-6),
            "mc": ("Millicoulomb", 1e-3),
            "c": ("Coulomb", 1),
            "mah": ("Milliampere-hour", 3.6),
            "ah": ("Ampere-hour", 3600),
            "faraday": ("Faraday", 96485.33212),
        })

        # ---------------- ELECTRIC CURRENT ----------------
        self.add("Electric Current", "Ampere", {
            "na": ("Nanoampere", 1e-9),
            "ua": ("Microampere", 1e-6),
            "ma": ("Milliampere", 1e-3),
            "a": ("Ampere", 1),
            "ka": ("Kiloampere", 1e3),
        })

        # ---------------- VOLTAGE ----------------
        self.add("Voltage (Potential)", "Volt", {
            "statv": ("Statvolt", 299.792458),
            "uv": ("Microvolt", 1e-6),
            "mv": ("Millivolt", 1e-3),
            "v": ("Volt", 1),
            "kv": ("Kilovolt", 1e3),
            "megav": ("Megavolt", 1e6),
        })

        # ---------------- RESISTANCE ----------------
        self.add("Electric Resistance", "Ohm", {
            "mohm": ("Milliohm", 1e-3),
            "ohm": ("Ohm", 1),
            "kohm": ("Kilohm", 1e3),
            "megohm": ("Megohm", 1e6),
        })

        # ---------------- CAPACITANCE ----------------
        self.add("Capacitance", "Farad", {
            "pf": ("Picofarad", 1e-12),
            "nf": ("Nanofarad", 1e-9),
            "uf": ("Microfarad", 1e-6),
            "mf": ("Millifarad", 1e-3),
            "f": ("Farad", 1),
        })

        # ---------------- INDUCTANCE ----------------
        self.add("Inductance", "Henry", {
            "nh": ("Nanohenry", 1e-9),
            "uh": ("Microhenry", 1e-6),
            "mh": ("Millihenry", 1e-3),
            "h": ("Henry", 1),
        })

        # ---------------- MAGNETIC FIELD ----------------
        self.add("Magnetic Field (B)", "Tesla", {
            "nt": ("Nanotesla", 1e-9),
            "ut": ("Microtesla", 1e-6),
            "gs": ("Gauss", 1e-4),
            "mt": ("Millitesla", 1e-3),
            "t": ("Tesla", 1),
        })

        # ---------------- MAGNETIC FLUX ----------------
        self.add("Magnetic Flux", "Weber", {
            "mx": ("Maxwell", 1e-8),
            "uwb": ("Microweber", 1e-6),
            "mwb": ("Milliweber", 1e-3),
            "wb": ("Weber", 1),
        })

        # ---------------- RADIOACTIVITY ----------------
        self.add("Radioactivity", "Becquerel", {
            "dpm": ("Disintegrations per minute", 1 / 60),
            "dps": ("Disintegrations per second", 1),
            "bq": ("Becquerel", 1),
            "kbq": ("Kilobecquerel", 1e3),
            "mbq": ("Megabecquerel", 1e6),
            "uci": ("Microcurie", 3.7e4),
            "mci": ("Millicurie", 3.7e7),
            "ci": ("Curie", 3.7e10),
        })

        # ---------------- RADIATION DOSE ----------------
        self.add("Radiation Dose", "Gray", {
            "ugy": ("Microgray", 1e-6),
            "mgy": ("Milligray", 1e-3),
            "gy": ("Gray", 1),
            "rd": ("Rad (dose)", 0.01),
            "erg/g": ("Erg per gram", 1e-4),
        })




# --------------------------------------------------------------------
#  PART 2 :  PHYSICS UNITS & DIMENSIONS  (11th / 12th syllabus)
# =====================================================================

#Topics:
BASE = "Base Quantites (SI)"
MECH = "Mechaniscs" 
MATTER = "Properties of Matter"
HEAT = "Heat & Thermodynamics"
ELEC = "Electricity"
MAG = "Magnetism & EMI"
WAVE = "Wave & Optics"
MODERN = "Modern Physics"
TOPICS = [BASE, MECH, MATTER, HEAT, ELEC, MAG, WAVE, MODERN]

# Words removed from a question like "what is the unit of force?"
FILLER_WORDS = {
    "what", "is", "the", "unit", "of", "dimension", "dimensions",
    "dimensional", "formula", "formulas", "si", "for", "a", "an", "in",
    "tell", "me", "about", "find", "give", "its", "are", "cgs", "show",
}


def normalize(text):
    """Lower-case and remove punctuation so searching is forgiving."""
    return text.lower().replace("'","").replace("?"," ").replace(","," ")



class Dimension:
    """
    Dimensional formula stored as the 7 SI base powers:
    M (mass), L (length), T (time), A (current),
    K (temperature), mol (amount), cd (luminous intensity)
    Force = M^1 L^1 T^-2  ->  Dimension(M=1, L=1, T=-2)
    """

    SYMBOLS = ["M", "L", "T", "A", "K", "mol", "cd"]

    def __init__(self, M=0, L=0, T=0, A=0, K=0, mol=0, cd=0):
        self.powers = [M, L, T, A, K, mol, cd]


    def __str__(self):
        parts = []

        for index, (symbol, power) in enumerate(zip(self.SYMBOLS, self.powers)):
        # M, L, T are always shown (textbook style); others only if used
           if index < 3 or power != 0:
             parts.append(f"{symbol}^{power}")
        return "[" + " ".join(parts) + "]"


    def same_as(self, other):
        return self.powers == other.powers


    def multiply(self, other):
        return Dimension(*[a + b for a, b in zip(self.powers, other.powers)])


    def divide(self, other):
        return Dimension(*[a - b for a,b in zip(self.powers , other.powers)])



class PhysicalQuantity:
    """One physical quantity with its unit, dimension and formula."""

    def __init__(self, name, symbol, unit_name, unit_symbol, base_form, 
                 dimension, formula, topic, cgs="-", aliases=None):
        self.name = name
        self.symbol = symbol
        self.unit_name = unit_name
        self.unit_symbol = unit_symbol
        self.base_form = base_form          # unit written in SI base units
        self.dimension = dimension          # Dimension object
        self.formula = formula
        self.topic = topic
        self.cgs = cgs
        self.aliases = aliases if aliases else []


    def unit_label(self):
        if self.unit_symbol == "-":
            return "no unit"
        return f"{self.unit_name} ({self.unit_symbol})"



class PhysicsLibrary:
    """Database of physical quantities + search + dimension tools."""

    def __init__(self):
        self.quantities = []
        self.load_data()


    def add (self, *args, **kwargs):
        self.quantities.append(PhysicalQuantity(*args, **kwargs))


    def clean_query(self,text):

        tokens = normalize(text).split()
        kept = [word for word in tokens if word not in FILLER_WORDS]
        if not kept:
            kept = tokens
        return " ".join(kept)


    def search(self,text):

        query = self.clean_query(text)
        if query == "":
            return []

        exact =[]
        partial = []
        for q in self.quantities:
            names = [normalize(q.name)] + [normalize(a) for a in q.aliases]
            unit_keys = [normalize(q.unit_name), normalize(q.unit_symbol)]

            if query in names or query in unit_keys:
                exact.append(q)
            else:
                words = query.split()
                for name in names + [unit_keys[0]]:
                    if all(word in name for word in words):
                        partial.append(q)
                        break

        return exact if exact else partial


    def find_one(self, text):
        results = self.search(text)
        if results:
            return results[0]
        return None


    def by_topic(self, topic):
        return [q for q in self.quantities if q.topic == topic]



    def with_dimension(self, dimension, exclude= None):
        return [q for q in self.quantities
            if q is not exclude and q.dimension.same_as(dimension)]


    def show_details(self, q):


    def show_table(self, quantities):


    def load_data(self):



class History;

    def __init__(self):


    def add(self,text);


    def show(self):


    def clear(self):


    def save_to_file(self, filname = "converison_history.txt"):




class PhysicsQuiz:

    def __init__(self, library):


    def run(self):



class UnitConvertorApp:

    def __init__(self):;


    def format_number(self, number):


    def get_number(self,message):


    def choose_unit(self, convertor, message):


    def do_converion(self, converter, value, from_unit, to_unit);


    def quick_convert(self):


    def popular_convert(self):


    def convert_to_all(self):


    def height_converter(self):


    def fund_quantity(self):


    def browse_topics(self):


    def dimension_calculator(self):


    def show_all_units(self):


    def history_menu(self):


    def change_precision(self):


    def show_menu(self):


    def run(self):


if __name__ = "__main__"
    app = UnitConverterApp()
    app.run()