class Car:
    """
    一辆汽车
    """

    def __int__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        """ 公里数--新车是 0 """
        self.odometer_reading = 0

    def update_odometer(self, meter):

        if meter >= self.odometer_reading:
            self.odometer_reading = meter
        else:
            print("禁止比现有公里数小")

    def increment_odometer(self, meter):
        """ 里程指定增加 """
        self.odometer_reading += meter


my_car = Car('奔驰', 'S500', 2023)
my_car.update_odometer(2300)
my_car.increment_odometer(1000)
print(f"我的车最新公里数，应该是 3300 ，现在输出为：{my_car.odometer_reading}")