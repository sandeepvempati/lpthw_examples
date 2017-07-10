people = 20
cats = 30
dogs = 15

if people < cats:
    print "too many cats"
if people > cats:
    print "too many people"
if people > dogs:
    print "too many dogs"
if people < dogs:
    print "less dogs"

dogs += 5

if people >= dogs:
    print "equal"
else:
    print "Nope"

a = int(raw_input("enter a"))
b = int(raw_input("enter b"))
c = int(raw_input("enter c"))

if(a>b & a>c):
    print "a is greater"
elif(b>a & b>c):
    print "b is greater"
else:
    print "c is greater"
