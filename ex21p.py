def add(a,b):
    print "add %d + %d" %(a,b)
    return a+b

def sub(a,b):
    print "sub %d - %d" %(a,b)
    return a-b

def mul(a,b):
    print "mul %d * %d"%(a,b)
    return a*b

def div(a,b):
    print "div %d / %d" %(a,b)
    return a/b

a = float(raw_input("enter a value"))
b = float(raw_input("enter b value"))


print add(a,b)

# print add(2,8)
# print sub(5,1)
# print mul(6,7)
# print div(8,6)
# print add(5,sub(90,mul(5,div(10,2))))
#
# print 10 - sub(6,3)
# print 5 + add(5,6)
