# -*- coding: utf-8 -*-

# 输入（提示和传递）的两种方式，raw_input和argv

from sys import argv

script, user_name, age = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of job do you do?"
job = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you are %r years old.  Your job is %r.  You have a %r computer.  Nice.
""" % (likes, lives, age, job, computer)