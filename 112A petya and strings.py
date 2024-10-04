t=int(input())
words = []
for i in range(t):
    w = input().strip()
    words.append(w)
for i in range(t):
    w = words[i]
    if len(w)>10:
        w=w[0]+ str(len(w)-2)+w[-1]
    print(w)