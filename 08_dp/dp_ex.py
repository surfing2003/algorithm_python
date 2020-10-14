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



# bj 1003
n = int(input())
c_0 = [1,0,1]
c_1 = [0,1,1]
def fib(chk):
    if len(c_0) <= chk:
        for i in range(len(c_0),chk+1):
            c_0.append(c_0[i-1] +c_0[i-2])
            c_1.append(c_1[i-1] +c_1[i-2])

    print(c_0[chk],c_1[chk])
            

for _ in range(n):

    chk = int(input())

    fib(chk)

# bj 9461
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


# bj 1463
x = int(input())
d =[0] * 1000001

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)

print(d[x])

# bj 2579
n = int(input())
s = [0] * 301
d = [0] * 301

for i in range(1,n+1):
    s[i] = int(input())

d[1] = s[1]
d[2] = s[1]+s[2] 
d[3] = max(s[2]+s[3],s[1]+s[3])

for i in range(3,n+1):
    d[i] = max(d[i-3]+s[i-1]+s[i], d[i-2]+s[i])

print(d[n])



# bj 14501
# dp인데 뒤에서 부터 해온다는 점이 주요 포인트
N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]

dp = [0] * (N)

for i in range(N-1,-1,-1):
    day = s[i][0]
    pay = s[i][1]

    if day > N - i:
        if i != N-1:
            dp[i] = dp[i+1]
        continue

    if i == N-1:
        dp[i] = pay
    elif i + day == N:  
        dp[i] = max(pay,dp[i+1])
    else:
        dp[i] = max(pay+dp[i+day],dp[i+1])
 
print(dp[0])
