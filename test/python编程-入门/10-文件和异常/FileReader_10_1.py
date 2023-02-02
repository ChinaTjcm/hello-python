import os

# 获取项目根目录
def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find('hello-python') + len('hello-python')]
    return rootPath


# 当前文件的路径
print(' 当前文件的路径: ' + os.path.abspath(os.path.dirname(__file__)))

# 绝对路径
# git 地址本地路径
# D:\gitData\python\hello-python\test\python编程-入门\file
with open('D:\\gitData\\python\\hello-python\\test\\python编程-入门\\file\\pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# 相对路径，取项目根目录
root_path = getRootPath()
file_path = root_path + "\\test\\python编程-入门\\file\\pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

