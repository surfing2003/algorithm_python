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
# N = int(input())
# idx_list = list(map(int,input().split()))
# balloons = [i+1 for i in range(N)]

# idx = 0
# K = idx_list.pop(0)
# print(balloons.pop(0),end = ' ')
# while balloons:
#     if K >0 :
#       idx = (idx+K-1) % len(balloons)
#     else :
#         idx = (idx+len(balloons)+K) % len(balloons)
#     K = idx_list.pop(idx)
#     print(balloons.pop(idx), end =' ')


# N = int(input())

# def fact(N):
#     if N == 0 or N == 1:
#         return 1
#     else:
#         return fact(N-1)*N

# print(fact(N))


# N = int(input())

# def fib(N):
#     if N==0:
#         return 0
#     if N==1:
#         return 1
#     else:
#         return fib(N-1)+fib(N-2)

# print(fib(N))

# 별찍기 10 
# N = int(input())
# stars = [[' ' for _ in range(N)] for _ in range(N)]

# def fill_star(size,x,y):
#     if size == 1:
#         stars[y][x] = '*'
#     else:
#         next = size//3
#         for dx in range(3):
#             for dy in range(3):
#                 if dx != 1 or dy != 1:
#                     fill_star(next,x+dx*next,y+dy*next)
# fill_star(N,0,0)
# for k in stars:
#     print(''.join(k))
# #
# def concat(r1, r2):
#     return [''.join(x) for x in zip(r1, r2, r1)]

# def stars(n):
#     if n == 1:
#         return ['*']
#     n //= 3
#     x = stars(n)
#     t = concat(x, x)
#     m = concat(x, [' '*n]*n)
#     return t + m + t


# n = int(input())
# print('\n'.join(stars(n)))

# from itertools import combinations

# N, M = map(int, input().split())
# cards = list(map(int,input().split()))
# answer = 0

# for temp in list(combinations(cards,3)):
#     card_sum = sum(temp)
#     if card_sum <= M:
#         answer = max(answer,card_sum)
# print(answer)

# N = int(input())
# c = 1
# while True:
#     temp = c
#     for i in str(temp):
#         temp += int(i)
#     if c == N:
#         print(0)
#         break
#     elif temp == N:
#         print(c)
#         break
#     c += 1

# N = int(input())
# for i in range(1,N+1):
#     temp = i + sum(list(map(int,str(i))))
#     if temp == N:
#         print(i)
#         break
#     if i == N:
#         print(0)
#         break


# N = int(input())
# people = [list(map(int,input().split())) for _ in range(N)]
# answer = []
# for i in range(N):
#     rank = 1
#     for j in range(N):
#         if i == j:
#             continue
#         if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
#             rank += 1
#     answer.append(str(rank))
# print(' '.join(answer)) 

# N = int(input())
# name = 665

# while N:
#     name += 1
#     if "666" in str(name):
#         N -= 1

# print(name)

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# N = int(input())
# temp = [0] * 10001

# for _ in range(N):
#     temp[int(input())] += 1

# # for i in range(1,10001):
# #     if temp[i] != 0:
# #         for _ in range(temp[i]):
# #             print(i)

# for i in range(1,10001):
#     print(f'{i}\n' * temp[i], end='')


# def smallestSubsequence(self, s: str) -> str:
#         s_dict = {}
#         for i,k in enumerate(s):
#             if k not in s_dict.keys():
#                 s_dict[k] = [i]
#             else:
#                 s_dict[k].append(i)
        
#         s_dict = sorted(s_dict.keys())
#         print(s_dict)

# def smallestSubsequence( s:str):
#     s_dict = {}
#     stack=[]
#     last = {}

#     for i in range(len(s)):
#         last[s[i]]=i
#     print(last)
#     for i,ch in enumerate(s):
#         if(ch in stack):
#             continue
#         while(stack and stack[-1]>ch and i<last[stack[-1]]):
#             print(stack)
#             stack.pop()
#         stack.append(ch)
#         print("s:",stack)
#     return ''.join(stack)

# smallestSubsequence(s="cbacdcbc")



# 유클리드 호제법
# A,B(A>B)의 최대공약수는  B와 R(A를 B로나눈 나머지)의 최대공약수와 같다.

# gcd(192,162)

# def gdc(a, b):
#     if a%b == 0:
#         return b
#     else :
#         return gdc(b, a%b)

# print(gdc(192,162))

# # dfs
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = ' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [False] * 9
# dfs(graph,1,visited)
# print()

# # bfs
# from collections import deque

# def bfs(graph, start, visited):
#     q = deque([start])
#     visited[start] = True

#     while q:
#         v = q.popleft()
#         print(v, end = ' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [False] * 9
# bfs(graph,1,visited)

