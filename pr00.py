import sys
input = lambda : sys.stdin.readline().rstrip()

# bj 14500 테트로미노

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
