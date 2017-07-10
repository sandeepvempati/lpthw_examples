x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and who know %s"%(binary,do_not)
print x
print y

print "I said: %r." %x
print "I said: %s." %x
print "I also said:%s" %y
hilarious = False
joke_evaluation = "funny? %r"
print joke_evaluation % hilarious

w = "This is left of string"
e = "string on right side"

print w+e
