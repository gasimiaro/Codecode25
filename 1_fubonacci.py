def fubonacci(n):
    l = [0,1]
    if 0<=n<=1:
        return n
    for i in range(2,n+1):
        l.append(l[-1]+l[-2])
    return l[-1]
   
n = int(input())
print(fubonacci(n))
        
