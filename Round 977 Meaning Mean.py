t = int(input())
for _ in range(t):
    input()
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    while len(arr)>1:
        a = arr.pop()
        b = arr.pop()
        arr = arr + [(a+b)//2]
    print(arr[0])