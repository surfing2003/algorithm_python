
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


# 벨만포드 알고리즘 
# 음수 간선이 포함된 상황에서의 최단거리 문제, 음수간선의 순환을 감지할 수 있음
# 시간 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느립니다.
# 다른 상황은 다익스트라를 활용하여 구하는 것이 가능하지만
# 음수간선의 순환에서 순환의 결과가 마이너스가 되는 경우 순환을 반복하여
# 마이너스 무한대로 가게 되는 문제가 발생함

# 아래의 유형을 모두 커버가 가능
# 1 모든 간선이 양수인 경우
# 2 음수 간선이 있는경우
# 2 - 1 음수 간선 순환은 없는 경우
# 2 - 1 음수 간선 순환이 있는 경우

# 1. 출발 노드를 설정합니다.
# 2. 최단거리 테이블을 초기화 합니다.
# 3. 다음과정을 N-1번 반복합니다. 
#  1. 전체 간선 E개를 하나씩 확인합니다.
#  2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단거리테이블을 갱신합니다.
# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번과정을 한번더 수행
# 이때 최단거리 테이블이 갱신된다면 음수간선 순환이 존재하는 것 입니다.

# 다익스트라 - 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
#         - 음수 간선이 없다면 최적의 해를 찾을 수 있습니다.

# 벨만포드  - 매번 모든 간선을 전부 확인
#         - 따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함
#         - 다익스트라에 비해 시간은 오래걸리지만, 음수간선 순환을 탐지할 수 있음
# pypy3 제출
INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur]+cost:
                dist[next_node] = dist[cur] + cost
                if i == n-1:
                    return True
    return False


n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])