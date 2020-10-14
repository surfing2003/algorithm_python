import sys
input = lambda : sys.stdin.readline().rstrip()

# bj 14502 연구소
# 다시 구현해보자. 
import copy
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = [[i,j] for i in range(N) for j in range(M) if lab[i][j]==2]
# 위, 오른쪽, 아래, 왼쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]
max_safe = 0

# 안전구역 구하기
def getSafeArea(copy_lab):
    safe = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:
                safe += 1
    return safe

# 바이러스 퍼지기
def spread(x,y,copy_lab):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < M:
            if copy_lab[nx][ny] == 0:
                copy_lab[nx][ny] = 2
                spread(nx,ny,copy_lab)

# 벽 세우기
def wall(start,depth):
    global max_safe

    if depth == 3:
        copy_lab = copy.deepcopy(lab)

        for i in range(len(virus)):
            v_x,v_y = virus[i]
            spread(v_x,v_y,copy_lab)
        
        max_safe = max(max_safe,getSafeArea(copy_lab))
        return
    for i in range(start,N*M):
        x = (int) (i/M)
        y = (int) (i%M)

        if lab[x][y] == 0:
            lab[x][y] = 1
            wall(i,depth+1)
            lab[x][y] = 0

wall(0,0)
print(max_safe)