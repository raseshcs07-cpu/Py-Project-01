class Convertor:

    def __init__(self,category, base_unit, units):
        self.category = category
        self.base_unit= base_unit
        self.units= units
        # self.history=[]
        # self.precision=4


    def convert(self, value, from_unit, to_unit):

        if from_unit not in self.units or to_unit not in self.units:            
          raise KeyError("Units Not found In this Category! ")

        value_in_base = value*self.units[from_unit][1]
        return value_in_base / self.units[to_unit][1]


    def convert_to_all(self,value,from_unit):

        results = {}
        for symbol in self.units:
           
           if symbol != from_unit:
               results[symbol] = self.convert(value, from_unit, symbol)

        return results



class Temperatureconvertor(Convertor):

    def convert(self, value, from_unit, to_unit):

        if from_unit == "C":
            if to_unit == "F":
                return (value * 9/5) + 32
            elif to_unit == "K":
                return value + 273.15 

        elif from_unit == "F":
            if to_unit == "C":
                return (value - 32) * 5/9
            elif to_unit == "K":
                return (value - 32) * 5/9 + 273.15

        elif from_unit == "K":
            if to_unit == "C":
                return value - 273.15
            elif to_unit == "F":
                return (value - 273.15) * 9/5 + 32


        elif from_unit == to_unit :
            return value 

        else :
            raise KeyError("Invalid Temperature unit! ")



class Convertorlibrary:

    def __init__(self):
        self.convertors = {}

    def add_convertor(self, category, convertor):
        self.convertors[category] = convertor



class Dimension:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def display(self):
        return f"{self.name} ({self.symbol})"



class PhysicalQuantity:

    def __init__(self, name, symbol, dimension):
        self.name = name
        self.symbol = symbol
        self.dimension = dimension

    def display(self):
        return f"{self.name} ({self.symbol}) - {self.dimension}"


class PhysicsLibrary:

    def __init__(self):
        self.quantities = {}

    def add_quantity(self, quantity):
        self.quantities[quantity.name] = quantity

    def find_quantity(self , name):
        return self.quantaties.get(name)

    def get_all_quantities(self):
        return self.quantaties.values()

    def search_by_dimension(self, dimension_name):
        results = []

        for quantity in self.quantities.values():
            if quantity.dimension == dimension_name:
                results.append(quantity)

        return results


    