ten_things = "Apples Oranges Crows Telephone Light Suggar"

print "There are not 10 things in list"

stuff = ten_things.split(' ')
more_stuff = ["day","night","song","fris","corn","banana","girl","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding ..." ,next_one
    stuff.append(next_one)
    print "there are %d items now" %len(stuff)

print "there we go" ,stuff

print "lets do something with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
