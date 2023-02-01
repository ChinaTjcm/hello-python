class Dog:
    """
        一次模拟小狗的简单尝试
    """

    def __init__(self, name, age):
        """ 初始化属性 name 、age """
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗收到命令蹲下 """
        print(f"{self.name} 狗狗蹲下")

    def roll_over(self):
        """ 模拟小狗收到命令打滚 """
        print(f"{self.name} 狗狗开始打滚")


my_dog = Dog('小天', 6)
print(f"狗的名字: {my_dog.name}")
print(f"狗的年龄: {my_dog.age}")
my_dog.sit()
my_dog.roll_over()
