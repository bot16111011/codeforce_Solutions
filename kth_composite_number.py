p = [2, 3, 5, 7, 11, 13]
k = 9999
i = 4
def isprime(n):
    if n%2==0:
        return False
    if n%3==0:
        return False
    for i in range(5,n//2+1):
        if n%i==0:
            return False
    return True
def isdiv(n):
    for i in p:
        if n%i==0:
            return True
    return False
while k!=0:
    x = isprime(i)
    if not x:
        if not isdiv(i):
            print(i)
            k-=1
    i+=1
print(i)
