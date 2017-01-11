def cheese_and_crackers(cheese_count, boxs):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes" % boxs
    print "man thats enough\n \n"

print "We can just give function numbers direcly"
cheese_and_crackers(100, 10)

print "Or we can use vars from our script"
cheeseAmt = raw_input("Enter chees count : ")
boxes = raw_input("Enter box count : ")

cheese_and_crackers(int(cheeseAmt), int(boxes))
