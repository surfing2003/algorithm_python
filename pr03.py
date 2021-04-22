
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
            

from itertools import combinations

N = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2]) %15746
    
print(dp[N])
