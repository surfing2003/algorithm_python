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
