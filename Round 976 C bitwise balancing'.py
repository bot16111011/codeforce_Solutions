t = int(input())
hash = {"110":"1", "001":"1", "111":"0", "010":"0", "101":"0", "000":"0"}
for _ in range(t):
    b,c,d = map(lambda x: bin(int(x))[2:], input().split(" "))
    maxl = max(len(d),len(b),len(c))

    b = "0"*(maxl-len(b))+b
    c = "0"*(maxl-len(c))+c
    d = "0"*(maxl-len(d))+d

    res = []
    for i in range(maxl):
        x = b[i] + c[i] + d[i] 
        if x in hash:
            res.append(hash[x])
        else:
            res = ["-1"]
            break
    print(int("".join(res),2))