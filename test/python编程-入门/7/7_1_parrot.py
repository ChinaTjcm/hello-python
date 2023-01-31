msg = input("请输入信息，我讲为您展示:")
print(msg)

# 练习7-2 : 餐馆订位 　编写一个程序，询问用户有多少人用餐。如果超过8位，
# 就打印一条消息，指出没有空桌；否则指出有空桌。
queryNum = input("请问有多少人用餐？输入数字：")
if int(queryNum) >= 8:
    print("没有空桌")
else:
    print("有空桌")
