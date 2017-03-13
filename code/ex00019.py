# -*- coding: utf-8 -*-

# 函数的变量关系，传递给函数的参数可以是数值、有值的变量、运算结果

# 定义函数cheese_and_crackers()，传递变量1和变量2
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # 打印字符串，格式化字符串%d（有符号整数），传递变量值
    print "You have %d cheeses!" % cheese_count
    # 打印字符串，格式化字符串%d（有符号整数），传递变量值
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # 打印字符串 
    print "Man that's enough for a party!"
    # 打印字符串，转义字符\n（换行）
    print "Get a blanket.\n"

# 打印字符串
print "We can just give the function numbers directly:"
# 调用cheese_and_cracker()函数，传递数值20、30两个参数。
cheese_and_crackers(20, 30)

# 打印字符串
print "OR, we can use variables from our script:"
# 给变量amount_of_cheese赋值为10
amount_of_cheese = 10
# 给变量amount_of_crackers赋值为50
amount_of_crackers = 50

# 调用cheese_and_cracker()函数，传递有值的变量1、有值的变量2两个参数。
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 打印字符串
print "We can even do math inside too:"
# 调用cheese_and_cracker()函数，传递10+20的运算结果、5+6的运算结果两个参数。
cheese_and_crackers(10 + 20, 5 + 6)

# 打印字符串
print "And we can combine the two, variables and math:"
# 调用cheese_and_cracker()函数，传递变量1+100的运算结果、变量2+1000的运算结果两个参数。
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def ten(a,b,c):
    print "Num a is: %d" % a
    print "Num b is: %d" % b
    print "Num c is: %d" % c

print "The first method: "
ten(1, 2, 3)

print "The second method: "
ten(2, 3, 4)

print "The third method: "
a = 3
b = 4
c = 5
ten(a, b, c)

print "The fourth kind of method: "
a = 4
b = a + 1
c = b + 1
ten(a, b, c)

print "The 5th kind of method: "
a = 3
b = 4
c = 5
ten(a+2, b+2, c+2)

print "The 6th kind of method: "
a = 6
ten(a, a+1, a+2)

print "The 7th kind of method: "
a = 7
b = 1
ten(a, a + b, a + 2)

print "The 8th kind of method: "
a = 10
ten(a - 2, a - 1, a)

print "The 9th kind of method: "
ten(5 + 4, 2 * 5, 11)

print "The 10th kind of method: "
a = 10
b = input("Please input 11 \n> ")
c = 12
ten(a, b, c)
