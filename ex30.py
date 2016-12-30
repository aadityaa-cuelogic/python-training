print "Choose door #1 or #2 ?"

door = raw_input('>')
if door == '1':
    print "There is gold chasel in room. What you wanna do ?"
    print "1. Stole gold chasel"
    print "2. Earn gold chasel"

    bear = raw_input('>')

    if bear == "1":
        print "You are a theif!!!"
    elif bear == "2":
        print "You are a winner!!!"
    else:
        print "You choose wrong option!!!"
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
