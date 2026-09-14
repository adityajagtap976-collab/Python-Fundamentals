class SmartThermostat:
    def __init__(self, brand: str, initial_temp: int) -> None:
        self.brand = brand
        self.__temperature = initial_temp  # Private attribute

    # Getter method to safely VIEW the temperature
    def get_temperature(self) -> int:
        return self.__temperature

    # Setter method to safely UPDATE the temperature
    def set_temperature(self, new_temp: int) -> None:
        if 60 <= new_temp <= 90:  # Safe range check
            self.__temperature = new_temp
            print(f"Temperature set to {self.__temperature}°F")
        else:
            print("Temperature out of safe range (60-90°F)")


# Creating thermostat object
my_thermostat = SmartThermostat("Nest", 80)

# Using the getter method to view the temperature
print(my_thermostat.get_temperature())

# Using the setter method to update the temperature
my_thermostat.set_temperature(75)
