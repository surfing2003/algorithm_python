# baekjoon 2440 별찍기-3
n = int(input())
for i in range(n):
    print('*'*(n-i))

# baekjoon 1316 그룹단어체커
import sys
input = lambda : sys.stdin.readline().rstrip()

# 내풀이
n = int(input())
answer = 0
for _ in range(n):
    word = input()
    word_length = len(word)

    for j in range(word_length):
        if j != word_length-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer += 1 
print(answer)

# 참고풀이
# word를 리스트로 바꾸고 
# word.find 를 키로 정렬한 값과 비교하게되면
# 기존위치는 그대로, 연속되는 것도 그대로, 하지만 건너뛰고 있는 알파벳에 대해서는 정렬순서에 의해 리스트 값이 달라짐.
result = 0
n = int(input())
for i in range(n):
    word = input()
    print(list(word))
    print(sorted(word,key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

# 책예시4_그냥
import sys
input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# moves = list(input().split())
# start_x = 1
# start_y = 1

# for move in moves:
#     if move == 'U' and start_x -1 > 0:
#         start_x -= 1
#     if move == 'D' and start_x +1 <= n:
#         start_x += 1
#     if move == 'L' and start_y -1 > 0:
#         start_y -= 1
#     if move == 'R' and start_y +1 <= n:
#         start_y += 1

# print(start_x,start_y)

x, y =1,1
n = int(input())
moves = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx <1 or ny <1 or nx> n or ny >n:
        continue

    x,y = nx,ny
print(x,y)

# 책예시 5
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

count =0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)

# 책예시 6
import sys
input = lambda : sys.stdin.readline().rstrip()

now = input()

x = int(now[1])
y = ord(now[0]) - 96

dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        answer += 1

print(answer)

# 책예시 7
import sys
input = lambda : sys.stdin.readline().rstrip()

n,m = map(int,input().split())

chk = [[False] * m for _ in range(n)]
# 0:북 1:동 2:남 3:서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

x,y,d = map(int,input().split())

array= []
for _ in range(n):
    array.append(list(map(int,input().split())))

chk[x][y] = True

def turnleft():
    global d
    d -= 1
    if d == -1:
        d = 3
    
count = 1
turn_time = 0

while True:
    turnleft()
    nx = x+dx[d]
    ny = y+dy[d]

    if not chk[nx][ny] and array[nx][ny] == 0:
        chk[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x -dx[d]
        ny = y -dy[d]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time=0
print(count)


# bj 3190 뱀
from collections import deque

def change(d,c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

n = int(input())
k = int(input())
maps = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = list(map(int,input().split()))
    maps[x-1][y-1] = 1

l = int(input())
control = {}
for _ in  range(l):
    t, d = input().split()
    control[int(t)] = d

dx = [-1,0,1,0]
dy = [0,1,0,-1]

direction = 1
time = 1
x,y = 0, 0
visited = deque([[x,y]])
maps[x][y] = 2
while True:
    x, y = x+dx[direction] ,y+dy[direction]
    if 0 <= y < n and 0 <=  x < n and maps[x][y] != 2:
        if not maps[x][y]:
            temp_x, temp_y = visited.popleft()
            maps[temp_x][temp_y] = 0
        maps[x][y] = 2
        visited.append([x,y])
        if time in control.keys():
            direction = change(direction, control[time])
        time += 1
    else:
        break

print(time)

# bj 14499 주사위 굴리기

N, M, r, c, K = map(int,input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# 오른쪽(동) 왼쪽(서) 위(남) 아래(북)

dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]
dice = [0, 0, 0, 0, 0, 0]
time = list(map(int,input().split()))

for t in time:
    nr = r + dr[t]
    nc = c + dc[t]

    if (nr < 0 or nr >= N) or (nc < 0  or nc >= M):
        continue
    
    # 주사위 굴리는 부분을 확인하고 알맞게 서로의 위치를 바꿔주는거 신경쓰기
    if t == 1:
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif t == 2:
        dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif t == 3:
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
    elif t == 4:
        dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]

    if maps[nr][nc] == 0:
        maps[nr][nc] = dice[5]
    else:
        dice[5] = maps[nr][nc]
        maps[nr][nc] = 0
    r, c = nr, nc
    print(dice[0])

# bj 14500 테트로미노
# dfs 쓰는게 정석인거 같은데 
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

max_sum = -1

for i in range(N):
    for j in range(M):
        
        if i+3 < N :
            max_sum = max(max_sum, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j])
        if j+3 < M :
            max_sum = max(max_sum, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3])

        if i+1 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1])

        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1])
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j])
        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1])
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])

        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1])
        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j])                    
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2])
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j+1]+arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1])

        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1])
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])
        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+1][j+1])
        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1])

        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i+2][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1])
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])
        if i+2 < N and j+1 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+2][j])
        if i+1 < N and j+2 < M:
            max_sum = max(max_sum,arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+2])
