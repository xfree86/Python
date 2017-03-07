# -*- coding: utf-8 -*-

# 转义符号\反斜杠 back-slash

print "I am 6'2\" tall." # 将字符串中的双引号转义
print 'I am 6\'2" tall.\n' # 将字符串中的单引号转义

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ %r but %s cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat % ("bl'a\nc\rk", "g'o\no\vd")
print fat_cat

# 一小段有意思的代码：
# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i,
