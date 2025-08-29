# Parent class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def info(self):
        print(f"This is a {self.brand} vehicle with {self.wheels} wheels.")


# Child class (Car inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, wheels, color):
        # Call parent constructor
        super().__init__(brand, wheels)
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} {self.model} is driving 🚗")

    # Encapsulation (private attribute)
    __engine_number = "Hidden"

    def set_engine_number(self, number):
        self.__engine_number = number

    def get_engine_number(self):
        print(f"Engine Number: {self.__engine_number}")


# Another child class (to show polymorphism)
class Bike(Vehicle):
    def __init__(self, brand, wheels, bike_type):
        super().__init__(brand, wheels)
        self.bike_type = bike_type

    def drive(self):
        print(f"The {self.brand} {self.bike_type} bike is riding 🏍️")


# Create objects
car1 = Car("Toyota", "Corolla", 4, "Red")
car2 = Car("Tesla", "Model 3", 4, "Black")
bike1 = Bike("Yamaha", 2, "Sport")

# Demonstration
car1.info()
car1.drive()
car1.set_engine_number("ENG12345XYZ")
car1.get_engine_number()

car2.info()
car2.drive()

bike1.info()
bike1.drive()
