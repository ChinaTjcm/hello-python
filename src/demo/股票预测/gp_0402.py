from jqdatasdk import get_factor_values
import jqdatasdk

jqdatasdk.auth('13652089358', 'Charminglife0313')


# 程序运行 demo
# https://www.joinquant.com/research?target=research&url=/user/59556498210/notebooks/Untitled.ipynb?kernel_name=python3

# 导入函数库
from jqfactor import get_factor_values
# 取值函数
factor_data = get_factor_values(securities=['000001.XSHE'], factors=['BR'], start_date='2012-04-01', end_date='2022-02-01')
print(factor_data['BR'])
# 获取因子Skewness60(个股收益的60日偏度)从 2017-01-01 至 2017-03-04 的因子值
# factor_data = get_factor_values(securities=['000001.XSHE'], factors=['BR'], start_date='2017-01-01', end_date='2017-03-04')
# 查看因子值
# print(factor_data)
# factor_data['Skewness60']