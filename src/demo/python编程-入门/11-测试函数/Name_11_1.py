from NameFunction_11_1 import get_formatted_name

print('执行程序，输入 q 取消程序执行')

while True:
    first = input('请输入姓:')
    if first == 'q':
        break
    last = input('请输入名:')
    if last == 'q':
        break

    format_name = get_formatted_name(first, last)
    print(f"姓名输出结果：{format_name}")
