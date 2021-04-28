# 4949
# import sys
# input = lambda : sys.stdin.readline().rstrip()


# while True:
#     sentence = input()
    
#     if sentence == '.':
#         break

#     flag = True
#     chk = []
#     for s in sentence:
#         if s == "(" or s == "[":
#             chk.append(s)
#             continue
    
#         elif s == ")":
#             if chk and chk[-1] == "(":
#                 chk.pop()
#                 continue
#             else:
#                 flag = False        
#                 break
#         elif s == "]":
#             if chk and chk[-1] == "[":
#                 chk.pop()
#                 continue
#             else:
#                 flag = False        
#                 break

#     if not chk and flag:
#         print("yes")
#     else:
#         print("no")

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# temp = []
# answer = []
# count = 0
# flag = False
# for now in arr:
#     while count < now:
#         count += 1
#         temp.append(count)
#         answer.append("+")
    
#     if temp[-1] == now:
#         temp.pop()
#         answer.append("-")
#     else:
#         flag = True
#         break

# if flag:
#     print("NO")
# else:
#     print('\n'.join(answer))


# 시간초과
# N = int(input())
# arr = list(map(int,input().split()))
# answer = [-1] * N

# for i in range(N):
#     for j in range(i,N):
#         if arr[i] < arr[j]:
#             answer[i] = arr[j]
#             break
# print(*answer)
    

# N = int(input())
# arr = list(map(int,input().split()))
# temp = []
# answer = [-1] * N

# for i in range(N):
#     while len(temp) != 0 and arr[temp[-1]] < arr[i]:
#         answer[temp.pop()] = arr[i]
#     temp.append(i)

# print(*answer)

# import sys
# from collections import deque

# input = lambda : sys.stdin.readline().rstrip()
# q = deque()
# for _ in range(int(input())):
#     temp = input().split()

#     if temp[0] == "push":
#         q.append(temp[1])
#     elif temp[0] == "pop":
#         if q:
#             print(q.popleft())
#         else:
#             print(-1)
#     elif temp[0] == "front":
#         if q:
#             print(q[0])
#         else:
#             print(-1)

#     elif temp[0] == "back":
#         if q:
#             print(q[-1])
#         else:
#             print(-1)
    
#     elif temp[0] == "size":
#         print(len(q))
    
#     elif temp[0] == "empty":
#         if not q:
#             print(1)
#         else:
#             print(0)

from collections import deque

q = deque(range(1,int(input())+1))

while len(q) != 1:
    print(q)
    q.popleft()
    q.rotate(-1)

print(q[0])