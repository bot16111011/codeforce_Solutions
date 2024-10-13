from collections import Counter
t = int(input())
for _ in range(t):
    d = list(map(int,input().split(" ")))
    arr = Counter(list(map(int, input().split(" "))))
    n, x = d[0], d[1]

    mex = 0
    while mex in arr:
        arr[mex] -= 1
        if arr[mex] > 0:
            arr[mex + x] += arr[mex]
        mex += 1
    print(mex)

    