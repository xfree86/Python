# -*- coding: utf-8 -*-

# 读文件 用argv和raw_input()来实现文件名称可变

# 引入argv模块
# from sys import argv

# argv解包
# script, filename = argv

print "Type the filename:"
filename = raw_input("> ")

# 给txt变量赋值为open
txt = open(filename)

# 打印字符串，其中%r字符格式变量filename的值
print "Here's your file %r:" % filename
# 打印txt变量的read函数的结果
print txt.read()
txt.close()

# 打印字符串
print "Type the filename again:"
# 给file_again变量赋值为raw_input()用户输入，提示符为> 
file_again = raw_input("> ")

# 给txt_again变量赋值为open(file_again),打开/读取一个文件
txt_again = open(file_again)

# 打印txt_again变量的read函数的结果
print txt_again.read()
txt_again.close()

# print txt_again.read()
# close()后再调用txt_again变量就会报错：
#
# Traceback (most recent call last):
#   File ".\ex00015.py", line 34, in <module>
#     print txt_again.read()
# ValueError: I/O operation on closed file