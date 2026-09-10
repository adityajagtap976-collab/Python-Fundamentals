class SmartBulb:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def toggle_power(self):
        self.is_on = not self.is_on

    def set_brightness(self, new_level):
        if new_level >= 0 and new_level < 30:
            print("Low_Level")
        elif new_level >= 30 and new_level < 60:
            print("Medium_Level")
        elif new_level >= 60 and new_level < 100:
            print("High_Level")
        else:
            print("Not_Working")


my_bulb = SmartBulb("Philips")
my_bulb.toggle_power()
print(my_bulb.is_on)
my_bulb.set_brightness(30)

# How to print the brand of the bulb?
print(my_bulb.brand)
