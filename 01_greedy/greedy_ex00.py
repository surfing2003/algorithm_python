# baekjoon 1138 한줄서기
# 작은 순서부터 위치를 정해가면 되는 문제
# 앞에 경우는 신경 쓰지 않고 인덱스 배열에서 나의 위치값만 가져가면 되는 부분 
# 위치값이 겹치더라도 앞서 먼저 사라진 위치값은 나의 왼쪽 결과에 아무런 영향 X
# 

#         h_chk = [-1,2,1,1,0]              index = [0,1,2,3]
# i = 1   h_chk[i] = 2   index.pop(2) = 2   index = [0,1,3]    result = [-1,-1,1,-1]
# i = 2   h_chk[i] = 1   index.pop(1) = 1   index = [0,3]      result = [-1,2,1,-1]
# i = 3   h_chk[i] = 1   index.pop(1) = 3   index = [0]        result = [-1,2,1,3]
# i = 4   h_chk[i] = 0   index.pop(0) = 0   index = []         result = [4,2,1,3]

# import sys
# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# h_chk = list(map(int,input().split()))
# result = [-1]*n
# index = list(range(n))

# for i in range(n):
#     result[index.pop(h_chk[i])] = i+1

# print(' '.join(str(e) for e in result))

# baekjoon 1080 행렬
# 다시 풀어보기...
import sys
input = lambda: sys.stdin.readline().rstrip()

n , m = map(int, input().split())
mat_1 = [list(input()) for _ in range(n)]
mat_2 = [list(input()) for _ in range(n)]
chk = [[mat_1[i][j]==mat_2[i][j] for j in range(m)] for i in range(n)]


