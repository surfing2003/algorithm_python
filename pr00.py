
import sys
input = lambda : sys.stdin.readline().rstrip()

# 17143 17142 17779 17837 19236 19237 19238

# bj 17143 낚시왕

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