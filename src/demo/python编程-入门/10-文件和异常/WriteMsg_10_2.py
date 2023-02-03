from FileReader_10_1 import getRootPath

root_path = getRootPath()
file_path = f"{root_path}\\test\\python编程-入门\\file\\10\\programming.txt"

# 第二个实参
# （'w' ）告诉Python，要以写入模式 打开这个文件。
# 打开文件时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或读写模式 （'r+' ）。
with open(file_path, 'w') as file_object:
    file_object.write('我是cm,我爱做项目')

print(f'写入成功，文件地址为：{file_path}')
