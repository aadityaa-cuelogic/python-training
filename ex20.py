from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(line_cnt, f):
    print line_cnt, f.readline()
current_file = open(input_file)

print "Print all file"
print_all(current_file)

print "Rewind file pointer"
rewind(current_file)

print "First 3 lines"
print_a_line(1, current_file)
print_a_line(1+1, current_file)
print_a_line(1+2, current_file)
