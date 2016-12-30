people = 20
cats = 30
dogs = 15

if people < cats :
    print "Too many cats!"
elif people > cats :
    print "Not too many cats!"
else:
    print "Cant tell you!!"
if people < dogs :
    print "Too many dogs"
elif people > dogs :
    print "Not too many dogs"
else :
    print "Still cant decide!!!"

dogs += 5
if people >= dogs :
    print "People >= dogs"
else:
    print "People < dogs"
