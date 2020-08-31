# baekjoon_1946 신입사원

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    chk = [list(map(int,input().split())) for _ in range(n)]
    chk.sort(key=lambda x: x[0])

    cnt = 1
    min_chk = chk[0]

    for i in range(1,n):
        if min_chk[1] > chk[i][1]:
            min_chk = chk[i]
            cnt += 1

    print(cnt)
