# 4.5.1 定义元组
import print as print

dimensions = (200, 50)
print(" 第一个元素:", dimensions[0])
# 元组不可修改
for one in dimensions:
    print(one)

# 元组能重新赋值
dimensions = (400, 100)
for one in dimensions:
    print(one)
