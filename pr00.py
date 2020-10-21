
import sys
input = lambda : sys.stdin.readline().rstrip()

# 17142 17779 17837 19236 19237 19238
# 17142 17837 다시풀어보기

# bj-10953
# N = int(input())
# for _ in range(N):
#     a,b = map(int,input().split(','))
#     print(a+b)

# bj-11718 11719
while True:
    try:
        print(input())
    except EOFError:
        break

# bj-11023 11024
N = int(input())
for _ in range(N):
    print(sum(list(map(int,input().split()))))