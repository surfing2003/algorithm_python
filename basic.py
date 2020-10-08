
# 1 5
# 12345

# n, m = map(int, input().split())
# a = [list(map(int, input())) for _ in range(n)]

# 1 5
# 1 2 3 4 5
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]


# import sys
# input = lambda: sys.stdin.readline().rstrip()


# def chk(string):
#     return sum([int(i) for i in string if i.isdigit()])


# n = int(input())
# l = []
# for _ in range(n):
#     l.append(input())
s
# l.sort(key = lambda x : (len(x),chk(x),x))


# for i in l:
#     print(i)

#####bfs
import queue
n, m, v = map(int, input().split())    # 정점의 개수, 간선의 개수, 시작 번호

a = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()

chk = [False]*(n+1)

# BFS 함수 구현 
def bfs(start):
    q = queue.Queue()
    q.put(start)
    chk[start] = True

    while not q.empty():               
        now = q.get()                 # 큐에서 가장 앞으 노드를 꺼내온다.
        print(now, end=" ")           # 해당 노드를 방문한다는 의미로 출력한다.
        for next in a[now]:           # 방문한 노드의 인접 노드들을 for문을 통해 next에 저장한다.
            if not chk[next]:         # 인접 노드가 체크가 되어있지 않다면
                chk[next] = True      # 체크를 해주고,
                q.put(next)           # 인접 노드를 큐에 넣어준다. 
    print()

bfs(v) # bfs 함수 실행 

import queue

# 입력
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
chk = [[0]* m for _ in range(n)]

q = queue.Queue()
q.put([0,0])
chk[0][0] = 1
while not q.empty():
    x, y = q.get()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n: continue  # 1. nx가 배열의 범위를 넘었는지
        if ny < 0 or ny >= m: continue  # 1. ny가 배열의 범위를 넘었는지
        if a[nx][ny] == 0: continue     # 2. 벽이 있는지
        if chk[nx][ny] != 0: continue   # 3. 이미 방문 한 곳인지

        chk[nx][ny] = chk[x][y] + 1
        q.put([nx, ny])

print(chk[n-1][m-1])



######dfs 
n, m, v = map(int, input().split()) #정점의 개수, 간선의 개수, 시작 번호

a = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()

chk = [False]*(n+1)

def dfs(node):
    chk[node] = True
    print(node, end=" ")

    for next in a[node]:
        if not chk[next]:
            dfs(next)

dfs(v)
print()


#########heap
# 모듈임포트
import heapq
# 힙 생성
heap = []
# 원소 추가
heapq.heappush(heap,1)
heapq.heappush(heap,4)
# 원소 제거
heapq.heappop(heap)
# 원소 제거 안하고 최소값 얻기
heap[0]
# 기존 리스트 힙으로
heap = [1,4,3,2,6,2,1]
heapq.heapify(heap)
print(heap)

# 최대 힙
nums = [4, 1, 7, 3, 8, 5]
heap = []
for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
# while heap:
#   print(heapq.heappop(heap)[1])  # index 1

# k번째 최소 값
import heapq
def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

# print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))
print(heap_sort([1,4,3,2,6,2,1]))


#########이진탐색
def b_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return b_search(array,target,start,mid-1)
    else:
        return b_search(array,target,mid+1,end)

def b_search_for(array, target, start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


temp = [1,3,5,7,9,11,13,15,17,19]
result = b_search(temp,7,0,len(temp)-1)
result = b_search(temp,2,0,len(temp)-1)


#  정렬되었는지 확인하는 방법
import sys
input = lambda: sys.stdin.readline().rstrip()

a = list(map(int,input().split()))

if all(x<y for x,y in zip(a[:-1],a[1:])):
    print("ascending")
elif all(x>y for x,y in zip(a[:-1],a[1:])):
    print("descending")
else:
    print("mixed")

## LIS 
n = int(input())
array = list(map(int,input().split()))
array.reverse()
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))