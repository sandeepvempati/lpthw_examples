from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "File copying from %s to %s" %(from_file,to_file)

txt = open (from_file)
fromfile_data = txt.read()

print "input data length %r"%len(fromfile_data)
print "wheather file exists %r" %exists(to_file)

tofile_txt = open(to_file,'w')
tofile_txt.write(fromfile_data)

print "all done"

tofile_txt.close()
txt.close()
