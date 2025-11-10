n,m = map(int,input().split())
maxi = 0
index=1
for i in range(n):
    l = [int(i) for i in input().split()]
    nmax = sum(l)
    if nmax> maxi:
        maxi = nmax
        index = i+1
print(index,maxi)
