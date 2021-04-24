
### 초기풀이
# def change(numbers,length):
#     dic = {
#         "A":10,
#         "B":11, 
#         "C":12,
#         "D":13,
#         "E":14,
#         "F":15
#     }
#     answer = 0

#     for i, v in enumerate(numbers):
#         if v in dic.keys():
#             answer += pow(16,(length-i-1))*dic[v]
#         else:
#             answer += pow(16,(length-i-1))*int(v)
#     return answer
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, K = map(int,input().split())
#     number = list(input())
#     number += number

#     length = N // 4
#     chk = set()

#     for i in range(length):
#         for j in range(0,N,length):
#             chk.add(change(number[(j+i):(j+i+length)],length))
#     print("#"+str(test_case),sorted(list(chk),reverse=True)[K-1])

# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int,input().split())
#     number = list(input())

#     length = N // 4
#     chk = set()

#     for _ in range(length):
#         for i in range(4):
#             chk.add(''.join(number[(i*length):(i+1)*length]))
#         number.append(number.pop(0))
#     my_list = []
#     for i in chk:
#         my_list.append(int(i,16))
#     my_list.sort(reverse=True)
#     print("#{} {}".format(test_case,my_list[K-1]))

# from itertools import product
# from copy import deepcopy

# def WH_check(x,y):
#     return not (x<0 or y<0  or x>H-1 or y>W-1)

# def search(y, blocks):
#     q = []
#     x = 0

#     while WH_check(x,y) and blocks[x][y] == 0:
#         x += 1
    
#     if x == H:
#         return blocks

#     q.append([blocks[x][y],x,y])
#     blocks[x][y] = 0
#     while q:
#         k,x,y = q.pop(0)
#         for i in range(4):
#             for t in range(1,k):
#                 nx = x+(t*dx[i])
#                 ny = y+(t*dy[i])
#                 if WH_check(nx,ny) and blocks[nx][ny] != 0:
#                     q.append([blocks[nx][ny],nx,ny])
#                     blocks[nx][ny] = 0
#     return blocks

# def swap(blocks):
#     before = list(zip(*blocks))
#     after = []
#     for b in before:
#         temp = [i for i in b if i != 0]
#         after.append([0]*(H-len(temp))+temp)
#     return [list(i) for i in zip(*after)]


# T = int(input())
# for test_case in range(1, T + 1):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     N, W, H = map(int,input().split())
#     blocks = [list(map(int,input().rstrip().split())) for _ in range(H)]
#     answer = W*H

#     for case in product(range(W),repeat=N):
#         copy_block = deepcopy(blocks)
#         for c in case:
#             copy_block = search(c,copy_block)
#             copy_block = swap(copy_block)
#         answer = min(answer,(W*H)-sum([i.count(0) for i in copy_block]))
#     print("#{} {}".format(test_case,answer))

# from collections import deque
# from itertools import product

# def out_check(x,y):
#     return not (x < 0 or y < 0 or x >= 4 or y >= N)

# def check(maps):
#     chk = []
#     for j in range(4):
#         if all([maps[i][j] for i in range(4)]):
#             chk.append(j)
#     return chk

# def remap(N,maps):
#     temp = [[0]*N for _ in range(4)]
#     for x in range(4):
#         for y in range(N):
#             if maps[x][y] != 0:
#                 for k in direction[maps[x][y]]:
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if out_check(nx,ny):
#                         if temp[nx][ny] == 0:
#                             temp[nx][ny] = maps[x][y]
#                             break
#                         else:
#                             temp[nx][ny] = min(maps[x][y],temp[nx][ny])
#                             break
#     for i in temp:
#         if i.count(0) == N:
#             continue
#         else:
#             while i[0] == 0:
#                 i.pop(0)
#                 i.append(0)
#     return temp
# def remap2(N,maps):
#     for i in maps:
#         if i.count(0) == N:
#             continue
#         else:
#             while i[0] == 0:
#                 i.pop(0)
#                 i.append(0)

#     return maps

# N = int(input())

# dx = [0,0,-1,-1,-1,0,1,1,1]
# dy = [0,1,1,0,-1,-1,-1,0,1]
# answer = 0
# direction = {}
# for i in range(1,9):
#     direction[i] = list(map(int,input().split()))

