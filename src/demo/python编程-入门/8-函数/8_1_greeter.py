def greet_user(username):
    """显示简单的问候语。"""
    print(f"你好 ! {username.title()}")


def describe_pet(animal_type='狗', pet_name='cm'):
    """ 显示宠物信息"""
    print(f" 我有这类宠物: {animal_type}")
    print(f" 宠物名称是: {pet_name}")


# 学习传参
greet_user('陈明先生')
# 顺序传参
describe_pet('猫', 'xqq')
# 格式传参
describe_pet(animal_type='猫')
