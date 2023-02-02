# pip 调整安装目录 https://www.jb51.net/article/253222.htm


# 异常学习
print('给我 2 个数字，我去执行除法操作')
print('输入 q 终止程序')
while True:
    try:
        first_num = input("\n第一个数字:")
        if first_num == 'q':
            break
        second_num = input("\n第二个数字:")
        if second_num == 'q':
            break
    except ZeroDivisionError:
        print('除数不能为 0 ！')
    else:
        result = int(first_num) / int(second_num)
        print('结果是：' + str(result))