# blocks = []
# M = 0
# for _ in range(N):
#     k,c = map(int,input().split())
#     blocks.append((k,c))
#     if c == 0:
#         M += 1
# N *= 2
# point = list(product(range(4),repeat=M))

# for p in point:
#     p = list(p)
#     score = 0
#     maps = [[0]*N for _ in range(4)]
#     for k,c in blocks:
#         score_yn = False
#         if c != 0:
#             maps[c-1][maps[c-1].index(0)] = k
#         else:
#             c = p.pop(0)
#             maps[c][maps[c].index(0)] = k
#         for idx in check(maps):
#             score += 1
#             for i in range(4):
#                 maps[i][idx] = 0
#         maps = remap(N,maps)
#         for idx in check(maps):
#             score += 1
#             for i in range(4):
#                 maps[i][idx] = 0
#         maps = remap2(N,maps)
#     answer = max(answer,score)
# print(answer)        
            
# N = int(input())

# dp = [0] * 1000001

# dp[1] = 1
# dp[2] = 2

# for i in range(3,N+1):
#     dp[i] = (dp[i-1] + dp[i-2]) %15746
    
# print(dp[N])

# N = 21

# dp = [[[0]*N for _ in range(N)] for _ in range(N)]

# def w(a,b,c):
#     if a<=0 or b<=0 or c<=0:
#         return 1

#     if a>20 or b>20 or c>20:
#         return w(20,20,20)
    
#     if dp[a][b][c]:
#         return dp[a][b][c]
    
#     if a<b<c:
#         dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
#         return dp[a][b][c]
    
#     dp[a][b][c] = w(a-1,b,c,)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
#     return dp[a][b][c]

# while True:
#     a,b,c = map(int,input().split())
#     if a == -1 and b == -1 and  c==-1:
#         break
#     print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))


# N = int(input())

# dp = [[0]*10 for _ in range(101)]
# for i in range(1,10):
#     dp[1][i] = 1

# for i in range(2,N+1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][j+1]
#         elif j == 9:
#             dp[i][j] = dp[i-1][j-1] 
#         else:
#             dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])
        
# print(sum(dp[N]) % 1000000000)


# N = int(input())
# dp = [0] * (N+1)
# wine = [0]
# for _ in range(N):
#     wine.append(int(input()))

# dp[1] = wine[1]
# if N>1:
#     dp[2] = wine[2] + wine[1]

# for i in range(3,N+1):
#     a = dp[i-3] + wine[i-1] + wine[i]
#     b = dp[i-2] + wine[i]
#     c = dp[i-1] 
#     dp[i] = max(a,b,c)

# print(dp[N])

# N = int(input())
# lines = [list(map(int,input().split())) for _ in range(N)]
# lines.sort(key= lambda x: x[0])

# dp = [1] * N

# for i in range(1,N):
#     for j in range(0,i):
#         if lines[j][1] < lines[i][1]:
#             dp[i] = max(dp[i],dp[j]+1)

# print(N - max(dp))

# N = int(input())
# lines = [list(map(int,input().split())) for _ in range(N)]
# lines.sort(key= lambda x: x[0])

# dp = [0] * 501
# for s, d in lines:
#     dp[d] = max(dp[:d]) + 1
# print(N - max(dp))


# N = int(input())
# arr = list(map(int,input().split()))
# dp = [0] * N

# dp[0] = arr[0]
# for i in range(1,N):
#     dp[i] = max(dp[i-1]+arr[i],arr[i])
# print(max(dp))

# N = int(input())
# arr = list(map(int,input().split()))
# dp3 = [0] * 101
# for i in arr:
#     dp3[i] = max(dp3[:i]) + i
# print(max(dp3))

# a = ' '+input().upper()
# b = ' '+input().upper()

# dp = [[0] * len(b) for _ in range(len(a))]

# for i in range(1,len(a)):
#     for j in range(1,len(b)):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i-1][j-1]+1
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i][j-1])
# print(dp[-1][-1])

# N = int(input())
# arr1 = list(map(int,input().split()))
# arr2 = arr1[::-1]
# dp1 = [1] * N
# dp2 = [1] * N

# for i in range(1,N):
#     for j in range(0,i):
#         if arr1[j] < arr1[i]:
#             dp1[i] = max(dp1[i],dp1[j]+1)

# for i in range(1,N):
#     for j in range(0,i):
#         if arr2[j] < arr2[i]:
#             dp2[i] = max(dp2[i],dp2[j]+1)

