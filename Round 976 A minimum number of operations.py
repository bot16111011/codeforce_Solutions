t = int(input())
nums = [list(map(int,input().split(" "))) for i in range(t)]
for i in range(t):
    n, k = nums[i][0], nums[i][1]
    if n == 0:
        print(0)
        continue
    if k == 1:
        print(n)
        continue
    ans = 0
    while n>0:
        ans += n % k
        n = n // k
    print(ans)