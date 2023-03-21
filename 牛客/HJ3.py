while True:
    try: 
        n ,s = int(input()),set()
        for i in range(n):
            m = int(input())
            s.add(m)
        for i in sorted(s):
            print(i)
    except:
        break
    
