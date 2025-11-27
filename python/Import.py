# from file import name
# print(name)
import file as a
print(a.name,a.age,a.gender)
# from file import *
# print(name,age,gender)
# 如果用from的方法，若两个文件有相同名字的部分，后导入的会覆盖前导入的
# 导入函数不要加括号，只要函数名就好