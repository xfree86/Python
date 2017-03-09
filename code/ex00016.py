# -*- coding: utf-8 -*-

# close -- 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
# read -- 读取文件内容。你可以把结果赋给一个变量。
# readline -- 读取文本文件中的一行。
# truncate -- 清空文件，请谨慎使用该命令。
# write('stuff') -- 将stuff写入文件。

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "Now The ", filename,
print "that's OK!"
target = open(filename)
print target.read()

print "And finally, we close it."
target.close()
