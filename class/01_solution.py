class Car:

    total_cars = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model 
        Car.total_cars += 1

    def get_brand(self):
        return f"{self.__brand} - {self.__model}"
    
    @property
    def model(self):
        return f"{self.__model}"

    def full_name(self):
        return  f"{self.__brand} {self.__model}"
    
    @staticmethod
    def general_info():
        return f"my car"
    
    def fuel_type(self):
        return "Gasoline"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"

    
# my_car = Car("Toyota","Corolla")
# my_car2 = ElectricCar("Honda","Civic","100kWh")
# my_car.model = "Camry" # this will not work because model is a property
# print(my_car.model)

# print(isinstance(my_car2,my_car))

# print(my_car.__brand)
# print(my_car.get_brand())
# print(my_car2.full_name())
# print(Car.full_name(my_car))
# print(ElectricCar.general_info())
# print(Car.general_info())
# print(Car.total_cars)

class Battery:
    def __init__(self,size):
        self.size = size

    def get_size(self):
        return f"{self.size}"


class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

    def get_horsepower(self):
        return f"{self.horsepower}"


class ElectricCar2(Car,Battery,Engine):
    def __init__(self,brand,model,battery_size,horsepower):
        super().__init__(brand,model)
        Battery.__init__(self,battery_size)
        Engine.__init__(self,horsepower)

    def fuel_type(self):
        return "Electric"

my_car = ElectricCar2("Toyota","Corolla","100kWh","1000hp")

print(my_car.get_horsepower())
print(my_car.get_size())
print(my_car.full_name())
print(my_car.fuel_type())