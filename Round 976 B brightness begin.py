from math import isqrt
t = int(input())
# nums = [list(map(int,input().split(" "))) for i in range(t)]
nums = [int(input()) for i in range(t)]
for i in range(t):
    k = nums[i]
    l,r  = k, 2 * 10**18
    while l < r:
        mid = (l + r) // 2
        if mid - isqrt(mid) < k:
            l = mid + 1
        else:
            r = mid
    print(l)