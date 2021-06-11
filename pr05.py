# N = int(input())

# for i in range(N):
#     print(' '*(i)+'*'*(N-i))

# N = int(input())

# for i in range(N):
#     print(' '*(N-i-1)+'*'*((2*i)+1))


# N = int(input())

# for i in range(N,0,-1):
#     print(' '*(N-i)+'*'*((2*i)-1))

# N = int(input())

# for i in range(N):
#     print(' '*i+'*'*((2*(N-i))-1))

# N = int(input())

# for i in range(N):
#     print(' '*(N-i-1)+'*'*((2*i)+1))

# for i in range(1,N):
#     print(' '*i+'*'*((2*(N-i))-1))

# N = int(input())

# for i in range(1,N):
#     temp = '*'*i + ' '*(N-i)
#     print(temp+temp[::-1])
# for i in range(N,0,-1):
#     temp = '*'*i + ' '*(N-i)
#     print(temp+temp[::-1])

# N = int(input())

# for i in range(1,N):
#     print('*'*i+' '*(2*N-i*2)+'*'*i)
# for i in range(N,0,-1):
#     print('*'*i+' '*(2*N-i*2)+'*'*i)

# N = int(input())

# for i in range(N):
#     print(' '*i+'*'*(2*(N-i)-1))
# for i in range(N-2,-1,-1):
#     print(' '*i+'*'*(2*(N-i)-1))

# N = int(input())
# for i in range(-N+1,N):
#     print(i)
#     print(' '*(N-abs(i)-1) + '*'*(2*abs(i)+1))

# 752ms
# N, M = map(int,input().split())
# num = 1
# for _ in range(N):
#     for _ in range(M):
#         if num % M == 0:
#             print(num,end = '')
#         else:
#             print(num,end = ' ')
#         num += 1
#     print()

# 556ms
# N,M = map(int,input().split())

# for i in range(N):
#     print(*[ M*i+j+1 for j in range(M)])

# 308ms
# n, m = map(int, input().split())
# for i in range(1, 1 + n*m, m):
#     print(' '.join(map(str, range(i, i+m))))