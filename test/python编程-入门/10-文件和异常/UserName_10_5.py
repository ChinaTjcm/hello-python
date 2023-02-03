import json
from FileReader_10_1 import getRootPath

# 10-11 练习题
print('欢迎客户')


# 获取数字方法
def get_store_num():
    file_path = getRootPath() + '\\test\\python编程-入门\\file\\10\\username.json'

    num = ''
    try:
        with open(file_path) as file_object:
            if file_object is not None:
                num = json.load(file_object)
    except Exception:
        return None
    else:
        return num


# 保存数字方法
def save_store_num():
    like_num = input('请输入喜欢的数字:')
    # 保存数据地址
    file_path = getRootPath() + '\\test\\python编程-入门\\file\\10\\username.json'
    with open(file_path, 'w') as file_object:
        json.dump(like_num, file_object)
    return like_num


def test():
    # 1. 获取客户信息，看是否存在
    num = get_store_num()
    if num:
        pass
    else:
        # 不存在
        num = save_store_num()

    print('您最喜欢的数字是:' + str(num))


test()
