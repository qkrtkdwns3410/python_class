# # num = int(input())
# # winlist=[]
# # for i in range(num):
# #     x=int(input())
# #     winlist.append(x)
# #
# #
# # T = [[0 for i in range(2)] for j in range(num+1)]
# #
# # for i in range(1, num+1):
# #     T[i][0] = max(T[i-1])
# #     if i > 1:
# #         T[i][1] = max(T[i-2][0] + winlist[i-1] + winlist[i-2], T[i-1][0] + winlist[i-1])
# #     else:
# #         T[i][1] = winlist[i-1]
# #
# #
# #
# # print(str(max(T[num])))
# # import math
# # from itertools import combinations
# # n =int(input())
# # for i in range(n):
# #     a,b =list(map(int,input().split()))
# #     print(math.factorial(b)//math.factorial(a)//math.factorial(b-a))
# #     blist=[i for i in range(b)]
# #     for j in range(1,b+1):
# #         comb=combinations(blist,j)
# #         for k in comb:
# #             print(k)
#
# # print("\"Hello! I\'m a student\"")
# # print("I like playing game.")
#
#
# # print(input())
#
# # a,b =list(map(int,input().split()))
# # print(a*b//2)
#
# # a =int(input())
# #
# #
# # if a%2 ==0:
# #     print(0)
# # else:
# #     print(1)
# #
# #
# # a =int(input())
# # if a>=30:
# #     print(1)
# # else:
# #     print(0)
# #
# #
# #
# # a,b =list(map(int,input().split()))
# # print(max(a,b))
#
# #
# # a=int(input())
# # print(a+2,a+4)
#
# # a=int(input())
# # for i in range(1,a+1):
# #     print(i)
#
#
# # from collections import Counter
# # a=int(input())
# # n=[]
# # counta=0
# # countb=0
# # for i in range(a):
# #     n.append(input())
# #
# # c=Counter(n).most_common()
# # # print(c)
# # print(c[0][0])
#
# # for i in range(a):
# #     if n[i]=='A':
# #         counta+=1
# #     elif n[i]=='B':
# #         countb+=1
# #     else:
# #         pass
# # if counta > countb:
# #     print('A')
# # else:
# #     print('B')
#
# # from collections import Counter
# # n=int(input())
# # alist=[]
# # for i in range(n):
# #     a=input()
# #     alist.append(a)
# # b=Counter(alist)
# # for i,v in b.items():
# #     print(i,v)
# # print(b)
# # # print(b[0][0])
# #
# # a,b=list(map(int,input().split()))
# # Sum=0
# #
# # if a==0:
# #     for i in range(1,b+1):
# #         if i %2==0:
# #             Sum+=i
# # elif a==1:
# #     for i in range(1,b+1):
# #         if i%2!=0:
# #             Sum+=i
# #
# # print(Sum)
# #
# #
# # a, b = list(map(int, input().split()))
# # suma = 0
# # sumb = 0
# # for i in range(1, a + 1):
# #     if a % i == 0:
# #         suma += i
# # for i in range(1, b + 1):
# #     if b % i == 0:
# #         sumb +=i
# # print(max(suma,sumb))
# #
# #
# alist=[]
# for i in range(10):
#     blist=list(map(int,input().split()))
#     alist.append(blist)
# for i in range(len(alist)):
#     for j in range(len(alist[i])):
#         if i==0 :
#             if j==0:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i+1][j]==1 or  alist[i][j+1]==1 or alist[i+1][j+1]==1 or alist[i+1][j+1]==1 ) )and alist[i][j] !=9:
#                     if alist[i+1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j+1] ==0 :
#                         alist[i][j+1]=9
#             elif j==len(alist[i])-1:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i+1][j]==1 or alist[i][j-1]==1  ) )and alist[i][j] !=9:
#                     if alist[i+1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j-1] ==0 :
#                         alist[i][j-1]=9
#             else:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i+1][j]==1 or alist[i][j-1]==1 or alist[i][j+1]==1 or alist[i+1][j+1]==1 or alist[i+1][j+1]==1 ) )and alist[i][j] !=9:
#                     if alist[i+1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j+1] ==0 :
#                         alist[i][j+1]=9
#
#         elif i==len(alist)-1:
#             if j==0:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i][j+1]==1 or alist[i+1][j+1]==1 ) )and alist[i][j] !=9:
#                     if alist[i-1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j+1] ==0 :
#                         alist[i][j+1]=9
#             elif j==len(alist[i])-1:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i+1][j]==1 or alist[i][j-1]==1  ) )and alist[i][j] !=9:
#                     if alist[i-1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j-1] ==0 :
#                         alist[i][j-1]=9
#             else:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and ( alist[i][j-1]==1 or alist[i][j+1]==1 ) )and alist[i][j] !=9:
#                     if alist[i-1][j] ==0:
#                         alist[i-1][j]=9
#                     if alist[i][j-1] ==0 :
#                         alist[i][j-1]=9
#
#         else:
#             if j==0:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i-1][j]==1 or alist[i-1][j+1]==1 or alist[i][j+1]==1 or alist[i+1][j+1]==1 or alist[i+1][j]==1 ) )and alist[i][j] !=9:
#                     if alist[i-1][j] ==0 :
#                         alist[i-1][j]=9
#                     if alist[i+1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j+1] ==0 :
#                         alist[i][j+1]=9
#
#             elif j==len(alist[i])-1:
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i-1][j]==1 or alist[i+1][j]==1 or alist[i+1][j-1]==1 or alist[i][j-1]==1 or alist[i-1][j-1]==1) )and alist[i][j] !=9:
#                     if alist[i-1][j] ==0 :
#                         alist[i-1][j]=9
#                     if alist[i+1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j-1] ==0 :
#                         alist[i][j-1]=9
#
#             else:
#                 #if alist[i][j] ==1 or (alist[i][j]==2):
#                 if alist[i][j] ==1 or (alist[i][j]==2 and (alist[i-1][j]==1 or alist[i-1][j+1]==1 or alist[i][j+1]==1 or alist[i+1][j+1]==1 or alist[i+1][j]==1 or alist[i+1][j-1]==1 or alist[i][j-1]==1 or alist[i-1][j-1]==1) ) and alist[i][j] !=9:
#                     if alist[i-1][j] ==0 :
#                         alist[i-1][j]=9
#                     if alist[i+1][j] ==0:
#                         alist[i+1][j]=9
#                     if alist[i][j-1] ==0 :
#                         alist[i][j-1]=9
#                     if alist[i][j+1] ==0 :
#                         alist[i][j+1]=9
# for i in alist:
#     for j in i:
#         print(j,end=" ")
#     print()

# a =int(input()) #day
# alist =list(map(int,input().split())) #car
# count=0
# for i in alist:
#     if a%2==0:
#         if i %2==0:
#             count+=1
#     else:
#         if i%2!=0:
#             count+=1
# print(count)

#

# h,m = list(map(int,input().split()))
# a,b = list(map(int,input().split()))
#
# total = h*60 + m -(a+b)
# print(total//60 , total%60)
#
#
# n,x0,y0=list(map(int,input().split()))
# alist=[]
#
# for i in range(n):
#     x1,y1=list(map(int,input().split()))
#     if x1-x0==0:
#         alist.append(1000)
#     else:
#         alist.append((y1-y0)/(x1-x0))
# # print(alist)
# # print(set(alist))
# print(len(set(alist)))

#
#
year =int(input())
alist=["mouse", "cow", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "chicken", "dog", "pig"]












