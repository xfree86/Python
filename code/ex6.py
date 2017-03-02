# -*- coding: utf-8 -*-

# 大量的字符串、变量、简写的变量和格式化字符

# 给变量x赋值字符串，%d格式化字符调用后面的数字10
x = "There are %d types of people." % 10

# 给变量binary赋值字符串
binary = "binary"

# 给变量do_not赋值字符串
do_not = "don't"

# 给变量y赋值字符串，两个%s格式化字符调用后面的变量binary和变量do_not
# 字符串包含字符串
y = "Those who know %s and those who %s." % (binary, do_not)

# 打印变量x的值
print x

# 打印变量y的值
print y

# 打印字符串，%r格式化字符调用变量x的值，调用后用单引号引用
# 字符串包含字符串
print "I said: %r." % x

# 打印字符串，%s格式化字符调用变量y的值
# 字符串包含字符串
print "I also said: '%s'." % y

# 给变量hilarious赋值布尔值False(假)
hilarious = False

# 给变量joke_evaluation赋值字符串，%r是格式化字符，但该语句后未跟随%符号和被调用值
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印变量joke_evaluation的值，但在打印前传送被调用值（这里是hilarious变量）给变量joke_evaluation中的%r格式化字符
# 字符串包含字符串
print joke_evaluation % hilarious

# 给变量w赋值字符串
w = "This is the left side of..."

# 给变量e赋值字符串
e = "a string with a right side."

# 打印变量w和e合并后的值
print w + e