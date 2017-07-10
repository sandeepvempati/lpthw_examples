for i in range(int(raw_input())):
    a, b = raw_input().split(" ")
    try:
        print int(a) / int(b)
    except Exception as e:
        print "Error code:",e




