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
    

N = int(input())
arr = list(map(int,input().split()))
temp = []
answer = [-1] * N

for i in range(N):
    while len(temp) != 0 and arr[temp[-1]] < arr[i]:
        answer[temp.pop()] = arr[i]
    temp.append(i)

print(*answer)

