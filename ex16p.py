from sys import argv

script,filename = argv

print "we are going to erase %r."%filename
print "If you don't want that hit ctrl+c."
print "If you do want hit return"

raw_input("?")

print "opening the file..."
target = open(filename,'w') # w opens a file if it there else creates a new file

print "Truncating the file. Bye!"
target.truncate()

print "Now enter 3 lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 4: ")

print "I am going to write this to file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it"
target.close()
