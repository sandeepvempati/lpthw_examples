tabby_cat = "\tI'm tabbed in"
persian_cat = "\I'm split\non a line"
backslash_cat = "I'm \\ a\\ cat."

#\t tab \n new line

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "using rper %r."% tabby_cat
print "using sper %s"% tabby_cat
print "\t fd\n \t gf"
print "\njan\nfeb"
print '''\tfs\naa %s'''%"\tstring\nldsk"
