current_number = 1

# 当前是 1,<=5 自增 1,超过 5 停止打印
while current_number <= 5:
    current_number += 1
    print(current_number)

test_num = 1
# 学习 break 、 coutinue
while test_num <= 10:
    test_num += 1
    if test_num == 8:
        print('break', test_num)
        break
    elif test_num % 3:
        print('continue', test_num)
        continue
