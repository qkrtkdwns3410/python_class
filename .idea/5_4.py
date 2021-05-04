# n = int(input())
# alist = list(map(int,input().split()))
# alist = list(set(alist))
# alist.sort()
# print(alist[-2])
# print(sorted(alist)[-2])
#
# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
#
# alist=[]
#
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k !=n:
#                 alist.append([i,j,k])
# print(alist)
# n=int(input())
# alist=[]
# for i in range(n):
#     blist=list(map(str,input().split()))
#     if blist[0]=='insert':
#         alist.insert(int(blist[1]),int(blist[2]))
#     elif blist[0]=='print':
#         print(alist)
#     elif blist[0]=='remove':
#         alist.remove(int(blist[1]))
#     elif blist[0]=='append':
#         alist.append(int(blist[1]))
#     elif blist[0]=='sort':
#         alist.sort()
#     elif blist[0]=='pop':
#         alist.pop()
#     elif blist[0]=='reverse':
#         alist.reverse()
# n = int(input())
# alist=[]
# blist=[]
# for i in range(n):
#     a = input()
#     b = float(input())
#     alist.append([a,b])
#     blist.append(b)
# blist=list(set(blist))
# blist.sort()
# c=blist[1]
# alist.sort()
# for i in alist:
#     if i[1]==c:
#         print(i[0])
# n=int(input())
# alist= list(map(str,input().split()))
#
# count=0
# for i in alist:
#     if i==i[::-1]:
#         count+=1
# if count>0:
#     print('True')
# else:
#     print('False')
# a,b = list(map(int,input().split()))
# blist=[]
# for i in range(a):
#     alist=list(map(int,input().split()))
#     blist.append(alist)
# k=int(input())
#
# blist=sorted(blist,key=lambda x:x[k])
#
# clist=[]
# for i in blist:
#     sub=[]
#     for j in i:
#         sub.append(str(j))
#     clist.append(sub)
#
# #print(clist)
# for i in clist:
#     print(" ".join(i))
# a = input()
# upper = []
# lower = []
# Num = []
# Even = []
# Odd = []
# for i in a:
#     if i.isalpha():
#         if i.isupper():
#             upper.append(i)
#         else:
#             lower.append(i)
#     elif i.isdigit():
#         if int(i) % 2 == 0:
#             Even.append(i)
#         else:
#             Odd.append(i)
# upper.sort()
# lower.sort()
# Even.sort()
# Odd.sort()
#
# b = lower + upper +  Odd + Even
# print("".join(b))
# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return (check(n - 2))
# n=int(input("Enter number:"))
# if(check(n)==True):
#       print("Number is even!")
# else:
#       print("Number is odd!")
#
# a = int(input())
#
# if a%2==0:
#     print('Number is even!')
# else:
#     print('Number is odd!')
# a=input()
# b=input()
# count=0
# for i in a:
#     if i==b:
#         count+=1
# print(count)
# def check(string,ch):
#     if not string:
#         return 0
#     elif string[0]==ch:
#         return 1+check(string[1:],ch)
#     else:
#         return check(string[1:],ch)
#
# a=input()
# b=input()
# print(check(a,b))

# a = int(input())
#
# def fibonacci(n):
#     if(n<=1):
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(a):
#     print(fibonacci(i),end=' ')
#
# n=int(input())
# alist=[0,1]
# for i in range(2,n):
#     alist.append(sum(alist[-2:]))
# print(alist)

# n=int(input())
# count=1
# for i in range(1,n+1):
#     count*=i
# print(count)

# def factorial(n):
#     if(n <= 1):
#         return 1
#     else:
#         return(n*factorial(n-1))
#
# a=int(input())
# print(factorial(a))

def sum_arr(arr,size):
    if(size==0):
        return 0
    else:
        return arr[size-1]+sum_arr(arr,size-1)

n=int(input())
alist=[i for i in range(1,n+1)]
print(sum_arr(alist,len(alist)))
