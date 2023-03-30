str_bin = bin(int(input()))
str_bin = str_bin[2::].rjust(32, "0")
ip = [str(int(str_bin[i*8:(i+1)*8],2)) for i in range(0,4)]
print(".".join(ip))
