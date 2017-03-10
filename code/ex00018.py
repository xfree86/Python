# -*- coding: utf-8 -*-

# 命名，变量，代码，函数
# 函数注意事项
#
# 1.函数定义是以 def 开始的吗？ （是）
# 2.函数名称是以字符和下划线 _ 组成的吗？（和变量命名规则相同。不能以数字开头，并且只能包含字母数字和下划线。）
# 3.函数名称是不是紧跟着括号( ？ （是）
# 4.括号里是否包含参数？多个参数是否以逗号隔开？ （可有可无，是）
# 5.参数名称是否有重复？（不能使用重复的参数名）
# 6.紧跟着参数的是不是括号和冒号 ):  （是）
# 7.紧跟着函数定义的代码是否使用了4个空格的缩进(indent)？ （是）
# 8.函数结束的位置是否取消了缩进("dedent")？ （是）
#
# 运行一个函数时，记得检查下面的点：
# 
# 1.调运函数时是否使用了函数的名称？ （是）
# 2.函数名称是否紧跟着 ( ？ （是）
# 3.括号后有无参数？多个参数是否以逗号隔开？ （可有可无，是）
# 4.函数是否以 ) 结尾？ （否）
#
# ‘运行函数(run)’、‘调用函数(call)’、和‘使用函数(use)’是同一个意思

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
