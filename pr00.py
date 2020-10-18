
import sys
input = lambda : sys.stdin.readline().rstrip()

# 17142 17779 17837 19236 19237 19238
# 17837 다시풀어보기
# 17142 연구소 3 - 틀림

# from collections import deque
# from itertools import combinations as cb
# import copy

# def bfs():
#     temp_arr = copy.deepcopy(arr)
#     while q:
#         x,y,t = q.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if temp_arr[nx][ny] == 0 or temp_arr[nx][ny] == "*":
#                     temp_arr[nx][ny] = t
#                     q.append([nx,ny,t+1])
    
#     for i in temp_arr:
#         if 0 in i:
#             return -1
#     return t



# N, V = map(int, input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# virus = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 2:
#             arr[i][j] = "*"
#             virus.append((i,j))
#         if arr[i][j] == 1:
#             arr[i][j] = "-"

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# answer = []
# pre = [i for i in arr if i.count(1)]
# if not pre:
#     print(0)
# else:
#     chk_list = cb(virus,V)
#     for chk in chk_list:
#         q = deque()
#         for i in range(V):
#             q.append([chk[i][0],chk[i][1],0])
#         ans = bfs()
#         if ans != -1:
#             answer.append(ans)

#     if answer:
#         print(min(answer))
#     else:
#         print(-1)

            



