import sys
input = lambda : sys.stdin.readline().rstrip()

# 개미전사
n = int(input())
stores = list(map(int, input().split()))

chk = [0] * n
chk[0] = stores[0]
chk[1] = max(stores[1],stores[0]) # 항상 1이 되는게 아니라 선택한 부분중 최대가 되는 것을 선택해야함. 
for i in range(2,n):
    chk[i] = max(chk[i-2]+stores[i], chk[i-1])    
print(chk[n-1])


# 1로만들기
n = int(input())

now = 1
array = [0] * (30001)

for i in range(2,n+1):
    array[i] = array[i-1] + 1
    
    if i % 2 == 0:
        array[i] = min(array[i], array[i//2]+1)

    if i % 3 == 0:
        array[i] = min(array[i], array[i//3]+1)

    if i % 5 == 0:
        array[i] = min(array[i], array[i//5]+1)

print(array[n])

# 효율적인 화폐구성
n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in coins:
    for j in range(i, m+1):
        if d[j-i] != 10001:
            d[j] = min(d[j],d[j-i]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# 금광문제
n, m = map(int, input().split())
array = list(map(int,input().split()))

dp = []
index = 0   
for i in range(n):
    dp.append(array[index:index+m])
    index += m

for j in range(1,m):
    if i in range(n):
        if i == 0 : 
            left_up = 0 
        else :
            left_up = dp[i-1][j-1]
        
        if i == n-1:
            left_down = 0
        else:
            left_down = dp[i+1][j-1]

        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up,left,left_down)
result = 0
for i in range(n):
    result = max(result, dp[i][m-1])
print(result)

# LIS 
n = int(input())
array = list(map(int,input().split()))
array.reverse()
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))