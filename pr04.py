# 4949
# import sys
# input = lambda : sys.stdin.readline().rstrip()


# while True:
#     sentence = input()
    
#     if sentence == '.':
#         break

#     flag = True
#     chk = []
#     for s in sentence:
#         if s == "(" or s == "[":
#             chk.append(s)
#             continue
    
#         elif s == ")":
#             if chk and chk[-1] == "(":
#                 chk.pop()
#                 continue
#             else:
#                 flag = False        
#                 break
#         elif s == "]":
#             if chk and chk[-1] == "[":
#                 chk.pop()
#                 continue
#             else:
#                 flag = False        
#                 break

#     if not chk and flag:
#         print("yes")
#     else:
#         print("no")

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# temp = []
# answer = []
# count = 0
# flag = False
# for now in arr:
#     while count < now:
#         count += 1
#         temp.append(count)
#         answer.append("+")
    
#     if temp[-1] == now:
#         temp.pop()
#         answer.append("-")
#     else:
#         flag = True
#         break

# if flag:
#     print("NO")
# else:
#     print('\n'.join(answer))


# 시간초과
# N = int(input())
# arr = list(map(int,input().split()))
# answer = [-1] * N

# for i in range(N):
#     for j in range(i,N):
#         if arr[i] < arr[j]:
#             answer[i] = arr[j]
#             break
# print(*answer)
    

# N = int(input())
# arr = list(map(int,input().split()))
# temp = []
# answer = [-1] * N

# for i in range(N):
#     while len(temp) != 0 and arr[temp[-1]] < arr[i]:
#         answer[temp.pop()] = arr[i]
#     temp.append(i)

# print(*answer)

# import sys
# from collections import deque

# input = lambda : sys.stdin.readline().rstrip()
# q = deque()
# for _ in range(int(input())):
#     temp = input().split()

#     if temp[0] == "push":
#         q.append(temp[1])
#     elif temp[0] == "pop":
#         if q:
#             print(q.popleft())
#         else:
#             print(-1)
#     elif temp[0] == "front":
#         if q:
#             print(q[0])
#         else:
#             print(-1)

#     elif temp[0] == "back":
#         if q:
#             print(q[-1])
#         else:
#             print(-1)
    
#     elif temp[0] == "size":
#         print(len(q))
    
#     elif temp[0] == "empty":
#         if not q:
#             print(1)
#         else:
#             print(0)

# from collections import deque

# q = deque(range(1,int(input())+1))

# while len(q) != 1:
#     q.popleft()
#     q.rotate(-1)

# print(q[0])

# N,K = map(int,input().split())
# q = list(range(1,N+1))
# answer = []
# idx = 0
# while q:
#     idx = ((idx + K-1) % len(q))
#     answer.append(str(q.pop(idx)))

# print("<{}>".format(', '.join(answer)))

# from collections import deque
# T = int(input())

# for _ in range(T):
#     N,T = map(int,input().split())
#     w = list(map(int,input().split()))
#     q = deque()
#     for i in w:
#         if len(q) == T:
#             q.append((i,1))
#             continue
#         q.append((i,0))

#     count = 0
#     w.sort(reverse=True)
#     while q:
#         temp = q.popleft()
#         if temp[0] == w[0]:
#             count += 1
#             w.pop(0)
#             if temp[1] == 1:
#                 break
#         else:
#             q.append(temp)
#     print(count)

# from collections import deque
# N, T = map(int,input().split())
# arr = list(map(int,input().split()))
# q = deque(range(1,N+1))
# answer = 0

# for a in arr:
#     i = 0
#     while a != q[i]:
#         i += 1

#     if len(q) - i < i:
#         i = len(q) - i
#     else:
#         i = -i

#     q.rotate(i)
#     answer += abs(i)
#     q.popleft()
# print(answer)

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# T = int(input())

# for _ in range(T):
#     flag = False
#     time = list(input())
#     n = int(input())
#     arr = input()[1:-1].split(',')
#     if n == 0:
#         arr = []

