from sys import argv

script, user_name, insult = argv
prompt = '> '

print "Hi %s, I'm the %s script, you big %s." % (user_name, script, insult)
print "I'd like to ask you a few questions."
print "Do you like me %s, %s?" % (user_name, insult)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. BTW: You are a total %r!
""" % (likes, lives, computer, insult)

