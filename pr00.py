
import sys
input = lambda : sys.stdin.readline().rstrip()

# 17142 17779 17837 19236 19237 19238
# 17142 17837 다시풀어보기
# 삼성 2072

# 우선순위 큐 - 우선순위가 가장 높은 데이터를 가장먼저 삭제하는 자료구조
# 우선순위에 따라 처리하고 싶을 때 사용
# 리스트를 이용하여 구현 // 삽입 : O(1) 삭제 : O(N)
# 힙을 이용하여 구현 // 삽입 : O(logN) 삭제 : O(logN)

# Heapify()
# 원소 삽입
# 상향식 - 부모노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우 위치를 교체

# 원소 제거 
# 가장 마지막 노드가 루트 노드의 위치에 오도록 하여 
# 하향식으로 Heapify 진행

# 파이썬 min heap 기본

# 바이너리 인덱스 트리 - 2진법 인덱스 구조를 활용해 구간합문제를 효과적으로 해결
# 팬윅트리

# n = 8

# for i in range(n + 1):
#     print(i, "의 마지막 비트 : ", (i & -i))

# # 1부터 N까지 누적합 구하기 

# bj 2042
# import sys
# input = lambda : sys.stdin.readline().rstrip()

# n, m, k = map(int,input().split())

# arr = [0] * (n+1)
# tree = [0] * (n+1)

# def prefix_sum(i):
#     result = 0
#     while i > 0:
#         result += tree[i]
#         i -= (i & -i)
#     return result

# def update(i,dif):
#     while i <= n:
#         tree[i] += dif
#         i += (i & -i)

# def interval_sum(start, end):
#     return prefix_sum(end) - prefix_sum(start-1)

# for i in range(1, n+1):
#     x = int(input())
#     arr[i] = x
#     update(i,x)

# for i in range(m+k):
#     a,b,c = map(int, input().split())
#     if a == 1:
#         update(b,c-arr[b])
#         arr[b] = c
#     else:
#         print(interval_sum(b,c))


# bj 2869
a, b, v = map(int,input().split())
now = 0
answer = 0
while True:
    now += a
    if now >= v:
        print(answer)