import math

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Kļūda: dalīšana ar nulli"
        
class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def square_root(self, x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Kļūda: Nevar celt pakāpē negatīvu skaitli"
    
    def power(self, base, exponent):
        return math.pow(base, exponent)
    
basic_calc = Calculator()
sci_calc = ScientificCalculator()

#Basic calculator
print("Pamata kalkulators:")
print("Papildinājums:", basic_calc.add(10, 5))
print("Divīzija:", basic_calc.divide(10, 0))

#Scientific calculator
print("\nZinātnskais kalkulators:")
print("Kvadrātsakne:", sci_calc.square_root(16))
print("Palielināts n-pakāpē:", sci_calc.power(2, 8))