# answer = 0
# for i in range(N):
#     answer = max(dp1[i]+dp2[-i-1]-1,answer)
# # print(arr1,dp1)
# # print(arr2,dp2)
# print(answer)

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# N = int(input())
# roads = list(map(int,input().split()))
# oils = list(map(int,input().split()))

# min_price = oils[0]
# total = 0
# for i in range(N-1):
#     if oils[i] < min_price:
#         min_price = oils[i]
#     total += min_price*roads[i]

# print(total)

# import sys
# N = int(input())
# answer = []
# K = list(map(int,sys.stdin.read().split()))
# for i in K:
#     if i == 0:
#         answer.pop()
#         continue
#     answer.append(i)
# print(sum(answer))

# from collections import deque
# import sys
# input = sys.stdin.readline

# N,K = map(int,input().split())

# rails = deque(map(int,input().split()))
# robot = deque([0]*N)
# answer = 0

# while True:

#     # 벨트 한칸 이동
#     rails.rotate(1)
#     robot.rotate(1)
#     robot[N-1] = 0

#     for i in range(N-2,-1,-1):
#         if (robot[i] == 1 and robot[i+1] == 0 and rails[i+1] >= 1): 
#             robot[i] = 0
#             robot[i+1] = 1
#             rails[i+1]-=1
#     robot[N-1] = 0
#     # 1위치 로봇 올리기
#     if (robot[0] == 0 and rails[0] >= 1):
#         robot[0] = 1
#         rails[0] -= 1

#     answer += 1

#     if rails.count(0) >= K :
#         break

# print(answer)

# from collections import deque
# import sys
# input = lambda : sys.stdin.readline().rstrip()

# dr = [-1,-1,0,1,1,1,0,-1]
# dc = [0,1,1,1,0,-1,-1,-1]
# N, M, K = map(int,input().split())
# arr = [[[] for _ in range(N)] for _ in range(N)]
# q = deque()
# answer = 0

# for _ in range(M):
#     r,c,m,s,d = map(int,input().split())
#     arr[r-1][c-1].append([r-1,c-1,m,s,d])
#     q.append([r-1,c-1,m,s,d])

# for _ in range(K):
#     for _ in range(len(q)):
#        r,c,m,s,d = q.popleft()
#        nr, nc = (r+s*dr[d])%N, (c+s*dc[d])%N
#        arr[nr][nc].append([nr,nc,m,s,d])
#        arr[r][c].remove([r,c,m,s,d])
    
#     for i in range(N):
#         for j in range(N):
#             if len(arr[i][j]) > 1:
#                 m = 0
#                 s = 0
#                 d = 0
#                 for k in arr[i][j]:
#                     m += k[2]
#                     s += k[3]
#                     d += (k[4] % 2)
#                 m //= 5
#                 if m != 0:
#                     s //= len(arr[i][j])
#                     if d == 0 or d == len(arr[i][j]):
#                         arr[i][j] = [[i,j,m,s,0],[i,j,m,s,2],[i,j,m,s,4],[i,j,m,s,6]]
#                     else:
#                         arr[i][j] = [[i,j,m,s,1],[i,j,m,s,3],[i,j,m,s,5],[i,j,m,s,7]]
#                 else:
#                     arr[i][j] = []
    
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != []:
#                 q += arr[i][j]
    
# for i in range(N):
#     for j in range(N):
#         for k in arr[i][j]:
#             answer += k[2]
# print(answer)

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# rate_left = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
# rate_down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,'a',10,0],[0,0,5,0,0]]
# rate_right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
# rate_up = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]


# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]

# def move(answer,arr,rate,nx,ny):
#     a, b = nx-2, ny-2
#     temp = 0
#     for i in range(5):
#         for j in range(5):
#             if rate[i][j] != 'a' and rate[i][j] != 0:
#                 if -1 < i+a < N and -1 < j+b < N:
#                     arr[i+a][j+b] += arr[nx][ny] * rate[i][j] // 100
#                 else:
#                     answer += arr[nx][ny] * rate[i][j] // 100
#                 temp += arr[nx][ny] * rate[i][j] // 100
#             elif rate[i][j] == 'a':
#                 point = (i,j)
    
