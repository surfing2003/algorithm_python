# baekjoon 9012 괄호

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

# for _ in range(n):
#     chk = input()
#     stack = []
#     for i in chk:
#         if i == "(":
#             stack.append(i)
        
#         if i == ")":
#             if not stack:
#                 stack.append(i)
#             elif stack[-1] == "(":
#                 stack.pop()
#             else:
#                 stack.append(i) 

#     if not stack:
#         print("YES")
#     else:
#         print("NO")   

# 실제 스택이아니라 그냥 숫자로 느낌만 가져도 충분하다 
for _ in range(n):
    chk = input()
    stack = 0
    for i in chk:
        if i == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break

    if stack == 0:
        print("YES")
    else:
        print("NO")   
    