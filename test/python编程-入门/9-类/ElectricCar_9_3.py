import Car_9_2


class Battery:
    """ 电池信息 """

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    """ 电量转为里程数 """

    def get_range(self):
        """ 打印一条信息，指出电瓶的续航里程 """
        # 暂定规则，100 能开 150km
        return self.battery_size / 100 * 150


class ElectricCar(Car_9_2.Car):
    """ 电动汽车 """

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()

    def describe_battery(self):
        """ 电车电池容量"""
        print(f"电车电池容量为 {self.battery_size}-kWh")
        return self.battery_size

    def fill_gas_tank(self):
        """ 电动汽车没有油箱 """
        print(f"{self.make} {self.model} 电车没有油箱")


def main():
    my_tesla = ElectricCar('tesla', 'model_s', 2023)
    # 获取当前电量
    my_tesla.describe_battery()
    # 重写父类
    my_tesla.fill_gas_tank()
    # 通过电量计算里程数
    range_value = my_tesla.battery.get_range()
    print("\t")
    print("\t")
    # 统一展示
    # f 拼接
    print(f'{my_tesla.get_descriptive_name()}  当前电量：{my_tesla.describe_battery()} 可以行驶：{str(range_value)} km')
    # format 拼接
    print(' {} 当前电量：{} 可以行驶：{} km'.format(
        my_tesla.get_descriptive_name(),
        my_tesla.describe_battery(),
        str(range_value)))
    # 百分号 拼接
    print(' %s 当前电量：%s 可以行驶：%s km' % (
        my_tesla.get_descriptive_name(),
        my_tesla.describe_battery(),
        str(range_value)))

# main()
