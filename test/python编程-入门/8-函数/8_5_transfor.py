def make_pizza(size, *toppings):
    """打印顾客点的所有配料。"""
    print(f"制作 {size} 寸披萨，需要如下原料: {toppings}")
    for ONE in toppings:
        print(f"-{ONE}")


make_pizza(7, 'aaa')
make_pizza(9, 'aaa', 'bbb', 'ccc')
