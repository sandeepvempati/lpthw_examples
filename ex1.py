



def find_last(s, t):
    last_pos = -1
    while True:
        pos = s.find(t, last_pos+1)
        print pos
        if pos == -1:
            return last_pos
        last_pos = pos

print find_last('yuhjhhjaaaa', 'a')


def big(a,b):
    if a>b:
        return a
    else:
        return b

print big(3,5)
