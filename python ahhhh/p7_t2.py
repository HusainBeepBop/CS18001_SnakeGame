# 2

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self._model = model  
        self.__year = year  

    def get_year(self):
        return self.__year  

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

class Car(Vehicle, Electric):
    def __init__(self, brand, model, year, battery_capacity):
        Vehicle.__init__(self, brand, model, year)
        Electric.__init__(self, battery_capacity)

    def display_attributes(self):
        print("Brand (Public):", self.brand)
        print("Model (Protected):", self._model)
        print("Year (Private):", self.get_year())
        print("Battery Capacity:", self.battery_capacity)


car = Car("Tesla", "Model 3", 2021, 75)
car.display_attributes()
