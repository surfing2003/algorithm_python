# N = int(input())

# for i in range(N):
#     print(' '*(i)+'*'*(N-i))

# N = int(input())

# for i in range(N):
#     print(' '*(N-i-1)+'*'*((2*i)+1))


# N = int(input())

# for i in range(N,0,-1):
#     print(' '*(N-i)+'*'*((2*i)-1))

# N = int(input())

# for i in range(N):
#     print(' '*i+'*'*((2*(N-i))-1))

# N = int(input())

# for i in range(N):
#     print(' '*(N-i-1)+'*'*((2*i)+1))

# for i in range(1,N):
#     print(' '*i+'*'*((2*(N-i))-1))

# N = int(input())

# for i in range(1,N):
#     temp = '*'*i + ' '*(N-i)
#     print(temp+temp[::-1])
# for i in range(N,0,-1):
#     temp = '*'*i + ' '*(N-i)
#     print(temp+temp[::-1])

# N = int(input())

# for i in range(1,N):
#     print('*'*i+' '*(2*N-i*2)+'*'*i)
# for i in range(N,0,-1):
#     print('*'*i+' '*(2*N-i*2)+'*'*i)

# N = int(input())

# for i in range(N):
#     print(' '*i+'*'*(2*(N-i)-1))
# for i in range(N-2,-1,-1):
#     print(' '*i+'*'*(2*(N-i)-1))

# N = int(input())
# for i in range(-N+1,N):
#     print(i)
#     print(' '*(N-abs(i)-1) + '*'*(2*abs(i)+1))

################# 시간복잡도 확인
# 752ms
# N, M = map(int,input().split())
# num = 1
# for _ in range(N):
#     for _ in range(M):
#         if num % M == 0:
#             print(num,end = '')
#         else:
#             print(num,end = ' ')
#         num += 1
#     print()

# 556ms
# N,M = map(int,input().split())

# for i in range(N):
#     print(*[ M*i+j+1 for j in range(M)])

# 308ms
# n, m = map(int, input().split())
# for i in range(1, 1 + n*m, m):
#     print(' '.join(map(str, range(i, i+m))))
####################################################

# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")

# print("    8888888888  888    88888")
# print("   88     88   88 88   88  88")
# print("    8888  88  88   88  88888")
# print("       88 88 888888888 88   88")
# print("88888888  88 88     88 88    888888")
# print("")
# print("88  88  88   888    88888    888888")
# print("88  88  88  88 88   88  88  88")
# print("88 8888 88 88   88  88888    8888")
# print(" 888  888 888888888 88  88      88")
# print("  88  88  88     88 88   88888888")

# print(".  .   .")
# print("|  | _ | _. _ ._ _  _")
# print("|/\|(/.|(_.(_)[ | )(/.")

# print("     /~\\")
# print("    ( oo|")
# print("    _\\=/_")
# print("   /  _  \\")
# print("  //|/.\\|\\\\")
# print(" ||  \\ /  ||")
# print("============")
# print("|          |")
# print("|          |")
# print("|          |")

# print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
# print("N2 Bomber      Heavy Fighter  Limited    21        ")
# print("J-Type 327     Light Combat   Unlimited  1         ")
# print("NX Cruiser     Medium Fighter Limited    18        ")
# print("N1 Starfighter Medium Fighter Unlimited  25        ")
# print("Royal Cruiser  Light Combat   Limited    4         ")

# print("NFC West       W   L  T")
# print("-----------------------")
# print("Seattle        13  3  0")
# print("San Francisco  12  4  0")
# print("Arizona        10  6  0")
# print("St. Louis      7   9  0")
# print()
# print("NFC North      W   L  T")
# print("-----------------------")
# print("Green Bay      8   7  1")
# print("Chicago        8   8  0")
# print("Detroit        7   9  0")
# print("Minnesota      5  10  1")


# def solution(lottos, win_nums):
#     t = [6,6,5,4,3,2,1]
    
#     z = lottos.count(0)
#     temp = 0
#     for i in lottos:
#         if i in win_nums:
#             temp += 1
    
