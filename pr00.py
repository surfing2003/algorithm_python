import sys
input = lambda : sys.stdin.readline().rstrip()

# bj 14889 스타트와 링크
# 시간초과

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
select = [False] * N

min_a = sys.maxsize

def gab(l, idx ,N):
    global min_a
    if l == N//2:
        a = 0
        b = 0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    a += arr[i][j]
                elif not select[i] and not select[j]:
                    b += arr[i][j]
        min_a = min(min_a, abs(a-b))

    for i in range(idx,N):
        if select[i]:
            continue
        select[i] = True
        gab(l+1,i,N)
        select[i] = False

gab(0,0,N)
print(min_a)