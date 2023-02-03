# 商店--能提供的配料信息
available_toppings = ['A', 'B', 'C', 'D', 'E', 'F']
# 客户--想要的配料信息
requested_toppings = ['A', 'B', 'G']

for requested_VO in requested_toppings:
    if requested_VO in available_toppings:
        print(f"添加配料成功 {requested_VO}")
    else:
        print(f"抱歉，我们无法提供这种配料 {requested_VO}")

print("\n 执行完毕")