# def dfs(x,y):
#     if x <= -1 or x >= N or y <= -1 or y >= M:
#         return False
#     if maps[x][y] == 0:
#         # 해당 시작점 방문 적용
#         maps[x][y] = 1
#         # 연결된 부분 방문 적용
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         # 실제로 사용하는 리턴값
#         return True

#     return False

# N,M = map(int, input().split())

# maps = [list(map(int,input())) for _ in range(N)]

# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i,j):
#             result += 1
# print(result)
# 4 5
# 00110
# 00011
# 11111
# 00000
# 3
# from collections import deque

# def bfs(x,y):
#     q = deque()
#     q.append((x,y))

#     while q:
#         x,y = q.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if maps[nx][ny] == 0:
#                 continue
#             if maps[nx][ny] == 1:
#                 maps[nx][ny] = maps[x][y] + 1
#                 q.append((nx,ny))
#     return maps[N-1][M-1]

# N, M = map(int,input().split())
# maps = [list(map(int,input())) for _ in range(N)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# print(bfs(0,0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 10

# # 선택정렬
# # O(N^2)
# array = [7,5,9,0,3,1,6,2,4,8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i],array[min_index] = array[min_index],array[i]
# print(array)

# # 삽입정렬
# # O(N^2)
# array = [7,5,9,0,3,1,6,2,4,8]

# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1],array[j]
#         else:
#             break
# print(array)

# # 퀵정렬
# # O(NlogN) 최악의 경우 O(N^2)

# array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start+1
#     right = end
#     while (left <= right):
#         while(left <= end and array[left] <= array[pivot]):
#             left += 1
#         while(right > start and array[right] >= array[pivot]):
#             right -= 1
#         if left > right :
#             array[right], array[pivot] = array[pivot],array[right]
#         else:
#             array[left], array[right] = array[right],array[left]
#     quick_sort(array, start, right -1)
#     quick_sort(array,right+1,end)

# quick_sort(array,0,len(array)-1)
# print(array)



# array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort2(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#     return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

# print(quick_sort2(array))

# # 계수정렬
# # O(N+K)

# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# count = [0] * (max(array)+1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     print(f'{i} ' * count[i], end='')


# 이진탐색
# O(logN)

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)

# def binary_search2(array, target, start, end):
#     while start <= end:
#         mid = (start+end)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n, target = list(map(int,input().split()))
# array = list(map(int,input().split()))

# result = binary_search(array,target,0,n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
# else :
#     print(result + 1)

# result = binary_search2(array,target,0,n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
# else :
#     print(result + 1)
# 10 7
# 1 3 5 7 9 11 13 15 17 19
# 4

# 10 7
# 1 3 5 6 9 11 13 15 17 19
# 원소가 존재하지 않습니다.


# 파이썬 이진탐색 라이브러리 
# from bisect import bisect_left,bisect_right

# bisect_left : 정렬된순서를 유지하면서 배열 a에 x를 삽일할 가장 왼쪽 인덱스를 반환
# bisect_right: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

# a = [1,2,4,4,8]
# x = 4

# print(bisect_left(a,x))
# print(bisect_right(a,x))

# 파라메트릭 서치

# def binary_search(target,start,end):
#     while start <= end:
#         mid = (start+end)//2
#         div = 0
#         for i in dduk:
#             if i > mid:
#                 div += i-mid
        
#         if div == target:
#             return mid
#         elif div > target:
#             start = mid + 1 
#         else:
#             end = mid -1
#     return None
# N, M = map(int,input().split())
# dduk = list(map(int,input().split()))
# print(binary_search(M,0,max(dduk)))

# N, M = map(int,input().split())
# array = list(map(int,input().split()))

# start = 0
# end = max(array)

# result = 0
# while (start <= end):
#     total = 0
#     mid = (start+end)//2
#     for x in array:
#         if x > mid:
#             total += x-mid
#     if total < M:
#         end = mid -1
#     else:
#         result = mid ## 중간에 길이를 저장해두어야함.
#         start = mid +1

# print(result)

# from bisect import bisect_left, bisect_right

# N, X = map(int,input().split())
# array = list(map(int,input().split()))


# print(bisect_right(array,X) - bisect_left(array,X))

# 피보나치 동적
# O(N)
# d = [0] * 100

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1)+fibo(x-2)
#     return d[x]

# print(fibo(99))

# d = [0] *100

# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3,n+1):
#     d[i] = d[i-1]+d[i-2]

# print(d[n])

# N = int(input())
# store = list(map(int,input().split()))
# ant = [0]*N
# ant[0] = store[0]
# ant[1] = max(store[0],store[1])
# for i in range(2,N):
#     ant[i] = max(store[i] + ant[i-2],ant[i-1])
# print(ant[N-1])

