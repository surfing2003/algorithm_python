# baekjoon 1002 터렛 
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = (((x1-x2)**2) + ((y1-y2)**2))**0.5
    rs = r1 + r2
    rm = abs(r1 - r2)
    
    if d == 0 :
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rs or d == rm:
            print(1)
        elif d < rs and d > rm:
            print(2)
        else:
            print(0)

# bj 13458 시험감독

n = int(input())
a = list(map(int,input().split()))
b, c = map(int, input().split())

total = 0
for i in a:

    total += 1
    if i < b:
        continue
    i -= b
    total += -(-i //c)

print(total)


# bj 14888 연산자 끼워넣기
# 시간초과.
# >> permutation 중복을 제거하면 해결된다.?
from itertools import permutations
n = int(input())
numbers = list(map(int, input().split()))
op = ["+","-","*","/"]
op_c = list(map(int,input().split()))

opers = []
for i in op_c:
    t = op.pop(0)
    opers.extend([t]*i)

permus = list(set(permutations(opers,len(opers))))

max_a = -1000000001
min_a = 1000000001
for i in permus:
    temp = numbers[0]
    for j in range(1,n):
        if i[j-1] == "+":
            temp += numbers[j]
        elif i[j-1] == "-":
            temp -= numbers[j]
        elif i[j-1] == "*":
            temp *= numbers[j]
        else:
            if temp < 0:
               temp = -((-temp)//numbers[j])
            else:
                temp //= numbers[j]
    
    max_a = max(temp,max_a)
    min_a = min(temp,min_a)
print(max_a)
print(min_a)

# 백트래킹?
n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int,input().split()))
max_a = -1000000001
min_a = 1000000001

def cal(i, result, plus, sub, mul, div):
    global max_a
    global min_a
    if i == n:
        max_a = max(max_a,result)
        min_a = min(min_a,result)
        return
    if plus:
        cal(i+1,result + numbers[i],plus-1,sub,mul,div)
    if sub:
        cal(i+1,result - numbers[i],plus,sub-1,mul,div)
    if mul:
        cal(i+1,result * numbers[i],plus,sub,mul-1,div)
    if div:
        cal(i+1,-(-result//numbers[i]) if result < 0 else result//numbers[i] ,plus,sub,mul,div-1)
    

cal(1,numbers[0],opers[0],opers[1],opers[2],opers[3])
print(max_a)
print(min_a)