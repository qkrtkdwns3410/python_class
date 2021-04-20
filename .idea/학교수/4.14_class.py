tot = 0
for a in range(11):
    tot+=a
print(tot,a)

tot =0
for a in range(1,11,2):
    tot+=a
print(tot,a)

tot=0
for a in range(11):
    if a%2==0:
        continue
    tot+=a
print(a,tot)

sum=0
for i in range(1,11):
    if i%2==0:
        continue
    else:
        sum+=i
print(sum)


