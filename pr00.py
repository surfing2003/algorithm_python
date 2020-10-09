import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
d =  [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# d.extend([0]*90) 이것보다는

for i in range(11,101):
    d.append(d[i-2]+d[i-3]) 
for _ in range(t):
    n = int(input())
    # if n > 10:
    #     for i in range(11,n+1):
    #         d[i] = d[i-2] + d[i-3]    # extend 안하는 방식의 경우는 필요없는 부분
    print(d[n])

