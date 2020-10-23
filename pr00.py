
import sys
input = lambda : sys.stdin.readline().rstrip()

# 17142 17779 17837 19236 19237 19238
# 17142 17837 다시풀어보기
# 삼성 2072
T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int,input().split()))
    b = sum([i for i in a if i % 2 == 1])
    print("#%d %d"%(test_case,b))