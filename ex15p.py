from sys import argv

script,filename = argv

txt = open(filename)



print "Here is your file:%s "%filename
print txt.read()



filename_again = raw_input("enter file name again: ")

text_again = open(filename_again)

print "reading file again"
print text_again.read()
