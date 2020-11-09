
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


# 정렬
# 선택정렬
# 기준을 한칸씩 뒤로 옮기며 최소값을 가져오는 방식
n = 10
data = [1,8,6,4,2,10,7,5,9,3]
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if data[min_index] > data[j]:
            min_index = j
    data[i],data[min_index] = data[min_index],data[i]

# 삽입정렬
# 앞에서부터 한칸씩 기준을 뒤로 미루며, 정렬상태를 유지하는 방식
# 정렬된 배열에 다음 숫자를 끼워넣는 느낌
for i in range(1,n):
    for j in range(i,0,-1):
        if data[j-1] > data[j]:
            data[j-1], data[j] = data[j],data[j-1]
        else:
            break

# 퀵정렬
# 분할 정복 방법 
# 피벗을 고르고, 피벗기준으로 작은요소는 왼쪽, 큰요소는 오른쪽으로 이동
# 피벗을 제외한 양쪽을 다시 정렬
# 더이상 분할이 불가능할때까지 분할
def quick(start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
        
    quick(start,right-1)
    quick(right+1,end)
    
quick(0,n-1)

# 계수정렬
# 해당 숫자의 인덱스에 갯수를 저장하고 이를 출력하는 방식으로 정렬
count = [0] * (max(data)+1)
for i in data:
    count[i] += 1

print("정렬후")
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = " ")


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

# 선형시간에 해결이 되는 것
# 투포인터 : 리스트에 순차적으로 접근해야 할 때, 
# 두 개의 점을 이용해 위치를 기록하면서 계산하는 기법?

# N개의 자연수로 구성된 수열이 있습니다. 
# 합이 M인 부분 연속 수열의 개수를 구해보세요.

n, m = 5, 5
data = [1,2,3,2,5]

result = 0
summary = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while summary < m and end < n:
        summary += data[end]
        end += 1
    
    if summary == m:
        result += 1
    summary -= data[start]

print(result) 

# 접두사합 
# M개의 쿼리 정보를 통해 구간에 해당하는 데이터의 합을 구하는 문제 
n = 5
data = [10, 20, 30, 40, 50]

summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])

# 백트래킹
# 현재상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘
# bj 15649 N과 M(1)
N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(N):  # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면
            visited[i] = True  # 탐사 시작(중복 제거)
            out.append(i+1)  # 탐사 내용
            solve(depth+1, N, M)  # 깊이 우선 탐색
            visited[i] = False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거

solve(0, N, M)

