dict = {'name':"sandeep", 'age':24, 'class' : 20,2:22,'list':[1,2,3]}
dict1 = {'name1':"sanffasd",23:65}
#dict['lastname'] = "san"
dict2 = {'name':"sandeep", 'age':24, 'class' : 20,2:22,'list':[1,2,3]}
# del dict['name'] # clears only particular field
# dict.clear() #clear all the values from dict
# del dict # deletes entire dict

print dict1
print dict

print "comparing two dictionaries" ,cmp(deict,dict1)
print "comparing two dictionaries" ,cmp(dict,dict2)
print "comparing two dictionaries" ,cmp(dict1,dict2)

print " lenth of dict" ,len(dict)
print str(dict)
print type(dict)

dict4 = dict1.copy()
#dict5 = dict1.deepcopy()

print "dict4 is " ,dict4
print "dict items" ,dict.items()
print "dict keys" ,dict.keys()
print "dict has keys" ,dict.has_key('name')
print "dict values" ,dict.values()

dict5 = {'name':"san"}
dict6 = {2:44}
dict5.update(dict6)
print "dict update adding" , dict5

print "dict get key give default value if value is not there" ,dict5.get('last',"def")
