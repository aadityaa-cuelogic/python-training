ten_things = "Apples Oranges Crows Telephone Light SUgar"

print "Wait there are not 10 things in that lists. Lets Fix that"

stuff = ten_things.split(' ')

more_stuff = ["day", "night", "Songs", "Frisbee", "Corn", "banana", "girl", "boy"]

while len(stuff) != 10:
        next_one = more_stuff.pop()
        print "Adding.. ", next_one
        stuff.append(next_one)
        print "There are now %d itnems.\n" % len(stuff)

print "there we go : ", stuff , "\n"
print "Lets do some things with stuff"

print stuff[1]
print stuff[-1]

print stuff.pop()
print ' '.join(stuff)

print '#'.join(stuff[3:6])
