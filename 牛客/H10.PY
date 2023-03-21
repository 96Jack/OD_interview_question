import sys
import re
while True:
    try:
        j = []
        inval = sys.stdin.readline().split(';')
        initx = 0
        inity = 0
        for i in inval:
            if i[0] == 'A':
                initx -= int(i[1:])
            if i[0] == 'D':
                initx += int(i[1:])
            if i[0] == 'W':
                inity += int(i[1:])
            if i[0] == 'S':
                inity -= int(i[1:])
            else:
                continue
            j.append(i)
        print(j)
        print(str(initx) + ',' + str(inity))
    except:
        break