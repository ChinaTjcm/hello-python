alien_0 = {"color": "green", "points": 5}
print(alien_0)

# 增加位置属性
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 移除位置属性
del alien_0['x_position']
del alien_0['y_position']
print(alien_0)

# 方法get() 的第一个参数用于指定键
getColor = alien_0.get('color', '值不存在时的结果')
getPosition = alien_0.get('x_position', '值不存在时的结果')
print(getColor)
print(getPosition)
