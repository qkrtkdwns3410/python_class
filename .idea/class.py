# num = int(input())
# winlist=[]
# for i in range(num):
#     x=int(input())
#     winlist.append(x)
#
#
# T = [[0 for i in range(2)] for j in range(num+1)]
#
# for i in range(1, num+1):
#     T[i][0] = max(T[i-1])
#     if i > 1:
#         T[i][1] = max(T[i-2][0] + winlist[i-1] + winlist[i-2], T[i-1][0] + winlist[i-1])
#     else:
#         T[i][1] = winlist[i-1]
#
#
#
# print(str(max(T[num])))
# import math
# from itertools import combinations
# n =int(input())
# for i in range(n):
#     a,b =list(map(int,input().split()))
#     print(math.factorial(b)//math.factorial(a)//math.factorial(b-a))
#     blist=[i for i in range(b)]
#     for j in range(1,b+1):
#         comb=combinations(blist,j)
#         for k in comb:
#             print(k)

# print("\"Hello! I\'m a student\"")
# print("I like playing game.")


# print(input())

# a,b =list(map(int,input().split()))
# print(a*b//2)

# a =int(input())
#
#
# if a%2 ==0:
#     print(0)
# else:
#     print(1)
#
#
# a =int(input())
# if a>=30:
#     print(1)
# else:
#     print(0)
#
#
#
# a,b =list(map(int,input().split()))
# print(max(a,b))

#
# a=int(input())
# print(a+2,a+4)

# a=int(input())
# for i in range(1,a+1):
#     print(i)


# from collections import Counter
# a=int(input())
# n=[]
# counta=0
# countb=0
# for i in range(a):
#     n.append(input())
#
# c=Counter(n).most_common()
# # print(c)
# print(c[0][0])

# for i in range(a):
#     if n[i]=='A':
#         counta+=1
#     elif n[i]=='B':
#         countb+=1
#     else:
#         pass
# if counta > countb:
#     print('A')
# else:
#     print('B')

















