# baekjoon_1946 신입사원
# 서류로 정렬 후 면접등수를 비교하면서 작은 경우를 찾아가는 방식

import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    chk = [list(map(int,input().split())) for _ in range(n)]
    chk.sort(key=lambda x: x[0])

    cnt = 1
    min_chk = chk[0]

    for i in range(1,n):
        if min_chk[1] > chk[i][1]:
            min_chk = chk[i]
            cnt += 1

    print(cnt)

# sort 대신 서류등수를 index로 가지는 리스트에 면접등수를 넣어서 풀이하면 정렬 시간 단축
t = int(input())
for _ in range(t):
    n = int(input())
    rank_list = [0] * (n+1)

    for _ in range(n):
        a,b = map(int,input().split())
        rank_list[a] = b

    cnt = 1
    min_rank = rank_list[1]

    for i in range(2,n+1):
        if rank_list[i] < min_rank:
            cnt += 1
            min_rank = rank_list[i]

    print(cnt)

# baekjoon_10162 전자레인지
# 거스름돈 문제와 비슷한 유형 큰 경우부터 정리해나가는 방식
import sys
input = lambda: sys.stdin.readline().rstrip()

buttons = [300,60,10]
t = int(input())
cnt = []
for button in buttons:
    cnt.append(t // button)
    t %= button

if t != 0:
    print(-1)
else:
    print("%d %d %d"%(cnt[0],cnt[1],cnt[2]))

# 리스트가 아니라 바로 값으로 입력 받아서 해결하는게 더 빠르다. 3개로 버튼이 정해져 있으니까
t = int(input())

if (t % 10) != 0:
    print(-1)
else :
    a = t // 300
    b = (t%300) // 60 
    c = ((t%300)%60) // 10
    print(a,b,c)

# baekjoon 1339 단어수학
# 단어별 위치를 10진수로 표현하고 가장 큰 수부터 9 8 7 ... 곱하는 방식으로 진행

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
alpha = [0] * 26

for _ in range(n):
    word = input()
    i = 0
    for w in word[::-1]:
        alpha[ord(w)-65] += (10 ** i)
        i += 1

alpha.sort(reverse=True)
answer = 0
num = 9
for i in range(26):
    if alpha[i] == 0:
        break
    answer += (num * alpha[i])
    num -= 1

print(answer)
