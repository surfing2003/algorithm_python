# 큰 수의 법칙

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int,input().split())

numbers = list(map(int,input().split()))
numbers.sort(reverse=True)

# 단순 반복 풀이
temp = 0
answer = 0
for _ in range(m):
    if temp != k:
        answer += numbers[0]
        temp += 1
    else:
        answer += numbers[1]
        temp = 0
print(answer)

# 수학적 접근?
max_0 = numbers[0]
max_1 = numbers[1]

cnt = (m//(k+1)) * k # 전체 횟수에서 (반복횟수+1) 것이 몇번 반복되는지 확인하고 반복횟수를 곱해주면 가장큰수가 몇번반복되는지
cnt += m%(k+1) # 추가로 (반복횟수+1) 의 나머지도 추가로 가장큰수 횟수에 추가

print(cnt) # 가장큰수가 들어가야하는 횟수
print(m-cnt) # 두번째로 큰수가 들어가야하는 횟수

answer = (cnt * max_0) + ((m-cnt)*max_1)
print(answer)