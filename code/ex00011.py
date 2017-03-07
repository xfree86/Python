# -*- coding: utf-8 -*-

# 一般软件做的事情主要就是下面几条
# 1.接收人的输入。
# 2.改变输入
# 3.打印改变后的输入值

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)

var = raw_input("What's your name?")
print var