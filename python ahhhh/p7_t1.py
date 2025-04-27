# 1

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_vehicle(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_battery(self):
        print("Battery Capacity:", self.battery_capacity, "kWh")

class Car(Vehicle, Electric):
    def __init__(self, brand, model, year, battery_capacity):
        Vehicle.__init__(self, brand, model, year)
        Electric.__init__(self, battery_capacity)

    def display_car(self):
        self.display_vehicle()
        self.display_battery()


car = Car("Tesla", "Model S", 2022, 100)
car.display_car()

