tup1 = (1,2,3,4,5,6)
tup2 = (9,10,11,12)
print tup1[1:3] #slicing
tup3 = tup1+tup2
print "adding tupples" ,tup3
#del tup3
#print "tup3 after deleting %r" %tup3
lista = list(tup1)
print "tup to list converting %r" %lista

lista.remove(3)
print lista
