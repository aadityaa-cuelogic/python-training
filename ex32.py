the_count = [1,2,3,4,5]
fruits = ['apple','banana','grapes', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count list : %d" % number
for fruit in fruits:
    print "This is fruit list : ",  fruit
for i in change:
    print "This is change list : ", i

elements = ['a', 'b', 3]
elements.append(range(-1, 6))
# for i in range(-1, 6):
#     print "Adding ",i," to the elements list"
#     elements.append(i)

for i in elements:
    print "Elements has :",i
