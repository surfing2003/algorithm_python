import sys
input = lambda : sys.stdin.readline().rstrip()

# # 큐
# queue = deque()
# queue.append(5)
# queue.popleft()

# # 스택
# stack = []
# stack.append(5)
# stack.pop()


# n = list(map(int,input()))
# a = [0]*9

# for i in n:
#     if i != 6 and i!=9:
#         a[i] += 1
#     else: 
#         a[6] += 1

# a[6] = -((-a[6]) // 2)

# print(max(a))

# n = list(map(int,input()))
# a = [0]*9

# for i in n:
#     if i != 6 and i!=9:
#         a[i] += 1
#     else: 
#         a[6] += 1

# a[6] = -((-a[6]) // 2)

# print(max(a))
# import sys
# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# answer =[]
# for _ in range(n):
#     answer.append(input())

# answer.sort(key=lambda x: (len(x),x))
# temp = ''
# for i in answer:
#     if temp == i:
#         continue
#     temp = i
#     print(i)

# import sys
# import queue
# input = lambda : sys.stdin.readline().rstrip()

# def bfs(start):
#     q = queue.Queue()
#     q.put(start)
#     chk[start] = True
    
#     while not q.empty():
#         now = q.get()
#         for next in array_graph[now]:
#             if not chk[next]:
#                 chk[next] = True
#                 q.put(next)

# count = 0
# n, m = map(int,input().split())

# array_graph = [list() for _ in range(n+1)]
# chk = [False] * (n+1)

# for _ in range(m):
#     x,y = map(int,input().split())
#     array_graph[x].append(y)
#     array_graph[y].append(x)

# for i in array_graph:
#     i.sort()


# for i in range(1,n+1):
#     if not chk[i]:
#         count += 1
#         bfs(i)

# print(count)


# a = []
# for _ in range(9):
#     a.append(int(input()))

# a.sort()
# sum_a = sum(a)


# for i in range(9):
#     for j in range(i+1,9):
#         if sum_a -a[i] -a[j] == 100:
#             for k in range(9):
#                 if k == i or k == j:
#                     continue
#                 else:
#                     print(a[k])
#             exit()


##### 백준 7662 이중우선순위 : 다시풀어야함

import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    max_heap, min_heap = [], []
    del_max_heap, del_min_heap = [], []

    for _ in range(int(input())):
        c, n = input().split()
        n = int(n)

        if c == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

        else:
            if n == 1:
                if max_heap:
                    heapq.heappush(del_max_heap, -heapq.heappop(max_heap))
            else:
                if min_heap:
                    heapq.heappush(del_min_heap, -heapq.heappop(min_heap))

        while max_heap and del_min_heap and max_heap[0] == del_min_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappop(del_min_heap)

        while min_heap and del_max_heap and min_heap[0] == del_max_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappop(del_max_heap)

    if not max_heap:
        print("EMPTY")

    else:
        print(-max_heap[0], min_heap[0])