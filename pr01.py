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

from math import factorial
N = int(input())
a = factorial(N)
answer = 0
while a % 10 == 0:
    answer += 1
    a //= 10
print(answer)

print(N//5 + N//25 + N//125)

