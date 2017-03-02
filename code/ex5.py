# -*- coding: utf-8 -*-

# 格式化字符串 (format string)

name = u'徐晶荣'
age = 29 # not a lie
height_inches = 70.079 # inches
height_cm = height_inches * 2.54 # cm
weight_lbs = 176.370 # lbs
weight_kg = weight_lbs * 0.4535923 # kg
eyes = u'棕色'
teeth = u'白色'
hair = u'黑色'

print u"Let's talk about %s." % name
print "He's %.3f cm tall." % height_cm
print "He's %.3f kg heavy." % weight_kg
print "Actually that's too heavy."
print u"He's got %s eyes and %s hair." % (eyes, hair)
print u"His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print u"If I add %d, %.3f, and %.3f I get %.3f." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg
)

print "%+8d" % 10
print "%8d" % 10
print "% X" % 10
print "%2X" % 10
print "%*X" % (2, 10)
print "%04d" % 5
print "%.3f" % 1.2

print round (1.73333)