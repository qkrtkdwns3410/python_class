# a = [[chr(ord('A')+i),0] for i in range(26)]
# b=input().upper()
# for i in b:
#     a[ord(i)-ord('A')][1]+=1
# a=sorted(a,key=lambda x: -x[1])
# # print(a)
# if a[0][1]==a[1][1]:
#     print('?')
# else:
#     print(a[0][0])
#
#
# from collections import Counter
#
# a=input().upper()
# b= Counter(a).most_common()
# print(b)
# if b[0][1]==b[1][1]:
#     print('?')
# else:
#     print(b[0][0])
# from collections import defaultdict
#
# d = defaultdict(list)
# a=input().upper()
#
# for i in a:
#     d[i].append(1)
# blist=[]
# for i,v in d.items():
#     blist.append([i,sum(v)])
# print(blist)
#
# a=list(input())
# for i in range(len(a)):
#     if i%2==0:
#         print(a[i],end='')
#
# a=input()
# for i,v in enumerate(a):
#     if i%2==0:
#         print(v,end="")
# suma=0
# a= list(map(str,input().split()))
# print(len(a))
# for i in a:
#     suma+=len(i)
# print(suma+len(a)-1)
# n=int(input())
# for i in range(1,n+1):
#     print("{}    {}    {}    {}".format(i,oct(i)[2:],hex(i)[2:],bin(i)[2:]))
#from collections import Counter
# a=list(map(int,input().split()))
# b=Counter(a).most_common()
# print(b)
# for i in b:
#     if i[1]==1:
#         print(i[0])
#suma=0
# a =int(input())
# for i in range(1,a):
#     suma+=i
# print(suma)
n=int(input())
alist=[]
for i in range(n):
    alist.append(list(map(str,input().split())))
a=input()
for i in alist:
    if i[0] == a:
        b=[float(i) for i in i[1:]]
        print("%.2f" %(sum(b)/len(b)))


























