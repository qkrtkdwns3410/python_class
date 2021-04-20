# a,b =list(map(str,input().split()))
# counta=0
# countb=0
# for i in range(1,10):
#     if str(i)*3 in a:
#        counta+=1
# for j in range(1,10):
#     if str(j)*2 in b:
#         countb+=1
# if counta>0 and countb>0:
#     print(1)
# else:
#     print(0)
#
#
# n =int(input())
# suma=0
# for i in range(1,n+1):
#     for j in str(i):
#         suma+=int(j)
# print(suma)
#
# a =int(input())
# b=int(input())
#
# d={}
# d.update({a:b})
# print(d)
#
#
# from collections import defaultdict
# a="abcdefeaadb"
# d=defaultdict(list)
# for i in a:
#     d[i].append(1)
# print(d)
# for i,v in d.items():
#     print(i,sum(v))
#
# alist=[[chr(ord("a")+i),0 ] for i in range(26)]
# print(alist)
# for i in a:
#     alist[ord(i)-ord("a")][1]+=1
# print(alist)
#
# from collections import Counter
# f=Counter(a).most_common(2)
# print(f)
#
#

# n=int(input())
# suma=0
# sumb=0
# sumc=0
# for i in range(1,n+1):
#     suma+=i**2
#     sumb+=i
# print(abs(suma-sumb**2))
# n=int(input())
# alist=[]
# counta=0
# while (n >  counta):
#     for i in range(2,200000):
#         for j in range(2,i//2+1):
#             if i %j==0:
#                 break
#         else:
#             alist.append(i)
#             counta+=1
#             if counta==10001:
#                 break
#
# print(alist[-1])



# import time
# def isPrime(n):
#     if n < 2: return "Neither prime, nor composite"
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def nthPrime(n):
#     numberOfPrimes = 0
#     prime = 1
#
#     while numberOfPrimes < n:
#         prime += 1
#         if isPrime(prime):
#             numberOfPrimes += 1
#     return prime
# starttime=time.time()
# print(nthPrime(10001))
# endtime=time.time()
# print(endtime-starttime)


# n =int(input())
# for a in range(1,n+1):
#     for b in range(1,a):
#         c=(a**2+b**2)**0.5
#         if c%1==0 and a+b+c==n:
#             print(int(a*b*c))
#
# import calendar
# a,b =list(map(int,input().split()))
# arrList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# day=calendar.weekday(2007,a,b)
# print(arrList[day])

N=int(input())
for i in range(N):
    if i%2==0:
        print("1"*(N-i))
    else:
        print("0"*(N-i))












