print "lets try tab new line "
print "\and \t and \n are escapes"

print """\t hi odlfsdljf
        fldsjfjdsfjds
        fdsgkdf;lk;fg
        \nfjdosajlfjslaf
        dfjsa\tdfklsdjf
        kdsf;ksf"""

five = 10-5
print "five is %d" %five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates

start_point = int(raw_input("enter start_point"))
beans,jars,crates = secret_formula(start_point)

print "with a start point %d" %start_point
print "beans %d jars %d crates %d " %(beans,jars,crates)
print "beans %r" %beans

start_point = start_point/10
print "we can do this way new start_point %d" %start_point
print "Now beans %d jars %d crates %d" %secret_formula(start_point)
