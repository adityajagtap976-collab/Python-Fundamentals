# Parent Class (Superclass)
class Vehicle:
    def __init__(self, brand: str, speed: int) -> None:
        self.brand = brand
        self.speed = speed

    def drive(self) -> None:
        print(f"The {self.brand} is driving at {self.speed} mph.")


# Child Class (Subclass) inheriting from Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand: str, speed: int, battery_capacity: int) -> None:
        super().__init__(brand, speed)  # Call the constructor of the parent class
        self.battery_capacity = battery_capacity  # Additional attribute for ElectricCar

    def charge(self) -> None:
        print(
            f"The {self.brand} is charging. Battery capacity: {self.battery_capacity} kWh."
        )


# Creating an object of the ElectricCar class
my_electric_car = ElectricCar("Tesla", 120, 75)
my_electric_car.charge()
