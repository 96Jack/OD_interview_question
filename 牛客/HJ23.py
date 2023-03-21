s = list(input())
s_dict = {x:s.count(x) for x in s}

min_v = min(s_dict.values())
for k,v in s_dict.items():
    if v == min_v:
        while True:
            try:
                s.remove(k)
            except:
                break
        print(s)
