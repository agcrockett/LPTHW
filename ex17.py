from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file).read()
#indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w')#.write(in_file)
out_file.write(in_file)


# print "Are both files %s and %s closed? " % (from_file, to_file)
# print "%s : %r and %s : %r" % (from_file, in_file.closed, to_file, out_file.closed)
# print "Alright, all done."

#out_file.close()
#in_file.close()
