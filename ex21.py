def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b

def subtract(a, b):
    print "subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multipling %d * %d" %(a, b)
    return a * b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)


print "Age: %d, Height: %d, Weight: %d" % (age, height, weight)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, 1)))

print "That becomes: ", what, "Can you do it by hand?"
