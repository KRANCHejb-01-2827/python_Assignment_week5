# Polymorphism Challenge with Vehicles

class Car:
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane:
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat:
    def move(self):
        print("⛵ The boat is sailing on the water.")

class Bike:
    def move(self):
        print("🏍️ The bike is speeding on the highway.")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()
