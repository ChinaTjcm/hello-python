from Car_9_2 import Car
from ElectricCar_9_3 import ElectricCar as ECar

# 声明油车
my_mzd = Car('马自达', '马自达-2型', 2010)
print(my_mzd.get_descriptive_name())

# 声明电车，引入时使用别名 as
my_byd = ECar('比亚迪', '驱逐舰05', 2022)
print(my_byd.get_descriptive_name())
