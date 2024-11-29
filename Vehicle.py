class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Zīmols: {self.brand}, Modelis: {self.model}, Gads: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, seating):
        super().__init__(brand, model, year)
        self.seating = seating

    def display_details(self):
        super().display_details()
        print(f"Sēdvietas: {self.seating}")

    def honk(self):
        print("Mašīnas signāls: Beep Beep!")

class Bike(Vehicle):
    def __init__(self, brand, model, year, engine):
        super().__init__(brand, model, year)
        self.engine = engine

    def display_details(self):
        super().display_details()
        print(f"Motora tilpums: {self.engine}")

    def rev_engine(self):
        print(f"Motocikla signāls: Revv Revv!")

#Create Car and Bike objects
car1 = Car("Toyota", "Camry", 2022, 5)
bike1 = Bike("Yamaha", "AAA-456", 2021, 323)

#Display details and all specific methods
print("Informācija par mašīnu:")
car1.display_details()
car1.honk()

print("\nInformācijas par motociklu:")
bike1.display_details()
bike1.rev_engine()