print(max_sum)


# bj 14503 로봇청소기

N,M = map(int,input().split())
x,y,d = map(int,input().split()) 

arr = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
cnt = 0
while True:
    if cnt == 4:
        nd = (d+2) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        
        if arr[nx][ny] == 2:
            x,y,d,cnt = nx,ny,d,0
        else:
            break

    if arr[x][y] == 0:
        answer += 1
        arr[x][y] = 2
    
    nd = (d+3) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]

    if arr[nx][ny] == 0:
        x,y,d,cnt = nx,ny,nd,0
    else:
        x,y,d,cnt = x,y,nd,cnt+1

print(answer)


# 17144 미세먼지 
# pypy3 통과

R, C, T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

# 위치 찾기
for i in range(R):
    if arr[i][0] == -1:
        air_up = i
        air_down = i+1
        break

# 확산방향
di = [0,1,0,-1]
dj = [1,0,-1,0]

for _ in range(T):
    # 확산먼지 저장
    temp_arr = [[0]*C for _ in range(R)]

    # 확산
    for i in range(R):
        for j in range(C):
            if (i == air_up or i == air_down) and j == 0:
                continue        
            t = 0
            if arr[i][j] != 0:
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]

                    if 0<= ni < R and 0<= nj < C and arr[ni][nj] != -1:
                        temp_arr[ni][nj] += arr[i][j] // 5
                        t += 1
                arr[i][j] -= t * (arr[i][j] // 5)

    # 적용
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp_arr[i][j]

    # 위쪽바람
    # 열 0
    for i in range(air_up-1,0,-1):
        arr[i][0] = arr[i-1][0]
    # 행 0
    for i in range(C-1):
        arr[0][i] = arr[0][i+1]

    # 열 C
    for i in range(0,air_up):
        arr[i][C-1] = arr[i+1][C-1]

    # 행 air_up
    for i in range(C-1,0,-1):
        arr[air_up][i] = arr[air_up][i-1]
        if i == 1:
            arr[air_up][i] = 0

    # 아래쪽바람
    # 열 0
    for i in range(air_down+1,R-1):
        arr[i][0] = arr[i+1][0]

    # 행 마지막
    for i in range(C-1):
        arr[R-1][i] = arr[R-1][i+1]

    # 열 C
    for i in range(R-1,air_down,-1):
        arr[i][C-1] = arr[i-1][C-1]

    # 행 air_down
    for i in range(C-1,0,-1):
        arr[air_down][i] = arr[air_down][i-1]
        if i == 1:
            arr[air_down][i] = 0

answer = sum([sum(i) for i in arr]) + 2
print(answer)

# bj 17143 낚시왕
# pypy3
R,C,M = map(int,input().split())
arr = [[0]*C for _ in range(R)]
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    arr[r-1][c-1] = [s,d,z]
# (r-1,c-1) 상어위치 // s 속력(), d 이동방향, z 크기
# 1 위 2 아래 3 오른쪽 4 왼쪽
# 결과
score = 0

di = [0,-1,1,0,0]
dj = [0,0,0,1,-1]

# 낚시왕 이동 
for t in range(C):
    # 상어잡기
    for i in range(R):
        if arr[i][t] != 0:
            score += arr[i][t][2]
            arr[i][t] = 0
            M -= 1
            break
    
    # 상어이동
    temp_arr = [[0]* C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 :
                x,y,s,d,z = i,j, *arr[i][j]
                while s > 0:
                    x += di[d]
                    y += dj[d]
                    if 0<= x < R and 0<= y < C:
                        s-=1
                    else:
                        x -= di[d]
                        y -= dj[d]
                        if d == 1: d =2
                        elif d == 2: d =1
                        elif d == 3: d =4
                        elif d == 4: d =3
                
                if temp_arr[x][y] == 0:
                    temp_arr[x][y] = [arr[i][j][0],d,z]
                else:
                    if temp_arr[x][y][2] < z:
                        temp_arr[x][y] = [arr[i][j][0],d,z]
    arr = temp_arr

print(score)


# bj 17837 새로운 게임 
# 다시 풀어보기
# 주요포인트 : 위치를 key로 하는 딕셔너리
#         : 말을 key로 활용해서 따로 관리하는 딕셔너리
import sys
input = lambda : sys.stdin.readline().rstrip()

# N * N 
# K개의 말 
# 체스판 : 흰 빨 파
# 이동방향 : 상하좌우
# 턴 한번 > 1~K까지 순서대로 이동
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
# 말이 4개이상 쌓이는 순간 게임 종료

# 맨앞이 가장 바닥 > stack 인듯

# 이동칸이 흰색인 경우
# 칸에 말이 있는 경우 이동하는 말을 위로 
# 기존 DE 이동 ABC  이동후 DEABC

# 이동칸이 빨간색인 경우
# 이동 후 순서 반전
# ABC > 이동칸에 아무도없으면 CBA
# ADFG > 이동칸에 ECB이 있으면 ECBGFDA

# 이동칸이 파란색인 경우
# A번 말의 이동 방향을 반대로하고 한칸 이동
# 반대로 바꾼후에 이동하려는 칸이 파란색인경우에는 이동하지않고 가만히 있는다.
# 벽을 벗어나는 경우도 파란색과 같은 경우

#종료조건 턴 > 1000 / 종료되지 않을 경우 -1


# 0 오 왼 상 하
dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]

N, K = map(int, input().split())

# 0 흰색 : 단순이동 / 1 빨간 : stack 역순 / 2 파랑 : 벽과같은 역할
arr = [list(map(int,input().split())) for _ in range(N)]

stone_arr = {(i,j):[] for j in range(N) for i in range(N)}
stone = {}
for i in range(K):
    r,c,d = map(int,input().split())
    stone_arr[(r-1,c-1)].append(i)
    stone[i] = [r-1,c-1,d]

def rev_d(d):
    if d == 1: d = 2
    elif d == 2: d = 1
    elif d == 3: d = 4
    elif d == 4: d = 3
    return d

def s():
    turn = 0
    P = 0
    while True:
        turn += 1
        if turn > 1000: 
            return -1
        for number in  range(K):
            x,y,d = stone[number]
            nx,ny = x+dx[d],y+dy[d]

            if  not 0 <= nx < N or not 0 <= ny < N or arr[nx][ny] == 2:
                d = rev_d(d)
                nx,ny = x+dx[d], y+dy[d]
                if  not 0 <= nx < N or not 0 <= ny < N or arr[nx][ny] == 2:
                    stone[number][2] = d
                    continue
                P = 1
            if arr[nx][ny] == 0:
                left = stone_arr[(x,y)][:stone_arr[(x,y)].index(number)]
                right = stone_arr[(x,y)][stone_arr[(x,y)].index(number):]            
                stone_arr[(x,y)] = left
                stone_arr[(nx,ny)].extend(right)
                if len(stone_arr[(nx,ny)]) >= 4: 
                    return turn
                for i in right:
                    stone[i][0], stone[i][1] = nx,ny
                if P == 1: 
                    stone[number][2] = d
                P = 0
            elif arr[nx][ny] ==1:
                left = stone_arr[(x,y)][:stone_arr[(x,y)].index(number)]
                right = stone_arr[(x,y)][stone_arr[(x,y)].index(number):]            
                stone_arr[(x,y)] = left
                right.reverse()
                stone_arr[(nx,ny)].extend(right)
                if len(stone_arr[(nx,ny)]) >= 4: 
                    return turn
                for i in right:
                    stone[i][0], stone[i][1] = nx,ny
                if P == 1: 
                    stone[number][2] = d
                P = 0
print(s())
