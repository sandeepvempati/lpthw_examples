# "Tuples and its built in functions working"
#
# x = (1,2,3,4,5,6)
#
# i = 0
# for i in x:
#     print "Tuple x[%r] is %r "  %(i-1,i)


"Working with Lists and built in functions"

x = [1,2,500,[3,4,"inside"],323,123,[1,34,5,[1,243,"deep",23]]]
y = [1000,"a"]

print tuple(x)
x[3] = 12
print max(y)
print max(x)
print min(x)
print len(x)

list1 = [1,2,3,4,5,6,7,8]
list2 = ["only","strings","no","other"]
list3 = [8,9,"ins","123",9,[4,8,97]]
list4 = [1,2,3,4,5]
list1.append(list4)
list1.extend(list4)
list1.insert(1,32)
print "appending lists %r" %list1
print "count of list1 %r" %list1.count(2)
print "index() in the list1",list1.index(32)
print "comparing lists " , cmp(list1,list4)
list2[2] = 2001
list4.remove(5)
print "after removing list 4" ,list4
list4.reverse()
print "reversing the list4 " , list4
list4.sort()
print "list after sorting" ,list4

print "list1+list2 is %r" %(list1+list2)
print "list 2 %r" %list2
#del list2 #deleting list
del list1[4]
print "list 1 afer deleting %r" %list1

#print "list 2 after deleting %r" %list2

print "indexing ", list3[len(list2)]
print "slicing ", list1[2:] #fetching the data
print "slicing from [2:5] is %r" %list1[2:5]
print max(list1)
print min(list3)
# def change(list1):
#     return x.append(list1)
#
# list1 = raw_input("enter list please")
# print change(list1)
