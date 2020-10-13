# baekjoon 1002 터렛 
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = (((x1-x2)**2) + ((y1-y2)**2))**0.5
    rs = r1 + r2
    rm = abs(r1 - r2)
    
    if d == 0 :
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rs or d == rm:
            print(1)
        elif d < rs and d > rm:
            print(2)
        else:
            print(0)

# bj 13458 시험감독

n = int(input())
a = list(map(int,input().split()))
b, c = map(int, input().split())

total = 0
for i in a:

    total += 1
    if i < b:
        continue
    i -= b
    total += -(-i //c)

print(total)