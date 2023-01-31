def show_msg(datas):
    """打印每条数据"""
    while datas:
        current = datas.pop()
        print(f'每条信息如：{current}')
        print(f'删除成功，打印原始数据： {datas}')


unprinted_designs = ['cm', '67', '77']


"""
    保留原始数据
"""
show_msg(unprinted_designs[:])
print(unprinted_designs)

"""
    不保留原始数据
"""
show_msg(unprinted_designs)
print(unprinted_designs)