#     l,r,d,flag = 0,0,True,False    
#     for t in time:
#         if t == "R":
#             d = not d
#         if t == "D":
#             if d:
#                 l += 1
#             else:
#                 r += 1
#         if l+r > n:
#             print("error")
#             flag = True
#             break
#     if flag:
#         continue
#     else:
#         temp = arr[l:n-r]
#         if d:
#             print("[{}]".format(",".join(temp)))
#         else:
#             print("[{}]".format(",".join(temp[::-1])))


# N,M = map(int,input().split())
# A = [list(map(int,input().split())) for _ in range(N)]

# M,K = map(int,input().split())
# B = [list(map(int,input().split())) for _ in range(N)]

# C = [[0] * K for _ in range(N)]

# for ni in range(N):
#     for ki in range(K):
#         for mi in range(M):
#             C[ni][ki] += A[ni][mi] * B[mi][ki]

# for i in C:
#     print(*i)

# N = int(input())
# M = int(input())
# INF = int(1e9)
# arr = [[INF]*N for _ in range(N)]
# for _ in range(M):
#     i,j,k = map(int,input().split())
#     if arr[i-1][j-1] > k:
#         arr[i-1][j-1] = k

# for i in range(N):
#     arr[i][i] = 0

# for k in range(N):    
#     for i in range(N):
#         for j in range(N):
#             if i != j:
#                 arr[i][j] = min(arr[i][j],arr[i][k] + arr[k][j])

# for a in arr:
#     for i in a:
#         if i == INF:
#             print(0, end = ' ')
#         else:
#             print(i, end = ' ')
#     print()


# from collections import deque

# V = int(input())
# arr = [[] for _ in range(V+1)]

# for _ in range(V):
#     c = list(map(int,input().split()))
#     for e in range(1,len(c)-2,2):
#         arr[c[0]].append((c[e],c[e+1]))

# def bfs(start):
#     visited = [-1]*(V+1)
#     q = deque()
#     q.append(start)
#     visited[start]=0
#     max_e = [0,0]

#     while q:
#         now = q.popleft()
#         for e,w in arr[now]:
#             if visited[e] == -1:
#                 visited[e] = visited[now] + w
#                 q.append(e)
#                 if max_e[0] < visited[e]:
#                     max_e = visited[e],e
#     return max_e

# dis,node = bfs(1) 
# dis,node = bfs(node)
# print(dis)


# from collections import deque

# n = int(input())
# arr = [[] for _ in range(n+1)]

# for _ in range(n-1):
#     i,j,k = map(int,input().split())
#     arr[i].append((j,k))
#     arr[j].append((i,k))

# def bfs(start):
#     visited = [-1]*(n+1)
#     q = deque()
#     q.append(start)
#     visited[start]=0
#     max_e = [0,0]

#     while q:
#         now = q.popleft()
#         for e,w in arr[now]:
#             if visited[e] == -1:
#                 visited[e] = visited[now] + w
#                 q.append(e)
#                 if max_e[0] < visited[e]:
#                     max_e = visited[e],e
#     return max_e

# dis,node = bfs(1) 
# dis,node = bfs(node)
# print(dis)

# 트리의 지름은 한번 탐색해서 가장 먼 노드에서 다시 탐색을 하면 찾을 수 있다. 

# from heapq import heappop, heappush

# INF = int(1e9)

# V,E = map(int,input().split())
# start = int(input())
# arr = [[] for _ in range(V+1)]

# for _ in range(E):
#     i,j,w = map(int,input().split())
#     arr[i].append((j,w))

# dp = [INF] * (V+1)
# heap = []
# def dijkstra(start):
#     dp[start] = 0
#     heappush(heap,(0,start))
#     while heap:
#         w,n = heappop(heap)
#         for dn, dw in arr[n]:
#             nw = w+dw
#             if nw < dp[dn]:
#                 dp[dn] = nw
#                 heappush(heap,(nw,dn))

# dijkstra(start)
# for i in dp[1:]:
#     print(i if i != INF else "INF")

