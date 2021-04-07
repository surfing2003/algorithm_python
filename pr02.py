import sys
input = lambda : sys.stdin.readline().rstrip()


# n, k = map(int, input().split())

# item_list = [[0,0]]
# bags = [[0 for _ in range(k+1)] for _ in range(n+1)]

# for _ in range(n):
#     item_list.append(list(map(int,input().split())))

# for i in range(1,n+1):
#     for j in range(1,k+1):
#         w = item_list[i][0]
#         v = item_list[i][1]

#         if j < w:
#             bags[i][j] = bags[i-1][j]
#         else:
#             bags[i][j] = max(v+bags[i-1][j - w], bags[i-1][j])
        
# print(bags[n][k])

# import bisect

# n = int(input())
# x = []

# result = []

# for _ in range(n):
#     bisect.insort(x,int(input()))
#     if(len(x)%2 == 0):
#         result.append(x[len(x)//2 - 1])
#     else:
#         result.append(x[len(x)//2])
# for i in result:
#     print(i)

##############################################
# import sys 
# import bisect 
# input = sys.stdin.readline 
# n = int(input().rstrip()) 
# x = [] 
# answers = [] 
# for _ in range(n): 
#     bisect.insort(x, int(input().rstrip())) 
#     if(len(x) % 2 == 0): 
#         answers.append(x[int(len(x)/2)-1]) 
#     else: 
#         answers.append(x[int(len(x)/2)]) 
    
# for a in answers: 
#     print(a)

# max_h, min_h = [], []

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# import heapq

# n = int(input())
# max_h, min_h  = [], []
# for _ in range(n):
#     num = int(input())
#     if len(max_h) == len(min_h):
#         heapq.heappush(max_h, (-num, num))
#     else:
#         heapq.heappush(min_h, (num, num))
#     if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0][1] > min_h[0][1]:
#         max_value = heapq.heappop(max_h)[1]
#         min_value = heapq.heappop(min_h)[1]
#         heapq.heappush(max_h, (-min_value, min_value))
#         heapq.heappush(min_h, (max_value, max_value))
#     print(max_h[0][1])

##############################################
# result = [0] * 10

# a = int(input())
# b = int(input())
# c = int(input())
# n = a * b * c

# for i in str(n):
#     result[int(i)] += 1

# for i in result:
#     print(i)

# a = int(input())
# b = int(input())
# c = int(input())

# d = list(map(int, (str(a * b * c))))

# for i in range(10):
#     print(d.count(i))

##############################################
# a = set()
# for _ in range(10):
#     temp = int(input())
#     a.add(temp%42)

# print(len(a))    

# b = [int(input())%42 for i in range(10)]
# print(len(set(b)))

##############################################

# n = int(input())
# score = list(map(int,input().split()))
# max_s = max(score)
# sum_s = 0
# for s in score:
#     sum_s += (s/max_s) * 100
# print(sum_s/n)

# ##############################################
# c = int(input())

# for _ in range(c):
#     temp = list(map(int,input().split()))
#     n = temp[0]
#     score = temp[1:]
#     mean = sum(score)/n
#     total = 0
#     for i in score:
#         if i > mean:
#             total += 1
#     print(format(total/n*100,".3f")+"%")
 
# print("A" in ["-A","A"])

# numbers = set(range(1,10001))
# generate_numbers = set()

# for i in range(1,10001):
#     for j in str(i):
#         i += int(j)
#     generate_numbers.add(i)

# self_num = sorted(numbers - generate_numbers)
# for i in self_num:
#     print(i)

# N = input()
# cnt = 0
# for i in range(1,N+1):
#     if i < 100 :
#         cnt += 1
#     else:
#         temp = str(i)
#         if int(temp[0]) + int(temp[2]) == int(temp[1]) * 2:
#             cnt += 1
# print(cnt)

# from string import ascii_lowercase

# N = input()
# a_list = list(ascii_lowercase)
# for i in a_list:
#     print(N.find(i),end = ' ')


# from collections import Counter

# N = input().upper()
# chk = Counter(N).most_common(2)

# if len(chk) == 1:
#     print(chk[0][0])
# elif chk[0][1] == chk[1][1]:
#     print('?')
# else:
#     print(chk[0][0])


# A,B = input().split()
# A_1 = int(A[::-1])
# B_1 = int(B[::-1])
# if A_1 > B_1:
#     print(A_1)
# else:
#     print(B_1)
    
# print(max([int(i[::-1] for i in input().split())]))

# N = input()
# a = ['ABC','DEF','GHI',"JKL","MNO","PQRS","TUV","WXYZ"]
# answer = 0

# for i in N:
#     for j in a:
#         if i in j:
#             answer += a.index(j) + 3
# print(answer)

# print(sum((ord(i)-62-(i in 'SVYZ')-(i=='Z'))//3+2 for i in input()))

# N = input()
# change_list = ["c=","c-","dz=","d-","lj","nj","s=","z=","dz="]

# for i in change_list:
#     N=N.replace(i,"*")
# print(len(N))

# A, B, C = map(int, input().split())

# if C-B <= 0:
#     print(-1)
# else:
#     print(A//(C-B) + 1)

# N = int(input())
# now = 1
# plus = 6
# result = 1
# if N == 1:
#     print(result)
# else:
#     while True:
#         now += plus
#         result += 1
#         if N <= now:
#             print(result)
#             break
#         plus += 6

# N = int(input())
# now = 1

# while N>now:
#     N -= now
#     now += 1

# if now % 2 == 0:
#     a = N
#     b = now - N + 1
# else:
#     a = now - N + 1
#     b = N
# print(a,"/",b,sep="")

# A,B,C = map(int,input().split())

# def solution(A,B,C):
#     if B == 1:
#         return A % C
#     else:
#         temp = solution(A,B//2,C)
#         if B % 2 == 0:
#             return temp * temp % C
#         else :
#             return temp * temp * A % C

# print(solution(A,B,C))
# print(pow(A,B,C))

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     print(pow(2,max(0,n-2),10**9+7))

# N, K = map(int, input().split())

# now = [i+1 for i in range(N)]
# result = []
# idx = 0
# while now:
#     idx = (idx+K-1) % len(now)
#     temp = now.pop(idx)
#     result.append(str(temp))

# print("<%s>"%(", ".join(result)))

#
N = int(input())
idx_list = list(map(int,input().split()))
balloons = [i+1 for i in range(N)]

idx = 0
K = idx_list.pop(0)
print(balloons.pop(0),end = ' ')
while balloons:
    if K >0 :
      idx = (idx+K-1) % len(balloons)
    else :
        idx = (idx+len(balloons)+K) % len(balloons)
    K = idx_list.pop(idx)
    print(balloons.pop(idx), end =' ')
    
