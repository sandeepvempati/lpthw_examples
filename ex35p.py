from sys import exit

def gold_room():
    print "room is full gold how much you take"

    choice = raw_input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("learn to type number")
    if how_much < 50:
        print "you won"
        exit(0)
    else:
        dead("you greedy")

def bear_room():
    print "bear here"
    bear_moved = False

    while True:
        choice = raw_input(">")

        if choice == "take honey":
            dead("the beer slaps")
        elif choice == "taunt bear" and not bear_moved:
            print "bear moved from door"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("bear pissed off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea"

def cthulhu_room():
    print "here see evil"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("wel that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print why, "good job"
    exit(0)

def start():
    print "you are in dark room"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("stumble")

start()
