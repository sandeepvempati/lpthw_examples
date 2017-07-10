from sys import argv

script, user_name = argv
prompt = '*'

print "Hi %s I'm the %s script." %(user_name,script)
print "I would like to ask few ques"
print "Do you like me %s" %user_name
likes = raw_input(prompt)

print "where do you lives%s"%user_name
lives = raw_input(prompt)

print "what kind of computer you have:%s"%user_name
computer = raw_input(prompt)


print '''you like %s.you live %s. Your computer %s
''' %(likes,lives,computer)