#     return t[temp+z],t[temp]

# from itertools import combinations

# def check(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
    
# def solution(nums):

#     answer = 0
#     for i in combinations(nums,3):
#         if check(sum(i)):
#             answer += 1
    
#     return answer

# def solution(nums):
#     n_1 = len(set(nums))
#     n_2 = len(nums)//2
#     return n_2 if n_1 >= n_2 else n_1

# def solution(nums):
#     return min(len(set(nums)),len(nums)//2)

# K, N = map(int,input().split())
# lans = [ int(input()) for _ in range(K)]
# start, end = 1, max(lans)

# while start <= end:
#     mid = (start+end)//2
#     lines = 0
#     for lan in lans:
#         lines += lan // mid

#     if lines >= N:
#         start = mid + 1
#     else:
#         end = mid - 1

# print(end)

# N, M = map(int,input().split())
# trees = list(map(int,input().split()))

# start = 0
# end = max(trees)

# answer = []
# while not end < start:

#     mid = (start+end)//2
#     log = sum(i-mid if i > mid else 0 for i in trees)

#     if log == M:
#         answer.append(mid)
#         break
#     elif log > M:
#         answer.append(mid)
#         start = mid + 1
#     else:
#         end = mid - 1
# print(max(answer))

# print(ord("a")-96,ord("z")-96)

# N = int(input())
# s = input()
# answer = 0
# for i in range(N):
#     answer += ((ord(s[i])-96) * (31**i)) % 1234567891
# print(answer % 1234567891)

# dict 사용
# N = int(input())
# cards = input().split()
# dict_cards = {}
# for i in cards:
#     if i in dict_cards.keys():
#         dict_cards[i] += 1
#     else:
#         dict_cards[i] = 1

# M = int(input())
# check_cards = input().split()
# for i in check_cards:
#     if i in dict_cards.keys():
#         print(dict_cards[i],end=' ')
#     else:
#         print(0,end=" ")

# 카운터 사용
# from collections import Counter
# N = int(input())
# N_list = input().split()
# M = int(input())
# M_list = input().split()

# C = Counter(N_list)
# print(' '.join(f'{C[m]}' if m in C else '0' for m in M_list))
# print(' '.join(str(C[m]) if m in C else '0' for m in M_list))

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# N,M,B = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]

# answer = int(1e10)
# height = 0

# for l in range(257):
#     max_b = 0
#     min_b = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] < l:
#                 min_b += l-arr[i][j]
#             else:
#                 max_b += arr[i][j]-l
#     total = max_b + B
#     if total < min_b :
#         continue
#     time = 2 * max_b + min_b
#     if time <= answer:
#         answer = time
#         height = l
# print(answer,height)


# 일반적인 반복문
# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(signs)):
#         if signs[i]:
#             answer += absolutes[i]
#         else:
#             answer -= absolutes[i]
#     return answer

# zip 함수 활용
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# def solution(a, b):
#     return sum( i*j for i,j in zip(a,b) )

################# 순서대로 조건 
# def solution(new_id):
#     new_id = new_id.lower()
#     temp = ''
#     for i in new_id:
#         if i.isalnum() or i in '-_.':
#             temp += i
#     while '..' in temp:
#         temp = temp.replace('..','.')
#     if temp[0] == '.' and len(temp) > 1:
#         temp = temp[1:]
#     if temp[-1] == '.':
#         temp = temp[:-1]
#     if temp == '':
#         temp = 'a'
#     if len(temp) >= 16:
#         temp = temp[:15]
#         if temp[-1] == '.':
#             temp = temp[:-1]
#     if len(temp) <= 3:
#         temp = temp + temp[-1]*(3-len(temp))    
#     return temp

# 정규식 활용
# import re

# def solution(new_id):
#     st = new_id.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + st[-1]*(3-len(st))
#     return st

# def solution(s):
#     temp = []
#     temp.append(s[0])
#     for i in s[1:]:
#         if not temp:
#             temp.append(i)
#             continue
#         if temp[-1] == i:
#             temp.pop()
#         else:
#             temp.append(i)
#     return 1 if not temp else 0

