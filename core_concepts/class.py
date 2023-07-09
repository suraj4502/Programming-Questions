'''
OOP is used to create reusable, modular code that is easy to understand and maintain.
A class can be thought of as a blueprint or template for creating objects. It defines the properties and behaviors that are common to a group of similar objects.
An object is an instance of a class.
'''

class Car():
  def __init__(self,make,model,color,year):
    self.company = make
    self.model = model
    self.color = color
    self.mfd = year

  def start_engine(self):
    print(f"{self.company} {self.model} Started ....")

  def drive(self):
    print(f"The {self.color} colored vehicle drives down the road.")

  def honk_horn(self):
    print(f"The {self.company}'s {self.model} honks its horn.")


#initilaizing a instance of the class
# my_car = Car('Hyundai','verna','black',2022)
# print(my_car)
# print(my_car.company)  # Hyundai
# print(my_car.model) # Verna
# print(my_car.color) # Black
# print(my_car.mfd)  # 2022

# print(my_car.start_engine())
# print(my_car.drive())


class ElectricCar(Car):
  def __init__(self,make,model,color,year,battery_size):
    super().__init__(make,model,color,year)
    self.battery_size = battery_size

  def battery_charge(self):
    print(f"The battery of {self.company}'s {self.model} is charged.")


# my_ecar = ElectricCar('Tesla','S','red',2019,10000)

# print(my_ecar.battery_charge())
# print(my_ecar.start_engine())

class HybridCar(Car):
    def __init__(self, make, model,color, year, battery_size, fuel_capacity):
        super().__init__(make, model,color,year)
        self.battery_size = battery_size
        self.fuel_capacity = fuel_capacity

    def charge_battery(self):
        print(f"The {self.company} {self.model}'s battery is now fully charged.")

    def fill_gas_tank(self):
        print(f"The {self.company} {self.model}'s gas tank is now full.")




my_hybrid_car = HybridCar("Toyota", "Prius","blue", 2020, 100, 10)
my_hybrid_car.start_engine() # The 2020 Toyota Prius starts its engine. 
my_hybrid_car.drive()        # The car drives down the road.
my_hybrid_car.honk_horn()
my_hybrid_car.charge_battery()
my_hybrid_car.fill_gas_tank()
  
