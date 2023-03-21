s = input()
def less_8(s):
    zero_list = ["0" for i in range(8-len(s))]
    zero_str = "".join(zero_list)
    print(s+zero_str)

n = len(s)
if len(s) < 8:
    less_8(s)
else:
    if len(s)%8==0 :
        print(s[0:1:8])

