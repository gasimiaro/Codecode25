n = int(input())
d = {}
for _ in range(n):
    name,v=input().split()
    if int(v) not in d:
           d[int(v)] = [name]
    else:
        d[int(v)].append(name)
        d[int(v)].sort()
new = sorted(d, reverse= True)
for key in new:
    for v in d[key]:
        print(v,key)
