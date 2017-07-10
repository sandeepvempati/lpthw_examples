from sys import argv

script,filename = argv

print "the file name is: %r" %filename

txt = open(filename,'w+')

print txt.read()

line1 = raw_input("enter some input")

txt.write(line1)

txt.close()

#print txt.readline()

# line1 = raw_input("write something to file")
#
# txt.write(line1)
#
# txt.close()
