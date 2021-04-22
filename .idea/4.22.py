alist =[-1 for i in range(26) ]
a = input()
for i,v in enumerate(a):
    if a[i-1]==a[i]:
        continue
    else:
        alist[ord(v)-ord("a")]=i
for i in alist:
    print(i,end=' ')