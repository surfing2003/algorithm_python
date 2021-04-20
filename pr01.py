# import sys
# input = lambda : sys.stdin.readline().rstrip()

# def hanoi(n, before, after, temp):
#     if n == 1:
#         print(before, after)
#         return
#     hanoi(n-1,before,temp,after)
#     print(before, after)
#     hanoi(n-1,temp,after,before)

# N = int(input())
# print((2**N) -1)
# hanoi(N,1,3,2) 


# import sys
# from collections import Counter
# input = lambda : sys.stdin.readline().rstrip()


# N = int(input())
# num = [int(input()) for _ in range(N)]

# print(round(sum(num)/N))

# print(sorted(num)[N//2])

# temp = Counter(num).most_common()
# temp.sort(key=lambda x: (-x[1],x[0]))
# if len(temp) > 1:
#     if temp[0][1] == temp[1][1]:
#         print(temp[1][0])
#     else:
#         print(temp[0][0])
# else:
#     print(temp[0][0])
# print(max(num) - min(num))

# import sys
# input = lambda: sys.stdin.readline().rstrip()

# N = int(input())
# num = [list(map(int,input().split())) for _ in range(N)]
# num.sort(key = lambda x: (x[0],x[1]))

# for i in num:
#     print(i[0],i[1])

# import sys
# input = lambda: sys.stdin.readline().rstrip()

# N = int(input())
# num = list(map(int,input().split()))
# temp = list(sorted(set(num)))
# d = {temp[i]:i for i in range(len(temp))}
# res = [d[i] for i in num]
# print(*res)


# n = int(input())
# a = [False] * n
# b = [False] * (2*n-1)
# c = [False] * (2*n-1)

# answer = 0
# def queen(i):
#     global answer
#     if i == n:
#         answer += 1
#         return
#     for j in range(n):
#         if not (a[j] or b[i+j] or c[i-j+n-1]):
#             a[j] = b[i+j] = c[i-j+n-1] = True
#             queen(i+1)
#             a[j] = b[i+j] = c[i-j+n-1] = False
# queen(0)
# print(answer)

# sudoku = [list(map(int,input().split())) for _ in range(9)]
# missing = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

# def find_num(i,j):
#     num = [1,2,3,4,5,6,7,8,9]

#     for k in range(9):
#         if sudoku[i][k] in num:
#             num.remove(sudoku[i][k])
#         if sudoku[k][j] in num:
#             num.remove(sudoku[k][j])

#     i //= 3
#     j //= 3

#     for p in range(i*3, (i+1)*3):
#         for q in range(j*3, (j+1)*3):
#             if sudoku[p][q] in num:
#                 num.remove(sudoku[p][q])
#     return num

# chk = False
# def dfs(x):
#     global chk

#     if chk:
#         return
#     if x == len(missing):
#         for row in sudoku:
#             print(*row)
#         chk = True
#         return
    
#     else:
#         (i,j) = missing[x]
#         num = find_num(i,j)

#         for k in num:
#             sudoku[i][j] = k
#             dfs(x+1)
#             sudoku[i][j] = 0
# dfs(0)

# N = int(input())
# array = [list(map(int,input().split())) for _ in range(N)]
# dp = [[0]*(i+1) for i in range(N)]
# dp[0][0] = array[0][0]
# for i in range(1,N):
#     for j in range(i+1):
#         if j == 0:
#             dp[i][j] = array[i][j] + dp[i-1][j]
#         elif j == i:
#             dp[i][j] = array[i][j] + dp[i-1][j-1]
#         else:
#             dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])

# print(max(dp[N-1]))

# num = [i**2 for i in map(int,input().split()) ]
# print(sum(num)%10)

# while True:
#     temp = input()

#     if temp == "0":
#         break

#     if temp == temp[::-1]:
#         print("yes")
#     else:
#         print("no")
# import sys
# input = lambda : sys.stdin.readline().rstrip()
# N, M = map(int,input().split())
# dic_1 ={}
# dic_2 ={}

# for i in range(1,N+1):
#     temp = input()
#     dic_1[temp] = i
#     dic_2[str(i)] = temp

# for _ in range(M):
#     temp = input()
#     try:
#         print(dic_1[temp])
#     except:
#         print(dic_2[temp])

# from math import factorial
# N = int(input())
# a = factorial(N)
# answer = 0
# while a % 10 == 0:
#     answer += 1
#     a //= 10
# print(answer)

# print(N//5 + N//25 + N//125)

# def b(array,target,start,end):
#     if start > end:
#         return False
#     mid = (start+end) // 2
#     if array[mid] == target:
#         return True
#     elif array[mid] < target:
#         return b(array,target,mid+1,end)
#     else:
#         return b(array,target,start,mid-1)
   

# N = int(input())
# num = list(map(int,input().split()))
# num.sort()


# M = int(input())
# test = list(map(int,input().split()))

# for i in test:
#     if b(num,i,0,N-1):
#         print("1")
#     else:
#         print("0")

# n = int(input())
# house = []
# for _ in range(n):
#     house.append(list(map(int,input().split())))

# value = [[0]*3 for _ in range(n)]
# value[0] = house[0]


# for i in range(1,n):
#     value[i][0] = house[i][0] + min(value[i-1][1],value[i-1][2])
#     value[i][1] = house[i][1] + min(value[i-1][0],value[i-1][2])
#     value[i][2] = house[i][2] + min(value[i-1][0],value[i-1][1])
#     print(value)

# print(min(value[n-1][0],value[n-1][1],value[n-1][2]))

## class 만들어서 풀어보기 
# N = int(input())

# tree = {}
# for _ in range(N):
#     k, v1, v2 = input().split()
#     tree[k] = [v1,v2]

# def preorder(k):
#     print(k,end="")
#     if tree[k][0] != ".":
#         preorder(tree[k][0])
#     if tree[k][1] != ".":
#         preorder(tree[k][1])

# def innerorder(k):
#     if tree[k][0] != ".":
#         innerorder(tree[k][0])
#     print(k,end="")
#     if tree[k][1] != ".":
#         innerorder(tree[k][1])

# def postorder(k):
#     if tree[k][0] != ".":
#         postorder(tree[k][0])
#     if tree[k][1] != ".":
#         postorder(tree[k][1])
#     print(k,end="")

# preorder("A")
# print()
# innerorder("A")
# print()
# postorder("A")
# print()

# import math

# n, m = map(int,input().split())
# a = math.factorial(n)
# b = math.factorial(n-m) * math.factorial(m)
# print(a//b)

#LIS
# N = int(input())
# array = list(map(int,input().split()))

# dp = [1]*N

# for i in range(1,N):
#     for j in range(0,i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i],dp[j]+1)
    
# print(max(dp))

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


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    number = list(input())

    length = N // 4
    chk = set()

    for _ in range(length):
        for i in range(4):
            chk.add(''.join(number[(i*length):(i+1)*length]))
        number.append(number.pop(0))
    my_list = []
    for i in chk:
        my_list.append(int(i,16))
    my_list.sort(reverse=True)
    print("#{} {}".format(test_case,my_list[K-1]))