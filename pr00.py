# 17144 17143 17142 17779 17837 19236 19237 19238

# 17144 미세먼지 
# 시간초과... 

import sys
input = lambda : sys.stdin.readline().rstrip()

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