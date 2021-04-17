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

print(''.join(sorted(input())[::-1]))