# T = int(input())
# INF = int(1e9)
# def solve_bf(bf,graph,N,M):
#     bf[1] = 0
#     for i in range(N):
#         for v in range(1,N+1):
#             for nv,nw in graph[v]:
#                 if bf[nv] > bf[v] + nw:
#                     bf[nv] =  bf[v]+nw
#                     if i == N-1:
#                         print("YES")
#                         return
#     print("NO")
#     return

# for _ in range(T):
#     N,M,W = map(int,input().split())
#     graph = [[] for _ in range(N+1)]
#     bf = [INF] * (N+1)

#     for _ in range(M):
#         s,e,t = map(int,input().split())
#         graph[s].append([e,t])
#         graph[e].append([s,t])

#     for _ in range(W):
#         s,e,t = map(int,input().split())
#         graph[s].append([e,-t])

#     solve_bf(bf,graph,N,M)

# temp = input()
# stack = []
# answer = ''
# for t in temp:
#     if t.isalpha():
#         answer += t
#     else:
#         if t == '(':
#             stack.append(t)
        
#         elif t == '*' or t == '/':
#             while stack and (stack[-1]=='*' or stack[-1]=='/'):
#                 answer += stack.pop()
#             stack.append(t)

#         elif t == '+' or t == '-':
#             while stack and stack[-1] != '(':
#                 answer += stack.pop()
#             stack.append(t)
        
#         elif t == ')':
#             while stack and stack[-1] != '(':
#                 answer += stack.pop()
#             stack.pop()
# while stack:
#     answer += stack.pop()
# print(answer)


# import math

# s = ['  *   ', ' * *  ', '***** ']

# def make_fractal(shift):
#     c = len(s)
#     for i in range(c):
#         s.append(s[i] + s[i])
#         s[i] = ("   " * shift + s[i] + "   " * shift)
#         # for j in s:
#         #     print(j)
#         # print("----------------------------------")

# n = int(input())
# k = int(math.log(int(n / 3), 2))
# for i in range(k):
#     make_fractal(int(pow(2, i)))
# for i in range(n):
#     print(s[i])


# T = int(input())
# for _ in range(T):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(2)]

#     arr[0][1] += arr[1][0]
#     arr[1][1] += arr[0][0]

#     for j in range(2,N):
#         arr[0][j] += max(arr[1][j-1],arr[1][j-2])
#         arr[1][j] += max(arr[0][j-1],arr[0][j-2])
    
#     print(max(arr[0][N-1],arr[1][N-1]))

# import sys
# from collections import deque

# input = lambda : sys.stdin.readline().rstrip()
# T = int(input())
# q = deque()
# for _ in range(T):
#     temp = input().split()
    
#     if temp[0] == "push_front":
#         q.appendleft(int(temp[1]))
#     elif temp[0] == "push_back":
#         q.append(int(temp[1]))

#     elif temp[0] == "pop_front":
#         print(q.popleft() if q else -1)
#     elif temp[0] == "pop_back":
#         print(q.pop() if q else -1)

#     elif temp[0] == "front":
#         print(q[0] if q else -1)
#     elif temp[0] == "back":
#         print(q[-1] if q else -1)
    
#     elif temp[0] == "size":
#         print(len(q))
#     elif temp[0] == "empty":
#         print(0 if q else 1)

# import sys
# from itertools import permutations
# N = int(input())
# K = int(input())
# a = [input() for _ in range(N)]

# # 오류
# # 예외 (2,12) , (21,2)
# print(set(permutations(a,K)))
# print(len(set(permutations(a,K))))

# answer = set()
# for line in list(permutations(a,K)):
#     answer.add(''.join(line))
# print
# print(len(answer))

# print(len(set([''.join(j)for j in permutations(a,K)])))

# from itertools import combinations
# N, S = map(int,input().split())
# arr = list(map(int,input().split()))
# answer = 0
# for i in range(1,N+1):
#     for j in combinations(arr,i):
#         answer += 1 if sum(j) == S else 0

# print(answer)

# N = int(input())
# dp = [[] for _ in range(N+1)]

