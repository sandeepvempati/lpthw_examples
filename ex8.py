def fix_machine(a,b):
    i = 0
    while len(a):
        b[i] == a.find('b[i]')
        print b[i]
        i = i+1
        return b
    return a

print fix_machine('san','dfdddd')




def sum_digit(n):
    x=str(n)
    temp = 0
    for a in x:
        temp += int(a)
    return temp

print sum_digit(12358)

def sum_dig(p):
    x = p%10
    y = p//10
    z = y%10
    p = y//10
    q = p%10
    return x+z+q

print sum_dig(1243888)
