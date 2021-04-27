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

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [int(input()) for _ in range(N)]
temp = []
answer = []
count = 0
flag = False
for now in arr:
    while count < now:
        count += 1
        temp.append(count)
        answer.append("+")
    
    if temp[-1] == now:
        temp.pop()
        answer.append("-")
    else:
        flag = True
        break

if flag:
    print("NO")
else:
    print('\n'.join(answer))