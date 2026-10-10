"""
=====================================================================
          ULTIMATE UNIT CONVERTER  v2.0   (Python + OOP)
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


# =====================================================================
#  SMALL SHARED DATA
# =====================================================================

# Words people use instead of symbols (irregular names / short forms)
ALIASES = {
    "feet": "ft", "inches": "in", "lbs": "lb", "kilo": "kg", "kilos": "kg",
    "kmph": "km/h", "kph": "km/h", "kmh": "km/h", "metre": "m",
    "metres": "m", "litre": "l", "litres": "l", "sec": "s", "secs": "s",
    "mins": "min", "hr": "h", "hrs": "h", "tonne": "t", "ton": "t",
    "tonnes": "t", "centigrade": "c", "sq m": "m2", "sq ft": "ft2",
}

# Popular conversions: (label, from_unit, to_unit)
POPULAR = [
    ("Pounds to Kilograms", "lb", "kg"),
    ("Kilograms to Pounds", "kg", "lb"),
    ("Feet to Inches", "ft", "in"),
    ("Inches to Feet", "in", "ft"),
    ("Inches to Centimeters", "in", "cm"),
    ("Centimeters to Inches", "cm", "in"),
    ("Meters to Feet", "m", "ft"),
    ("Feet to Meters", "ft", "m"),
    ("Kilometers to Miles", "km", "mi"),
    ("Miles to Kilometers", "mi", "km"),
    ("Celsius to Fahrenheit", "c", "f"),
    ("Fahrenheit to Celsius", "f", "c"),
    ("Celsius to Kelvin", "c", "k"),
    ("Liters to Gallons", "l", "gal"),
    ("Gallons to Liters", "gal", "l"),
    ("Ounces to Grams", "oz", "g"),
    ("Grams to Ounces", "g", "oz"),
    ("Stone to Kilograms", "st", "kg"),
    ("km/h to mph", "km/h", "mph"),
    ("mph to km/h", "mph", "km/h"),
    ("Hours to Minutes", "h", "min"),
    ("Days to Hours", "day", "h"),
    ("MB to GB", "mb", "gb"),
    ("GB to MB", "gb", "mb"),
    ("Degrees to Radians", "deg", "rad"),
    ("Radians to Degrees", "rad", "deg"),
    ("Acres to Hectares", "acre", "ha"),
    ("Atmosphere to Pascal", "atm", "pa"),
    ("Newton to Dyne", "n", "dyne"),
    ("kcal to kJ", "kcal", "kj"),
    ("Horsepower to Kilowatt", "hp", "kw"),
    ("eV to Joule", "ev", "j"),
]


# =====================================================================
#  PART 1 :  UNIT CONVERSION CLASSES
# =====================================================================
class Converter:
    """
    One category of units (Length, Mass, ...).
    units = { "symbol": ("Full Name", factor_to_base_unit) }
    Example: "km": ("Kilometer", 1000)  ->  1 km = 1000 m (base unit)
    """

    def __init__(self, category, base_unit, units):
        self.category = category
        self.base_unit = base_unit
        self.units = units

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

    def get_name(self, symbol):
        return self.units[symbol][0]

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise KeyError("Unit not found in this category.")
        value_in_base = value * self.units[from_unit][1]
        return value_in_base / self.units[to_unit][1]

    def convert_to_all(self, value, from_unit):
        results = {}
        for symbol in self.units:
            if symbol != from_unit:
                results[symbol] = self.convert(value, from_unit, symbol)
        return results

    def show_units(self):
        print(f"\n  {self.category}  (base unit: {self.base_unit})")
        print("  " + "-" * 44)
        for symbol, data in self.units.items():
            print(f"    {symbol:<10} -> {data[0]}")


class TemperatureConverter(Converter):
    """Temperature needs formulas, so it overrides convert()."""

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
        return (value - 491.67) * 5 / 9          # Rankine

    def from_celsius(self, value, unit):
        if unit == "c":
            return value
        if unit == "f":
            return value * 9 / 5 + 32
        if unit == "k":
            return value + 273.15
        return (value + 273.15) * 9 / 5          # Rankine

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise KeyError("Unit not found in this category.")
        celsius = self.to_celsius(value, from_unit)
        if celsius < -273.15:
            raise ValueError("Temperature is below absolute zero!")
        return self.from_celsius(celsius, to_unit)


class ConverterLibrary:
    """Holds all 30 converters and can search through them."""

    def __init__(self):
        self.converters = []
        self.load_all()

    def add(self, category, base_unit, units):
        self.converters.append(Converter(category, base_unit, units))

    def find_pair(self, unit1, unit2):
        """Find the category that has BOTH units. Returns (converter, sym1, sym2)."""
        for converter in self.converters:
            symbol1 = converter.find_symbol(unit1)
            symbol2 = converter.find_symbol(unit2)
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


# =====================================================================
#  PART 2 :  PHYSICS UNITS & DIMENSIONS  (11th / 12th syllabus)
# =====================================================================

# Topic names
BASE = "Base Quantities (SI)"
MECH = "Mechanics"
MATTER = "Properties of Matter"
HEAT = "Heat & Thermodynamics"
ELEC = "Electricity"
MAG = "Magnetism & EMI"
WAVE = "Waves & Optics"
MODERN = "Modern Physics"
TOPICS = [BASE, MECH, MATTER, HEAT, ELEC, MAG, WAVE, MODERN]

# Words removed from a question like "what is the unit of force?"
FILLER_WORDS = {
    "what", "is", "the", "unit", "units", "of", "dimension", "dimensions",
    "dimensional", "formula", "formulas", "si", "for", "a", "an", "in",
    "tell", "me", "about", "find", "give", "its", "are", "cgs", "show",
}


def normalize(text):
    """Lower-case and remove punctuation so searching is forgiving."""
    return text.lower().replace("'", "").replace("?", " ").replace(",", " ")


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
        return Dimension(*[a - b for a, b in zip(self.powers, other.powers)])


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

    def add(self, *args, **kwargs):
        self.quantities.append(PhysicalQuantity(*args, **kwargs))

    # ---------- searching ----------
    def clean_query(self, text):
        tokens = normalize(text).split()
        kept = [word for word in tokens if word not in FILLER_WORDS]
        if not kept:
            kept = tokens
        return " ".join(kept)

    def search(self, text):
        query = self.clean_query(text)
        if query == "":
            return []

        exact = []
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

    def with_dimension(self, dimension, exclude=None):
        return [q for q in self.quantities
                if q is not exclude and q.dimension.same_as(dimension)]

    # ---------- displaying ----------
    def show_details(self, q):
        print("\n  " + "=" * 58)
        print(f"  Quantity          : {q.name}   (symbol: {q.symbol})")
        print(f"  SI unit           : {q.unit_label()}")
        print(f"  In SI base units  : {q.base_form}")
        print(f"  Dimensional form. : {q.dimension}")
        print(f"  CGS unit          : {q.cgs}")
        print(f"  Formula / Meaning : {q.formula}")
        print(f"  Topic             : {q.topic}")

        same = [other.name for other in self.with_dimension(q.dimension, q)]
        if same:
            print(f"  Same dimensions as: {', '.join(same)}")
        print("  " + "=" * 58)

    def show_table(self, quantities):
        print(f"\n  {'Quantity':<34}{'SI unit':<18}Dimension")
        print("  " + "-" * 74)
        for q in quantities:
            print(f"  {q.name:<34}{q.unit_symbol:<18}{q.dimension}")

    # ---------- all physics data ----------
    def load_data(self):
        add = self.add
        D = Dimension

        # ===== BASE QUANTITIES =====
        add("Length", "l", "meter", "m", "m", D(L=1),
            "Distance between two points", BASE, "centimeter (cm)",
            aliases=["distance", "displacement", "height", "width", "radius"])
        add("Mass", "m", "kilogram", "kg", "kg", D(M=1),
            "Amount of matter in a body", BASE, "gram (g)")
        add("Time", "t", "second", "s", "s", D(T=1),
            "Duration between two events", BASE, "second (s)",
            aliases=["duration", "time period"])
        add("Electric current", "I", "ampere", "A", "A", D(A=1),
            "I = q / t", BASE, "abampere / statampere", aliases=["current"])
        add("Temperature", "T", "kelvin", "K", "K", D(K=1),
            "T(K) = T(C) + 273.15", BASE, "kelvin (K)")
        add("Amount of substance", "n", "mole", "mol", "mol", D(mol=1),
            "n = N / N_A  (N_A = Avogadro number)", BASE, "mole (mol)")
        add("Luminous intensity", "I_v", "candela", "cd", "cd", D(cd=1),
            "Light power per unit solid angle", BASE, "candela (cd)")

        # ===== MECHANICS =====
        add("Area", "A", "square meter", "m^2", "m^2", D(L=2),
            "A = l x b", MECH, "cm^2")
        add("Volume", "V", "cubic meter", "m^3", "m^3", D(L=3),
            "V = l x b x h", MECH, "cm^3")
        add("Velocity", "v", "meter per second", "m/s", "m s^-1",
            D(L=1, T=-1), "v = displacement / time", MECH, "cm/s",
            aliases=["speed"])
        add("Acceleration", "a", "meter per second squared", "m/s^2",
            "m s^-2", D(L=1, T=-2), "a = change in velocity / time", MECH,
            "cm/s^2 (gal)")
        add("Momentum", "p", "kilogram meter per second", "kg m/s",
            "kg m s^-1", D(M=1, L=1, T=-1), "p = m x v", MECH, "g cm/s")
        add("Force", "F", "newton", "N", "kg m s^-2", D(M=1, L=1, T=-2),
            "F = m x a", MECH, "dyne", aliases=["weight", "thrust"])
        add("Impulse", "J", "newton second", "N s", "kg m s^-1",
            D(M=1, L=1, T=-1), "Impulse = F x t = change in momentum", MECH,
            "dyne s")
        add("Work", "W", "joule", "J", "kg m^2 s^-2", D(M=1, L=2, T=-2),
            "W = F x d x cos(theta)", MECH, "erg")
        add("Energy", "E", "joule", "J", "kg m^2 s^-2", D(M=1, L=2, T=-2),
            "KE = 1/2 m v^2 ;  PE = m g h", MECH, "erg",
            aliases=["kinetic energy", "potential energy"])
        add("Power", "P", "watt", "W", "kg m^2 s^-3", D(M=1, L=2, T=-3),
            "P = W / t", MECH, "erg/s")
        add("Torque", "tau", "newton meter", "N m", "kg m^2 s^-2",
            D(M=1, L=2, T=-2), "tau = r x F", MECH, "dyne cm",
            aliases=["moment of force"])
        add("Moment of inertia", "I", "kilogram square meter", "kg m^2",
            "kg m^2", D(M=1, L=2), "I = m r^2", MECH, "g cm^2")
        add("Angular velocity", "omega", "radian per second", "rad/s",
            "s^-1", D(T=-1), "omega = angle / time", MECH, "rad/s",
            aliases=["angular frequency"])
        add("Angular acceleration", "alpha", "radian per second squared",
            "rad/s^2", "s^-2", D(T=-2), "alpha = change in omega / time", MECH,
            "rad/s^2")
        add("Angular momentum", "L", "kilogram square meter per second",
            "kg m^2/s", "kg m^2 s^-1", D(M=1, L=2, T=-1),
            "L = I x omega = r x p", MECH, "g cm^2/s")
        add("Density", "rho", "kilogram per cubic meter", "kg/m^3",
            "kg m^-3", D(M=1, L=-3), "rho = mass / volume", MECH, "g/cm^3")
        add("Spring constant", "k", "newton per meter", "N/m", "kg s^-2",
            D(M=1, T=-2), "F = k x", MECH, "dyne/cm",
            aliases=["force constant"])
        add("Gravitational constant", "G", "newton meter squared per kg squared",
            "N m^2/kg^2", "kg^-1 m^3 s^-2", D(M=-1, L=3, T=-2),
            "F = G m1 m2 / r^2", MECH, "dyne cm^2/g^2")
        add("Gravitational potential", "V_g", "joule per kilogram", "J/kg",
            "m^2 s^-2", D(L=2, T=-2), "V = - G M / r", MECH, "erg/g")
        add("Plane angle", "theta", "radian", "rad", "m/m (ratio)", D(),
            "theta = arc length / radius", MECH, "degree")
        add("Solid angle", "omega", "steradian", "sr", "m^2/m^2 (ratio)", D(),
            "omega = area / r^2", MECH, "-")

        # ===== PROPERTIES OF MATTER =====
        add("Pressure", "P", "pascal", "Pa", "kg m^-1 s^-2",
            D(M=1, L=-1, T=-2), "P = F / A", MATTER, "barye (dyne/cm^2)")
        add("Stress", "sigma", "pascal", "Pa", "kg m^-1 s^-2",
            D(M=1, L=-1, T=-2), "Stress = F / A", MATTER, "dyne/cm^2")
        add("Strain", "epsilon", "no unit", "-", "-", D(),
            "Strain = change in length / original length", MATTER, "-")
        add("Young's modulus", "Y", "pascal", "Pa", "kg m^-1 s^-2",
            D(M=1, L=-1, T=-2), "Y = stress / strain", MATTER, "dyne/cm^2",
            aliases=["modulus of elasticity"])
        add("Bulk modulus", "B", "pascal", "Pa", "kg m^-1 s^-2",
            D(M=1, L=-1, T=-2), "B = - P / (change in V / V)", MATTER,
            "dyne/cm^2")
        add("Modulus of rigidity", "eta", "pascal", "Pa", "kg m^-1 s^-2",
            D(M=1, L=-1, T=-2), "eta = shear stress / shear strain", MATTER,
            "dyne/cm^2", aliases=["shear modulus"])
        add("Poisson's ratio", "sigma", "no unit", "-", "-", D(),
            "sigma = lateral strain / longitudinal strain", MATTER, "-")
        add("Surface tension", "S", "newton per meter", "N/m", "kg s^-2",
            D(M=1, T=-2), "S = F / l", MATTER, "dyne/cm")
        add("Surface energy", "-", "joule per square meter", "J/m^2",
            "kg s^-2", D(M=1, T=-2), "Energy / area", MATTER, "erg/cm^2")
        add("Coefficient of viscosity", "eta", "pascal second", "Pa s",
            "kg m^-1 s^-1", D(M=1, L=-1, T=-1), "F = eta A (dv/dx)", MATTER,
            "poise", aliases=["viscosity"])

        # ===== HEAT & THERMODYNAMICS =====
        add("Heat", "Q", "joule", "J", "kg m^2 s^-2", D(M=1, L=2, T=-2),
            "Q = m c (change in T)", HEAT, "calorie (cal)",
            aliases=["thermal energy"])
        add("Heat capacity", "C", "joule per kelvin", "J/K",
            "kg m^2 s^-2 K^-1", D(M=1, L=2, T=-2, K=-1), "C = Q / change in T",
            HEAT, "cal/C")
        add("Specific heat capacity", "c", "joule per kilogram kelvin",
            "J/(kg K)", "m^2 s^-2 K^-1", D(L=2, T=-2, K=-1),
            "c = Q / (m x change in T)", HEAT, "cal/(g C)",
            aliases=["specific heat"])
        add("Latent heat", "L", "joule per kilogram", "J/kg", "m^2 s^-2",
            D(L=2, T=-2), "L = Q / m", HEAT, "cal/g")
        add("Thermal conductivity", "K", "watt per meter kelvin", "W/(m K)",
            "kg m s^-3 K^-1", D(M=1, L=1, T=-3, K=-1),
            "Q/t = K A (change in T) / d", HEAT, "cal/(s cm C)")
        add("Entropy", "S", "joule per kelvin", "J/K", "kg m^2 s^-2 K^-1",
            D(M=1, L=2, T=-2, K=-1), "change in S = Q / T", HEAT, "erg/K")
        add("Universal gas constant", "R", "joule per mole kelvin",
            "J/(mol K)", "kg m^2 s^-2 K^-1 mol^-1",
            D(M=1, L=2, T=-2, K=-1, mol=-1), "PV = n R T", HEAT,
            "erg/(mol K)", aliases=["gas constant"])
        add("Boltzmann constant", "k_B", "joule per kelvin", "J/K",
            "kg m^2 s^-2 K^-1", D(M=1, L=2, T=-2, K=-1), "E = k_B T", HEAT,
            "erg/K")
        add("Coefficient of linear expansion", "alpha", "per kelvin", "K^-1",
            "K^-1", D(K=-1), "alpha = change in L / (L x change in T)", HEAT,
            "C^-1")
        add("Stefan-Boltzmann constant", "sigma", "watt per sq meter per K^4",
            "W/(m^2 K^4)", "kg s^-3 K^-4", D(M=1, T=-3, K=-4),
            "P = sigma A T^4", HEAT, "erg/(s cm^2 K^4)")

        # ===== ELECTRICITY =====
        add("Electric charge", "q", "coulomb", "C", "A s", D(A=1, T=1),
            "q = I x t", ELEC, "statcoulomb (esu)", aliases=["charge"])
        add("Potential difference", "V", "volt", "V", "kg m^2 s^-3 A^-1",
            D(M=1, L=2, T=-3, A=-1), "V = W / q", ELEC, "statvolt",
            aliases=["voltage", "potential", "electric potential"])
        add("Electromotive force", "emf", "volt", "V", "kg m^2 s^-3 A^-1",
            D(M=1, L=2, T=-3, A=-1), "emf = - d(flux)/dt", ELEC, "statvolt",
            aliases=["emf"])
        add("Resistance", "R", "ohm", "ohm", "kg m^2 s^-3 A^-2",
            D(M=1, L=2, T=-3, A=-2), "R = V / I", ELEC, "statohm")
        add("Impedance", "Z", "ohm", "ohm", "kg m^2 s^-3 A^-2",
            D(M=1, L=2, T=-3, A=-2), "Z = V_rms / I_rms (AC)", ELEC, "statohm",
            aliases=["reactance"])
        add("Resistivity", "rho", "ohm meter", "ohm m", "kg m^3 s^-3 A^-2",
            D(M=1, L=3, T=-3, A=-2), "R = rho x l / A", ELEC, "ohm cm",
            aliases=["specific resistance"])
        add("Conductance", "G", "siemens", "S", "kg^-1 m^-2 s^3 A^2",
            D(M=-1, L=-2, T=3, A=2), "G = 1 / R", ELEC, "-", aliases=["mho"])
        add("Electrical conductivity", "sigma", "siemens per meter", "S/m",
            "kg^-1 m^-3 s^3 A^2", D(M=-1, L=-3, T=3, A=2), "sigma = 1 / rho",
            ELEC, "-")
        add("Capacitance", "C", "farad", "F", "kg^-1 m^-2 s^4 A^2",
            D(M=-1, L=-2, T=4, A=2), "C = q / V", ELEC, "statfarad")
        add("Electric field", "E", "volt per meter (or N/C)", "V/m",
            "kg m s^-3 A^-1", D(M=1, L=1, T=-3, A=-1), "E = F / q", ELEC,
            "dyne/statcoulomb", aliases=["electric field intensity"])
        add("Electric flux", "phi_E", "volt meter", "V m", "kg m^3 s^-3 A^-1",
            D(M=1, L=3, T=-3, A=-1), "phi = E A cos(theta)", ELEC, "-")
        add("Permittivity of free space", "eps_0", "farad per meter", "F/m",
            "kg^-1 m^-3 s^4 A^2", D(M=-1, L=-3, T=4, A=2),
            "F = q1 q2 / (4 pi eps_0 r^2)", ELEC, "-",
            aliases=["permittivity"])
        add("Electric dipole moment", "p", "coulomb meter", "C m", "A s m",
            D(L=1, T=1, A=1), "p = q x 2a", ELEC, "statcoulomb cm",
            aliases=["dipole moment"])
        add("Current density", "J", "ampere per square meter", "A/m^2",
            "A m^-2", D(L=-2, A=1), "J = I / A", ELEC, "-")

        # ===== MAGNETISM & EMI =====
        add("Magnetic field", "B", "tesla", "T", "kg s^-2 A^-1",
            D(M=1, T=-2, A=-1), "F = q v B sin(theta)", MAG, "gauss (G)",
            aliases=["magnetic flux density", "magnetic induction"])
        add("Magnetic flux", "phi_B", "weber", "Wb", "kg m^2 s^-2 A^-1",
            D(M=1, L=2, T=-2, A=-1), "phi = B A cos(theta)", MAG,
            "maxwell (Mx)")
        add("Inductance", "L", "henry", "H", "kg m^2 s^-2 A^-2",
            D(M=1, L=2, T=-2, A=-2), "emf = - L (dI/dt)", MAG, "abhenry",
            aliases=["self inductance", "mutual inductance"])
        add("Permeability of free space", "mu_0", "henry per meter", "H/m",
            "kg m s^-2 A^-2", D(M=1, L=1, T=-2, A=-2),
            "B = mu_0 I / (2 pi r)", MAG, "-", aliases=["permeability"])
        add("Magnetic dipole moment", "m", "ampere square meter", "A m^2",
            "A m^2", D(L=2, A=1), "m = N I A", MAG, "erg/gauss")
        add("Magnetic intensity", "H", "ampere per meter", "A/m", "A m^-1",
            D(L=-1, A=1), "H = B / mu", MAG, "oersted",
            aliases=["magnetising field"])

        # ===== WAVES & OPTICS =====
        add("Frequency", "f", "hertz", "Hz", "s^-1", D(T=-1),
            "f = 1 / T", WAVE, "hertz (Hz)")
        add("Wavelength", "lambda", "meter", "m", "m", D(L=1),
            "v = f x lambda", WAVE, "angstrom / cm")
        add("Wave number", "k", "per meter", "m^-1", "m^-1", D(L=-1),
            "wave number = 1 / lambda", WAVE, "cm^-1")
        add("Intensity of wave", "I", "watt per square meter", "W/m^2",
            "kg s^-3", D(M=1, T=-3), "I = Power / Area", WAVE, "erg/(s cm^2)",
            aliases=["intensity"])
        add("Power of lens", "P", "dioptre", "D", "m^-1", D(L=-1),
            "P = 1 / f (f in meters)", WAVE, "-")
        add("Refractive index", "n", "no unit", "-", "-", D(),
            "n = c / v", WAVE, "-")
        add("Luminous flux", "phi_v", "lumen", "lm", "cd sr", D(cd=1),
            "Light power as seen by the eye", WAVE, "-")
        add("Illuminance", "E_v", "lux", "lx", "cd sr m^-2", D(L=-2, cd=1),
            "E = luminous flux / area", WAVE, "phot")

        # ===== MODERN PHYSICS =====
        add("Planck's constant", "h", "joule second", "J s", "kg m^2 s^-1",
            D(M=1, L=2, T=-1), "E = h x f", MODERN, "erg s",
            aliases=["planck"])
        add("Work function", "phi_0", "joule (or eV)", "J", "kg m^2 s^-2",
            D(M=1, L=2, T=-2), "KE_max = h f - phi_0", MODERN, "erg")
        add("Radioactivity", "A", "becquerel", "Bq", "s^-1", D(T=-1),
            "A = lambda x N", MODERN, "curie (Ci)", aliases=["activity"])
        add("Decay constant", "lambda", "per second", "s^-1", "s^-1", D(T=-1),
            "N = N0 e^(- lambda t)", MODERN, "s^-1")
        add("Absorbed dose", "D", "gray", "Gy", "m^2 s^-2", D(L=2, T=-2),
            "D = energy absorbed / mass", MODERN, "rad")
        add("Rydberg constant", "R_H", "per meter", "m^-1", "m^-1", D(L=-1),
            "1/lambda = R (1/n1^2 - 1/n2^2)", MODERN, "cm^-1")


# =====================================================================
#  PART 3 :  HISTORY
# =====================================================================
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


# =====================================================================
#  PART 4 :  QUIZ
# =====================================================================
class PhysicsQuiz:
    def __init__(self, library):
        self.library = library

    def run(self):
        print("\n  ===== PHYSICS UNITS & DIMENSIONS QUIZ =====")
        try:
            total = int(input("  How many questions? (1-20): "))
        except ValueError:
            total = 5
        total = max(1, min(total, 20))

        pool = [q for q in self.library.quantities if q.unit_symbol != "-"]
        chosen = random.sample(pool, total)
        score = 0

        for number, q in enumerate(chosen, start=1):
            if random.choice(["unit", "dimension"]) == "unit":
                question = f"What is the SI unit of {q.name}?"
                correct = q.unit_label()
                wrong_pool = {x.unit_label() for x in pool}
            else:
                question = f"What is the dimensional formula of {q.name}?"
                correct = str(q.dimension)
                wrong_pool = {str(x.dimension) for x in self.library.quantities}

            wrong_pool.discard(correct)
            options = random.sample(sorted(wrong_pool), 3) + [correct]
            random.shuffle(options)

            print(f"\n  Q{number}. {question}")
            for letter, option in zip("abcd", options):
                print(f"     {letter}) {option}")

            answer = input("  Your answer (a/b/c/d): ").strip().lower()
            if len(answer) == 1 and answer in "abcd" \
                    and options["abcd".index(answer)] == correct:
                print("  Correct!")
                score += 1
            else:
                print(f"  Wrong. Correct answer: {correct}")

        print(f"\n  FINAL SCORE: {score} / {total}")
        percent = score * 100 / total
        if percent == 100:
            print("  Perfect! You really know your units!")
        elif percent >= 60:
            print("  Good job! Keep practising.")
        else:
            print("  Revise the quantities from option 7 and try again.")


# =====================================================================
#  PART 5 :  MAIN APPLICATION
# =====================================================================
class UnitConverterApp:
    def __init__(self):
        self.library = ConverterLibrary()
        self.physics = PhysicsLibrary()
        self.history = History()
        self.quiz = PhysicsQuiz(self.physics)
        self.precision = 6          # significant digits

    # ---------------- helper methods ----------------
    def format_number(self, number):
        if number == 0:
            return "0"
        size = abs(number)
        if 1e-6 <= size < 1e12:
            exponent = math.floor(math.log10(size))
            decimals = max(self.precision - 1 - exponent, 0)
            text = f"{number:.{decimals}f}"
            if "." in text:
                text = text.rstrip("0").rstrip(".")
            return text
        return format(number, f".{self.precision}g")

    def get_number(self, message):
        while True:
            try:
                value = float(input(message))
                if math.isinf(value) or math.isnan(value):
                    print("  Please enter a normal number.")
                    continue
                return value
            except ValueError:
                print("  Invalid number. Please try again.")

    def choose_category(self):
        converters = self.library.converters
        print("\n  Choose a category:")
        for index in range(0, len(converters), 2):
            left = f"{index + 1:>2}. {converters[index].category}"
            line = f"    {left:<30}"
            if index + 1 < len(converters):
                right = f"{index + 2:>2}. {converters[index + 1].category}"
                line += right
            print(line)

        while True:
            choice = input("  Enter number: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(converters):
                return converters[int(choice) - 1]
            print("  Invalid choice.")

    def choose_unit(self, converter, message):
        while True:
            text = input(message).strip()
            if text.lower() == "list":
                converter.show_units()
                continue
            symbol = converter.find_symbol(text)
            if symbol is not None:
                return symbol
            print("  Unit not found. Type 'list' to see the units.")

    def do_conversion(self, converter, value, from_unit, to_unit):
        """Convert, print and store in history (used by many menu options)."""
        try:
            result = converter.convert(value, from_unit, to_unit)
        except ValueError as error:
            print(f"  Error: {error}")
            return

        text = (f"{self.format_number(value)} {from_unit} = "
                f"{self.format_number(result)} {to_unit}   [{converter.category}]")
        print(f"\n  RESULT -> {text}")
        print(f"            ({converter.get_name(from_unit)} to "
              f"{converter.get_name(to_unit)})")
        self.history.add(text)

    # ---------------- 1. normal convert ----------------
    def normal_convert(self):
        converter = self.choose_category()
        converter.show_units()
        print("\n  (You can type symbols like 'km' or names like 'kilometer')")

        value = self.get_number("\n  Enter value: ")
        from_unit = self.choose_unit(converter, "  From unit: ")
        to_unit = self.choose_unit(converter, "  To unit  : ")
        self.do_conversion(converter, value, from_unit, to_unit)

    # ---------------- 2. quick convert ----------------
    def quick_convert(self):
        print("\n  Type like:   5 feet to inches   |   150 lb to kg")
        print("               100 c to f          |   2 gb to mb")
        line = input("  > ").strip().lower()

        parts = line.split(" to ")
        if len(parts) != 2:
            print("  Wrong format. Use:  <value> <unit> to <unit>")
            return

        left = parts[0].split(None, 1)
        if len(left) != 2:
            print("  Wrong format. Use:  <value> <unit> to <unit>")
            return

        try:
            value = float(left[0])
        except ValueError:
            print("  The first part must be a number.")
            return

        converter, from_unit, to_unit = self.library.find_pair(left[1], parts[1])
        if converter is None:
            print("  Those units are unknown or from different categories.")
            return
        self.do_conversion(converter, value, from_unit, to_unit)

    # ---------------- 3. popular conversions ----------------
    def popular_convert(self):
        print("\n  POPULAR CONVERSIONS")
        print("  " + "-" * 60)
        for index in range(0, len(POPULAR), 2):
            left = f"{index + 1:>2}. {POPULAR[index][0]}"
            line = f"  {left:<32}"
            if index + 1 < len(POPULAR):
                line += f"{index + 2:>2}. {POPULAR[index + 1][0]}"
            print(line)

        choice = input("\n  Enter number: ").strip()
        if not (choice.isdigit() and 1 <= int(choice) <= len(POPULAR)):
            print("  Invalid choice.")
            return

        label, unit1, unit2 = POPULAR[int(choice) - 1]
        converter, from_unit, to_unit = self.library.find_pair(unit1, unit2)
        value = self.get_number(
            f"  Enter value in {converter.get_name(from_unit)}: ")
        self.do_conversion(converter, value, from_unit, to_unit)

    # ---------------- 4. convert to all ----------------
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
        print("  " + "-" * 50)
        for symbol, result in results.items():
            name = converter.get_name(symbol)
            print(f"    {self.format_number(result):>18} {symbol:<9} ({name})")

        self.history.add(
            f"{self.format_number(value)} {from_unit} converted to all "
            f"{converter.category} units")

    # ---------------- 5. height converter ----------------
    def height_converter(self):
        print("\n  HEIGHT CONVERTER")
        print("    1. Feet & inches  ->  cm & meters")
        print("    2. Centimeters    ->  feet & inches")
        choice = input("  Choose: ").strip()

        if choice == "1":
            feet = self.get_number("  Feet  : ")
            inches = self.get_number("  Inches: ")
            total_inches = feet * 12 + inches
            cm = total_inches * 2.54
            text = (f"{self.format_number(feet)} ft {self.format_number(inches)} in"
                    f" = {self.format_number(cm)} cm"
                    f" = {self.format_number(cm / 100)} m")
        elif choice == "2":
            cm = self.get_number("  Centimeters: ")
            total_inches = cm / 2.54
            feet = int(total_inches // 12)
            inches = total_inches - feet * 12
            text = (f"{self.format_number(cm)} cm = {feet} ft "
                    f"{self.format_number(inches)} in")
        else:
            print("  Invalid choice.")
            return

        print(f"\n  RESULT -> {text}")
        self.history.add(text + "   [Height]")

    # ---------------- 6. physics quantity finder ----------------
    def find_quantity(self):
        print("\n  PHYSICS QUANTITY FINDER  (units + dimensions)")
        print("  Ask like:  force | unit of torque | N | joule | dimension of power")
        print("  Press Enter to go back.")

        while True:
            text = input("\n  Ask > ").strip()
            if text == "" or text.lower() == "back":
                return

            results = self.physics.search(text)
            if not results:
                print("  Not found. Try another name, or use option 7 to browse.")
            elif len(results) <= 3:
                for q in results:
                    self.physics.show_details(q)
            else:
                print(f"  {len(results)} matches found. Be more specific:")
                self.physics.show_table(results)

    # ---------------- 7. browse by topic ----------------
    def browse_topics(self):
        print("\n  BROWSE PHYSICS QUANTITIES")
        for number, topic in enumerate(TOPICS, start=1):
            print(f"    {number}. {topic}")
        print(f"    {len(TOPICS) + 1}. Show EVERYTHING")

        choice = input("  Choose: ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= len(TOPICS) + 1:
            print("  Invalid choice.")
            return

        choice = int(choice)
        if choice == len(TOPICS) + 1:
            for topic in TOPICS:
                print(f"\n  >>> {topic.upper()}")
                self.physics.show_table(self.physics.by_topic(topic))
        else:
            topic = TOPICS[choice - 1]
            print(f"\n  >>> {topic.upper()}")
            self.physics.show_table(self.physics.by_topic(topic))

        print("\n  Tip: use option 6 to see the formula, CGS unit and more "
              "for any quantity.")

    # ---------------- 8. dimension calculator ----------------
    def dimension_calculator(self):
        print("\n  DIMENSION CALCULATOR")
        print("  Multiply or divide two quantities and see the result.")
        print("  Example:  Force * Length  ->  [M^1 L^2 T^-2]  (= Work/Energy)")

        first = self.physics.find_one(input("\n  First quantity : "))
        if first is None:
            print("  Quantity not found.")
            return

        operation = input("  Operation (* or /): ").strip()
        if operation not in ("*", "/", "x"):
            print("  Please type * or /")
            return

        second = self.physics.find_one(input("  Second quantity: "))
        if second is None:
            print("  Quantity not found.")
            return

        if operation == "/":
            answer = first.dimension.divide(second.dimension)
        else:
            answer = first.dimension.multiply(second.dimension)

        symbol = "/" if operation == "/" else "x"
        print(f"\n  {first.name} {first.dimension}")
        print(f"  {symbol} {second.name} {second.dimension}")
        print(f"  = {answer}")

        matches = self.physics.with_dimension(answer)
        if matches:
            names = ", ".join(q.name for q in matches)
            print(f"\n  This dimension belongs to: {names}")
        else:
            print("\n  No quantity in our list has this dimension.")

    # ---------------- 10. show all units ----------------
    def show_all_units(self):
        choice = input("\n  Enter a category number, or press Enter for ALL: ").strip()
        converters = self.library.converters

        if choice == "":
            for converter in converters:
                converter.show_units()
        elif choice.isdigit() and 1 <= int(choice) <= len(converters):
            converters[int(choice) - 1].show_units()
        else:
            self.choose_category().show_units()

    # ---------------- 11. history menu ----------------
    def history_menu(self):
        print("\n  HISTORY")
        print("    1. View history")
        print("    2. Clear history")
        print("    3. Save history to file")
        choice = input("  Choose: ").strip()

        if choice == "1":
            self.history.show()
        elif choice == "2":
            self.history.clear()
        elif choice == "3":
            self.history.save_to_file()
        else:
            print("  Invalid choice.")

    # ---------------- 12. precision ----------------
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

    # ---------------- menu + main loop ----------------
    def show_menu(self):
        print("\n" + "=" * 52)
        print("            UNIT CONVERTER  -  MAIN MENU")
        print("=" * 52)
        print("   CONVERT")
        print("    1. Convert units (step by step)")
        print("    2. Quick convert  (e.g. 5 feet to inches)")
        print("    3. Popular conversions (lb to kg, ft to in ...)")
        print("    4. Convert to ALL units of a category")
        print("    5. Height converter (ft/in <-> cm)")
        print("   PHYSICS: UNITS & DIMENSIONS")
        print("    6. Find unit & dimension of a quantity")
        print("    7. Browse quantities topic-wise (11th/12th)")
        print("    8. Dimension calculator")
        print("    9. Quiz")
        print("   OTHER")
        print("   10. Show all conversion units")
        print("   11. History")
        print("   12. Change precision")
        print("    0. Exit")
        print("=" * 52)

    def run(self):
        print("\n  Welcome to the Ultimate Unit Converter!")

        actions = {
            "1": self.normal_convert,
            "2": self.quick_convert,
            "3": self.popular_convert,
            "4": self.convert_to_all,
            "5": self.height_converter,
            "6": self.find_quantity,
            "7": self.browse_topics,
            "8": self.dimension_calculator,
            "9": self.quiz.run,
            "10": self.show_all_units,
            "11": self.history_menu,
            "12": self.change_precision,
        }

        while True:
            self.show_menu()
            choice = input("  Your choice: ").strip()

            if choice == "0":
                print("\n  Thank you for using Unit Converter. Goodbye!\n")
                break
            elif choice in actions:
                actions[choice]()
            else:
                print("\n  Invalid option. Please choose from the menu.")


# =====================================================================
#  PROGRAM STARTS HERE
# =====================================================================
if __name__ == "__main__":
    app = UnitConverterApp()
    app.run()