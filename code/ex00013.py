# -*- coding: utf-8 -*-

# 导入模块，参数，解包，变量

# from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

from sys import argv

script, height, weight = argv
name = raw_input("What's your name? ")
print "The script is called: ", script
print "Your name are: ", name
print "Your height is: ", height
print "Your weight is: ", weight