# N = int(input())

# d = [0] * 30001

# for i in range(2,N+1):
#     d[i] = d[i-1]+1
#     if i % 2 == 0:
#         d[i] = min(d[i],d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i],d[i//3]+1)
#     if i % 5 == 0:
#         d[i] = min(d[i],d[i//5]+1)
# print(d[N])

# N,M = map(int,input().split())
# coins = [int(input()) for _ in range(N)]

# d = [10001]* (M+1)

# d[0] = 0
# for i in range(N):
#     for j in range(coins[i],M+1):
#         if d[j - coins[i]] != 10001:
#             d[j] = min(d[j],d[j-coins[i]]+1)

# if d[M] == 10001:
#     print(-1)
# else:
#     print(d[M])

# for _ in range(int(input())):
#     N, M = map(int,input().split())
#     array = list(map(int,input().split()))

#     dp = []
#     index = 0
#     for i in range(N):
#         dp.append(array[index:index+M])
#         index += M
    
#     for j in range(1,M):
#         for i in range(N):
#             if i==0: left_up = 0
#             else: left_up = dp[i-1][j-1]

#             if i==N-1: left_down = 0
#             else: left_down = dp[i+1][j-1]

#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left_up,left,left_down)

#     result = 0
#     for i in range(N):
#         result = max(result,dp[i][m-1])
#     print(result)

#LIS
# N = int(input())
# array = list(map(int,input().split()))
# array.reverse()

# dp = [1]*N

# for i in range(1,N):
#     for j in range(0,i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i],dp[j]+1)
    
# print(N - max(dp))


# 다익스트라 O(V^2) 노드 개수 5000개 이하
# 음의 간선 X
# 그리디알고리즘
# 출발노드 설정 > 최단거리테이블 초기화
# > 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 선택
# > 해당 노드를 거쳐 다른노드로 가는 비용을 계산하여 최단거리테이블 갱신
# > 3 ~ 4번 과정 반복

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int,input().split())
# start = int(input())

# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))

# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True

#     for j in graph[start]:
#         distance[j[0]] = j[1]
    
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True

#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost


# dijkstra(start)

# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

# 우선순위큐
# 가장 우선순위가 높은 데이터 순서대로 추출 > 힙활용
# 최소힙 낮은데이터부터 최대힙 높은데이터 
# 리스트 삽입 O(1), 삭제 O(N)
# 힙    삽입 O(logN), 삭제 O(logN)
# 파이썬 기본 최대힙 
# import heapq
# # 오름차순(최소힙)
# def heapsort1(iterable):
#     h = []
#     result = []

#     for value in iterable:
#         heapq.heappush(h,value)
    
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
    
#     return result
# # 내림차순(최대힙)
# def heapsort2(iterable):
#     h = []
#     result = []

#     for value in iterable:
#         heapq.heappush(h,-value)
    
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h))
    
#     return result

# result = (heapsort1([1,3,5,7,9,2,4,6,8,0]))
# print(result)
# result = (heapsort2([1,3,5,7,9,2,4,6,8,0]))
# print(result)

# # 다익스트라 힙 활용
# # O(ElogV)

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n,m = map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]

# distance = [INF] *(n+1)

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
        
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))

# dijkstra(start)
# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])


# 플로이드 워셜 알고리즘
# O(N^3)
# 노드가 적을때는 효과적이지만 노드가 많으면 다익스트라를 활용
# D_ab = min(D_ab, D_ak + D_kb)

# INF = int(1e9)
# n = int(input()) # 노드?
# m = int(input()) # 간선?

# graph = [[INF] * (n+1) for _ in range(n+1)]

# for a in range(1,n+1):
#     graph[a][a] = 0

# for  _ in range(m):
#     a, b, c = map(int,input().split())
#     graph[a][b] = c

# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if graph[a][b] == INF:
#             print("INF",end = " ")
#         else:
#             print(graph[a][b], end = " ")
#     print()

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0

#     while q:
#         dist , now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
            
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))

# #노드 간선 시작
# n, m, start = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y,z))

# dijkstra(start)

# count = 0
# max_distance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distance = max(max_distance,d)
# print(count - 1, max_distance)


# n, m = map(int,input().split())
# INF = int(1e9)
# graph = [[INF]*(n+1) for _ in range(n+1)]

# for i in range(1,n+1):
#     graph[i][i] = 0

# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# x, k = map(int,input().split())

# for c in range(1, n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             graph[a][b] = min(graph[a][b], graph[a][c]+graph[c][b])