# dp[1].append(1)
# for i in range(2,N+1):

#     dp[i] = dp[i-1] + [i]
#     if i % 2 == 0:
#         temp =  dp[i//2] + [i]
#         if len(temp) < len(dp[i]):
#             dp[i] = temp
#     if i % 3 == 0:
#         temp =  dp[i//3] + [i]
#         if len(temp) < len(dp[i]):
#             dp[i] = temp

# print(len(dp[N])-1)
# print(*dp[N][::-1])

# import sys
# import heapq

# numbers = int(input())
# heap = []

# for _ in range(numbers):
#     num = int(sys.stdin.readline())
#     if num != 0:
#         heapq.heappush(heap, -num)
#     else:
#         try:
#             print(-heapq.heappop(heap))
#         except:
#             print(0)

# A,B,V = map(int,input().split())
# k = (V-B)/(A-B)
# print( int(k) if k == int(k) else int(k)+1)


# T = int(input())
# for _ in range(T):
#     H,W,N = map(int,input().split())
#     a = N%H
#     b = N//H+1
#     if a == 0: 
#         a = H
#         b -= 1
#     print(a*100 + b)



# T = int(input())

# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     people = [ i for i in range(1, n+1)]
#     for __ in range(k):
#         for j in range(1,n):
#             people[j] += people[j-1]

#     print(people[-1])

# print(sum(map(int,input().split())))

# x,y,w,h = map(int,input().split())
# print(min(x,y,abs(w-x),abs(h-y)))

# import math
# r = int(input())
# print(f'{r*r*math.pi:.6f}')
# print(f'{r*r*2:.6f}')


# x = y = 0
# for _ in range(3):
#     nx,ny = map(int,input().split())
#     x ^= nx
#     y ^= ny
# print(x,y)

# while True:
#     arr = list(map(int,input().split()))
#     if not all(arr):
#         break
#     arr.sort()
#     if arr[2]**2 == arr[0]**2 + arr[1]**2:
#         print("right")
#     else:
#         print("wrong")


# def solution(arr):
#     result = -64
#     for i in range(4):
#         for j in range(4):
#             result = max(result, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
#     return result

# from collections import deque

# def rotLeft(a, d):
#     temp = deque(a)
#     temp.rotate(-d)
#     return temp

# def rotLeft(a, d):
#     return a[d:]+a[:d]

# n = int(input())
# numbers = list(map(int,input().split()))
# answer = 0
# for num in numbers:
#     flag = True
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 flag = False
#                 break
#         if flag:
#             answer += 1
# print(answer)

# def check(n):
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# N = int(input())
# M = int(input())

# answer = []
# for number in range(N,M+1):
#     if check(number):
#         answer.append(number)
# if answer:
#     print(sum(answer))
#     print(min(answer))
# else:
#     print(-1)

# arr =[False, False] + [True]*9999

# for i in range(2,101):
#     if arr[i]:
#         for j in range(i*2,len(arr),i):
#             arr[j] = False
# m = int(input())
# n = int(input())
# nums = [i for i in range(m,n+1) if arr[i]]
# if nums:
#     print(sum(nums))
#     print(min(nums))
# else:
#     print(-1)

# 1564 ms
# N = int(input())
# div = 2
# while N != 1:
#     while N % div == 0:
#         N //= div
#         print(div)
#     div += 1

# 72 ms
# N = int(input())
# div = 2
# # 이부분?
# r = int(N ** 0.5)
# while div <= r:
#     while not N % div:
#         print(div)
#         N //= div
#     div += 1
# if N > 1:
#     print(N)

# # 1929
# # 3928 ms >> 104ms 수정필요
# def check(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True

# N,M = map(int,input().split())
# for num in range(N,M+1):
#     if check(num):
#         print(num)

# def check(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True

# li = list(range(2,246912))
# prime_li = []
# for i in li:
#     if check(i):
#         prime_li.append(i)

# while True:
#     N = int(input())
#     answer = 0
#     if N == 0:
#         break

