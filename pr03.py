
### 초기풀이
# def change(numbers,length):
#     dic = {
#         "A":10,
#         "B":11, 
#         "C":12,
#         "D":13,
#         "E":14,
#         "F":15
#     }
#     answer = 0

#     for i, v in enumerate(numbers):
#         if v in dic.keys():
#             answer += pow(16,(length-i-1))*dic[v]
#         else:
#             answer += pow(16,(length-i-1))*int(v)
#     return answer
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, K = map(int,input().split())
#     number = list(input())
#     number += number

#     length = N // 4
#     chk = set()

#     for i in range(length):
#         for j in range(0,N,length):
#             chk.add(change(number[(j+i):(j+i+length)],length))
#     print("#"+str(test_case),sorted(list(chk),reverse=True)[K-1])

# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int,input().split())
#     number = list(input())

#     length = N // 4
#     chk = set()

#     for _ in range(length):
#         for i in range(4):
#             chk.add(''.join(number[(i*length):(i+1)*length]))
#         number.append(number.pop(0))
#     my_list = []
#     for i in chk:
#         my_list.append(int(i,16))
#     my_list.sort(reverse=True)
#     print("#{} {}".format(test_case,my_list[K-1]))

# from itertools import product
# from copy import deepcopy

# def WH_check(x,y):
#     return not (x<0 or y<0  or x>H-1 or y>W-1)

# def search(y, blocks):
#     q = []
#     x = 0

#     while WH_check(x,y) and blocks[x][y] == 0:
#         x += 1
    
#     if x == H:
#         return blocks

#     q.append([blocks[x][y],x,y])
#     blocks[x][y] = 0
#     while q:
#         k,x,y = q.pop(0)
#         for i in range(4):
#             for t in range(1,k):
#                 nx = x+(t*dx[i])
#                 ny = y+(t*dy[i])
#                 if WH_check(nx,ny) and blocks[nx][ny] != 0:
#                     q.append([blocks[nx][ny],nx,ny])
#                     blocks[nx][ny] = 0
#     return blocks

# def swap(blocks):
#     before = list(zip(*blocks))
#     after = []
#     for b in before:
#         temp = [i for i in b if i != 0]
#         after.append([0]*(H-len(temp))+temp)
#     return [list(i) for i in zip(*after)]


# T = int(input())
# for test_case in range(1, T + 1):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     N, W, H = map(int,input().split())
#     blocks = [list(map(int,input().rstrip().split())) for _ in range(H)]
#     answer = W*H

#     for case in product(range(W),repeat=N):
#         copy_block = deepcopy(blocks)
#         for c in case:
#             copy_block = search(c,copy_block)
#             copy_block = swap(copy_block)
#         answer = min(answer,(W*H)-sum([i.count(0) for i in copy_block]))
#     print("#{} {}".format(test_case,answer))


