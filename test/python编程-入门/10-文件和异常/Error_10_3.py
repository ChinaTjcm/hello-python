#
from decimal import Decimal, InvalidOperation

print("程序将执行 2 个数的加法")
print("非法字符会报异常\n")
num_1 = input(" 请输入第 1 个数字:")
num_2 = input(" 请输入第 2 个数字:")

try:
    # 引入高精度计算
    result = Decimal(num_1) + Decimal(num_2)
except (ValueError, InvalidOperation):
    # 捕获多异常 https://www.ycpai.cn/python/mph7ePQH.html
    print('输入有误，请输入纯数字')
except Exception:
    print('过于宽泛的捕获未知异常')
else:
    print('求和结果为:' + str(result))
