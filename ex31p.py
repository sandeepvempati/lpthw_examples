print "please enter to door 1 or 2"

door = int(raw_input("> "))

if(door == 1):
    bear = int(raw_input("please enter number"))
    if(bear == 1):
        print "danger"
    elif(bear == 2):
        print "saved"
    else:
        print "nothing"
elif(door == 2):
    deer = int(raw_input("please enter the number"))
    if(deer == 1):
        print "deer"
    elif(deer == 3):
        print "second deer"
    elif(deer == 5):
        print "fifth deer"
    else:
        print "no deer"
else:
    print "nothing is matched"
