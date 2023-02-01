import Car_9_2


class ElectricCar(Car_9_2.Car):
    """ 电动汽车 """

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """ 电车电池容量"""
        print(f"电车电池容量为 {self.battery_size}-kWh")


my_tesla = ElectricCar('tesla', 'model_s', 2023)
my_tesla.describe_battery()
