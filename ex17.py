from sys import argv as cmdio
from os.path import exists

script, from_file, to_file = cmdio

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "Does the output file exists ? %r " % exists(to_file)
print "Ready, hit Return to continue, Ctrl-C to abort"
raw_input('>')

out_file = open(to_file, 'w')
out_file.write(indata)

print "Writing Done!"

out_file.close()
in_file.close()
