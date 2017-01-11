def print_two(*args):
    arg1, arg2 = args
    print "arg1 : %r , arg2 : %r " % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1 : %r , arg2 : %r " % (arg1, arg2)

def print_one(arg1):
    print "arg1: ", arg1

def print_none():
    print "Nothing to print"

print_two("Good", "Day")
print_two_again("Helo", "again")
print_one(100)
print_none()