# dist = graph[1][k] + graph[k][x]
# if dist >= INF:
#     print("-1")
# else:
#     print(dist)

# # 서로소 집합
# # 편향된 상태에서는 효율적이지 않기때문에 아래처럼 parent를 갱신하는 방식을 활용
# def find_parent(parent,x):
#     if parent[x] != x:
#         return find_parent(parent,parent[x])
#     return x

# # 부모노드가 루트노드가 되도록 parent를 변경
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]


# def union_parent(parent,a,b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


# v, e = map(int,input().split())
# parent = [0] * (v+1)
# for i in range(1,v+1):
#     parent[i] = i

# for i in range(e):
#     a, b = map(int,input().split())
#     union_parent(parent, a, b)

# for i in range(1,v+1):
#     print(find_parent(parent,i),end = ' ')
# print()
# for i in range(1,v+1):
#     print(parent[i], end = " ")
# print()

# 서로소 집할을 활용한 무방향그래프에서 사이클 판별
# 방향의 경우는 dfs를 활용
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int,input().split())
# parent = [0] * (v+1)

# for i in range(1,v+1):
#     parent[i] = i

# cycle = False

# for i in range(e):
#     a, b = map(int,input().split())
#     if find_parent(parent,a) == find_parent(parent,b):
#         cycle = True
#         break
#     else:
#         union_parent(parent,a,b)

# print(cycle)

# 신장트리 
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 최소신장트리 - 크루스칼 알고리즘 O(ElogE)
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int,input().split())
# parent = [0] * (v+1)
# edges = []
# result = 0

# for i in range(1,v+1):
#     parent[i] = i

# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost,a,b))

# edges.sort()

# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent,a) != find_parent(parent,b):
#         union_parent(parent,a,b)
#         result += cost
# print(result)

# 위상정렬 O(V+E)
# 진입차수 : 특정한 노드로 들어오는 간선의 개수
# 진출차수 : 특정한 노드로 나가는 간선의 개수
# 큐를 이용하는 위상정렬알고리즘의 동작과정
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다 
# 2. 큐가 빌때까지 다음의 과정을 반복한다. 
#   1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선의 그래프에서 제거한다.
#   2) 새롭게 진입하는 차수가 0이 된 노드를 큐에 넣는다.
# 각 노드가 큐에 들어온 순서가 위상정렬을 수행한 결과와 같다.
# 사이클이 없는 방향그래프 (DAG) 에서 가능

# 모든원소를 방문하기 전에 큐가 비는경우 사이클이 존재
# 스택을 활용한 DFS로도 가능

# from collections import deque

# v, e = map(int,input().split())

# indegree = [0] * (v+1)
# graph = [[] for i in range(v+1)]

# for _ in range(e):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     indegree[b] += 1

# def topology_sort():
#     result = []
#     q = deque()
    
#     for i in range(1,v+1):
#         if indegree[i] == 0:
#             q.append(i)
        
#     while q:
#         now = q.popleft()
#         result.append(now)

#         for i in graph[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
#     for i in result:
#         print(i,end = " ")
#     print()

# topology_sort()

# # 소수 판별 알고리즘
# def is_prime_number1(x):
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True

# print(is_prime_number1(4))
# print(is_prime_number1(7))

# import math

# def is_prime_number2(x):
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# print(is_prime_number1(4))
# print(is_prime_number1(7))

# # 에라토스테네스의 체 O(NloglogN)
# # 2부터 N까지의 모든 자연수를 나열한다. 
# # 남은 수 중에서 아직 처리하지 않은 가장 작은 소수 i를 찾는다 
# # 남은 수중에서 i의 배수를 모두 제거한다. (i는 제거하지 않는다.)
# # 더이상 반복할 수 없을 때까지 반복

# import math

# n = 1000
# array = [True] * (n+1)

# for i in range(2,int(math.sqrt(n))+1):
#     if array[i] == True:
#         j = 2
#         while i*j <= n:
#             array[i*j] = False
#             j+=1

# for i in range(2,n+1):
#     if array[i]:
#         print(i, end=" ")
# print()

# 투포인터 알고리즘
# 특정한 합을 가지는 부분 연속 수열 찾기 


n = 5
m = 5

data = [1,2,3,2,5]

count = 0
interval = 0
end = 0

for start in range(n):
    while interval < m and end < n:
        interval += data[end]
        end += 1
    if interval == m:
        count += 1
    interval -= data[start]

# 구간합 
# 접두사합 : 배열의 앞부터 특정 위치까지의 합을 미리 구해놓는 것

n = 5
data = [10,20,30,40,50]

sum_val = 0
prefix_sum = [0]
for i in data:
    sum_val += i
    prefix_sum.append(sum_val)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])