# from collections import deque

# def bfs(start,visited,arr):
#     count = 0
#     q = deque()
#     q.append((start, count))
#     while q:
#         now,c = q.popleft()
#         if visited[now] == -1:
#             visited[now] = c
#             for i in arr[now]:
#                 q.append((i,c+1))

# def solution(n, edge):
#     answer = 0
#     visited = [-1] * (n+1)
#     arr = [[] for _ in  range(n+1)]
#     for e in edge:
#         arr[e[0]].append(e[1])
#         arr[e[1]].append(e[0])

#     bfs(1,visited,arr)
#     for v in visited:
#         if v == max(visited):
#             answer += 1
#     return answer

# print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# def solution(n, results):
#     win = {x:set() for x in range(1,n+1)}
#     lose = {x:set() for x in range(1,n+1)}
    
#     for w,l in results:
#         win[w].add(l)
#         lose[l].add(w)
    
#     for i in range(1,n+1):
#         for w in lose[i]:
#             win[w].update(win[i])
#         for l in win[i]:
#             lose[l].update(lose[i])
    
#     answer = 0
#     for i in range(1,n+1):
#         if len(win[i]) + len(lose[i]) == n-1:
#             answer += 1
#     return answer

# print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

############################### 17836
# 비효율 적인거같은데 
# from collections import deque

# N,M,T = map(int,input().split())
# arr = [input().split() for _ in range(N)]
# visited = [[-1]* M for _ in  range(N)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# q = deque()
# q.append([0,0,0])
# visited[0][0] = 0
# sword_time = -1
# while q:
#     x,y,c = q.popleft()
#     if arr[x][y] == '2':
#         sword_time = visited[x][y] + (N-1-x) + (M-1-y)

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '1' and visited[nx][ny] == -1:
#             visited[nx][ny] = c+1
#             q.append([nx,ny,c+1])

# if visited[N-1][M-1] != -1 and sword_time != -1:
#     answer = min(visited[N-1][M-1],sword_time)
#     print(answer if answer <= T else "Fail")
# elif visited[N-1][M-1] == -1 and sword_time != -1:
#     print(sword_time if sword_time <= T else "Fail")
# elif visited[N-1][M-1] != -1 and sword_time == -1:
#     print(visited[N-1][M-1] if visited[N-1][M-1] <= T else "Fail")
# else:
#     print("Fail")

# 함수
# from collections import deque

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# N,M,T = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[-1] * M for _ in range(N)]

# def bfs():
#     temp = int(1e9)
#     q = deque()
#     q.append((0,0))
#     visited[0][0] = 0

#     while q:
#         x,y = q.popleft()
#         if arr[x][y] == 2:
#             temp = (N-1-x) + (M-1-y) + visited[x][y]
#         if x == N-1 and y == M-1:
#             return min(temp,visited[x][y])
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1 and arr[nx][ny] != 1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append((nx,ny))
#     return temp

# answer = bfs()
# print("Fail" if answer > T else answer)

# 이렇게 안되는 이유 찾아보기
# from collections import deque

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# N,M,T = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[-1] * M for _ in range(N)]

# answer = int(1e9)
# q = deque()
# q.append((0,0))
# visited[0][0] = 0

# while q:
#     x,y = q.popleft()
#     if arr[x][y] == 2:
#         answer = (N-1-x) + (M-1-y) + visited[x][y]
#     if x == N-1 and y == M-1:
#         answer = min(answer,visited[x][y])
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1 and arr[nx][ny] != 1:
#             visited[nx][ny] = visited[x][y] + 1
#             q.append((nx,ny))

# print("Fail" if answer > T else answer)

#############################################################


# def solution(n, times):
#     answer = 0

#     start = 0
#     end = max(times)*n

#     while start <= end:
#         mid = (start+end)//2
#         temp = sum(mid//i for i in times)

#         if temp >= n:
#             answer = mid
#             end = mid - 1
#         elif temp < n:
#             start = mid + 1

#     return answer

# print(solution(6,[7,10]))