#     if -1 < point[0]+a < N and -1 < point[1]+b < N:
#         arr[point[0]+a][point[1]+b] += arr[nx][ny] - temp
#     else:
#         answer += arr[nx][ny] - temp
#     arr[nx][ny] = 0
#     return arr, answer

# x, y = N//2, N//2

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# time = 1
# flag = 0
# answer = 0
# while flag != 1:
#     for i in range(4):
#         for j in range(time):
#             x, y = x+dx[i], y+dy[i]
#             if i == 0:
#                 arr,answer = move(answer,arr,rate_left,x,y)
#             elif i == 1:
#                 arr,answer = move(answer,arr,rate_down,x,y)
#             elif i == 2:
#                 arr,answer = move(answer,arr,rate_right,x,y)
#             elif i == 3:
#                 arr,answer = move(answer,arr,rate_up,x,y)
            
#             if (x,y) == (0,0):
#                 flag = 1
#                 break
#         if i == 1 or i == 3:
#             time += 1
#         if flag == 1:
#             print(answer)
#             break

# from collections import deque

# dir = [(1,0),(0,1),(-1,0),(0,-1)]
# n, q = map(int,input().split())
# n = 2**n
# arr = [ list(map(int,input().split())) for i in range(n)]

# for l in list(map(int,input().split())):
#     k = 2**l
#     for x in range(0,n,k):
#         for y in range(0,n,k):
#             temp = [arr[i][y:y+k] for i in range(x,x+k)]
#             for i in range(k):
#                 for j in range(k):
#                     arr[x+j][y+k-1-i] = temp[i][j]

#     cnt = [[0] * n for _ in range(n)]
#     for x in range(n):
#         for y in range(n):
#             for d in dir:
#                 nx = x + d[0]
#                 ny = y + d[1]
#                 if 0<=nx<n and 0<=ny<n and arr[nx][ny]:
#                     cnt[x][y] += 1

#     for x in range(n):
#         for y in range(n):
#             if arr[x][y] > 0 and cnt[x][y] < 3:
#                 arr[x][y] -= 1


# print(sum(sum(i) for i in arr))

# visited = [[False]*n for _ in range(n)]
# answer = 0
# for i in range(n):
#     for j in range(n):
#         q = deque()
#         if not visited[i][j] and arr[i][j] != 0:
#             q.append([i,j])
#             visited[i][j] = True
#             cnt = 1

#             while q:
#                 x,y = q.popleft()
#                 for d in dir:
#                     nx = x+d[0]
#                     ny = y+d[1]
#                     if -1<nx<n and -1<ny<n and not visited[nx][ny] and arr[nx][ny] != 0:
#                         q.append([nx,ny])
#                         visited[nx][ny] = True
#                         cnt += 1

#             answer = max(answer,cnt)
# print(answer)

# def choose(S,temp):
#     if len(temp) == 6:
#         print(*temp)
#         return

#     for i in S:
#         if len(temp) == 0:
#             temp.append(i)
#             choose(S,temp)
#             temp.pop()

#         else:
#             if temp[-1]  < i:
#                 temp.append(i)
#                 choose(S,temp)
#                 temp.pop()


# while True:
#     S = list(map(int,input().split()))
#     if S[0] == 0:
#         break
    
#     temp = []

#     choose(S[1:],temp)
#     print()

# L,C = map(int,input().split())
# chars = input().split()
# chars.sort()
# temp = []

# def check(temp):
#     a = 0
#     b = 0
#     for i in temp:
#         if i in ['a','e','i','o','u']:
#             a += 1
#         else:
#             b += 1
#     return (a>0 and b>1)

# def choose(idx,cnt,temp):
#     if cnt == L and check(temp):
#         print(''.join(temp))
#         return

#     for i in range(idx,C):
#         temp.append(chars[i])
#         choose(i+1,cnt+1,temp)
#         temp.pop()    

# choose(0,0,temp)


# R,C = map(int,input().split())
# arr = [list(input()) for _ in range(R)]
# temp = [ord(arr[0][0])]
# visited = [[False]*C for _ in range(R)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# answer = 0

# def choose(x,y,temp,c):
#     global answer
#     answer = max(answer,c)

#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if -1<nx<R and -1<ny<C:
#             t = ord(arr[nx][ny])
#             if t not in temp:
#                 temp.append(t)
#                 choose(nx,ny,temp,c+1)
#                 temp.pop()

# choose(0,0,temp,1)
# print(answer)