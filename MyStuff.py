mystuff = {'apple':'I am apples'}
print mystuff['apple']

def apple():
    print "I am apples!"

x = "Living reflection in a dream"


class MyStuff(object):

    def __init__(self):
        self.x = "changed to -----"

    def apple(self):
        print "I apple"

class Song(object):

    def __init__(a,lyrics):
        a.lyrics = lyrics

    def sing_me_a_song(a):
        for line in a.lyrics:
            print line

happy_bday = Song(["happ to you",
                    "i do fbkdsbfbds",
                    "dfs fdsfsf sdff "])

bulls_on_parade = Song(["thhfkj fsddfj",
                        "fhdskjndfds kfdsldff dffdn"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