#     for num in prime_li:
#         if N < num <= 2*N:
#             answer += 1
#         elif num > 2*N:
#             break
#     print(answer)

### 9020
# prime_li = [0 for i in range(10001)]
# prime_li[1] = 1

# for i in range(2,98):
#     for j in range(i*2, 10001,i):
#         prime_li[j] = 1

# T = int(input())
# for _ in range(T):
#     a = int(input())
#     b = a // 2
#     for j in range(b,1,-1):
#         if prime_li[a-j] == 0 and prime_li[j] == 0:
#             print(j,a-j)
#             break

### 1011
# T = int(input())
# for _ in range(T):
#     a,b = map(int,input().split())
#     c = b - a
#     n = 1
#     while True:
#         if n ** 2 <= c < (n + 1) ** 2:
#             break
#         n += 1
#     if n ** 2 == c:
#         print((n * 2) - 1)
#     elif n ** 2 < c <= n ** 2 + n:
#         print(n * 2)
#     else:
#         print((n * 2) + 1)

# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     if b % a == 0:
#         print("factor")
#     elif a % b == 0:
#         print("multiple")
#     else:
#         print("neither")

# N = int(input())
# arr = list(map(int,input().split()))
# arr.sort()
# print(arr[0]*arr[-1])

# 유클리드 호제법
# 최대 공약수
# a와 b(a>b) 의 최대 공약수 G는 b와 a%b의 최대 공약수 G과 서로 같다.
# 최소 공배수
# a == x*G / b == y*G >> (a*b)/G == (x*y*G^2) / G == x*y*G == L
# a, b = map(int,input().split())

# if a >= b:
#     A, B = a, b
# else:
#     A, B = b, a

# while B != 0:
#     A = A % B
#     A,B = B, A

# print(A)
# print(a*b//A)

# def g(a,b):
#     return g(b,a%b) if b else a

# def l(a,b):
#     return (a*b) // g(a,b)

# T = int(input())

# for _ in range(T):
#     a,b = map(int,input().split())
#     print(l(a,b))

# from math import factorial
# n, k = map(int, input().split())
# b = factorial(n) // (factorial(k) * factorial(n - k))
# print(b)

# n,k = map(int,input().split())
# a = 1
# b = 1

# while k:
#     a *= n
#     b *= k
#     n -= 1
#     k -= 1
# print(a//b)

# N, K = map(int,input().split())
# a = 1
# b = 1

# while K:
#     a *= N
#     b *= K
#     N -= 1
#     K -= 1
# print((a//b)%10007)

# arr = [16,12,17,48,85]

# for i in range(5):
#     for j in range(i+1,5):
#         print(i,j)
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j],arr[i]

# print(arr[2])

# T = int(input())
# def com(N,K):
#     a = 1
#     b = 1
#     while K:
#         a *= N
#         b *= K
#         N -= 1
#         K -= 1
#     return a//b

# for _ in range(T):
#     K, N = map(int,input().split())
#     print(com(N,K))


# from collections import Counter

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     s = []
#     for _ in range(N):
#         a, b = input().split()
#         s.append(b)
#     answer = 1
#     result = Counter(s)
#     for k in result:
#         answer *= (result[k] + 1)
#     print(answer - 1)

# def div_n(k,n):
#     cnt = 0
#     while (k != 0):
#         # print(k,cnt)
#         k //= n
#         cnt += k
#     # print("return :",cnt)
#     return cnt

# n, m = map(int,input().split())

# div_five = div_n(n,5) - div_n(m,5) - div_n(n-m,5)
# div_two = div_n(n,2) - div_n(m,2) - div_n(n-m,2)

# print(min(div_five,div_two))



# def gcd(a,b):
#     return gcd(b,a%b) if b else a

# N = int(input())
# arr = list(map(int,input().split()))

# for i in range(1,N):
#     g = gcd(arr[0],arr[i])
#     print('{}/{}'.format(arr[0]//g,arr[i]//g))

# s = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     a %= 10
#     if a != 0:
#         print(s[a][b % len(s[a])])
#     else:
#         print(10)