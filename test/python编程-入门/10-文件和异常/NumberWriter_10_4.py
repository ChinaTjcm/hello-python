import json
from FileReader_10_1 import getRootPath

numbers = {
    "name": "cm",
    "age": "30",
    "area": "天津"
}

# 相对路径，取项目根目录
root_path = getRootPath()
file_path = root_path + "\\test\\python编程-入门\\file\\10\\numbers.json"
# 1. 写入 json 数据
with open(file_path, 'w') as file_object:
    json.dump(numbers, file_object)

result = ''
# 2. 读取 json 数据
with open(file_path) as file_object:
    result = json.load(file_object)
print(result)
