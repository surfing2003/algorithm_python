# baekjoon 2440 별찍기-3
n = int(input())
for i in range(n):
    print('*'*(n-i))

# baekjoon 1316 그룹단어체커
import sys
input = lambda : sys.stdin.readline().rstrip()

# 내풀이
n = int(ㄴinput())
answer = 0
for _ in range(n):
    word = input()
    word_length = len(word)

    for j in range(word_length):
        if j != word_length-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer += 1 
print(answer)

# 참고풀이
# word를 리스트로 바꾸고 
# word.find 를 키로 정렬한 값과 비교하게되면
# 기존위치는 그대로, 연속되는 것도 그대로, 하지만 건너뛰고 있는 알파벳에 대해서는 정렬순서에 의해 리스트 값이 달라짐.
result = 0
n = int(input())
for i in range(n):
    word = input()
    print(list(word))
    print(sorted(word,key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

# 책예시4_그냥
import sys
input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# moves = list(input().split())
# start_x = 1
# start_y = 1

# for move in moves:
#     if move == 'U' and start_x -1 > 0:
#         start_x -= 1
#     if move == 'D' and start_x +1 <= n:
#         start_x += 1
#     if move == 'L' and start_y -1 > 0:
#         start_y -= 1
#     if move == 'R' and start_y +1 <= n:
#         start_y += 1

# print(start_x,start_y)

x, y =1,1
n = int(input())
moves = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx <1 or ny <1 or nx> n or ny >n:
        continue

    x,y = nx,ny
print(x,y)

# 책예시 5
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

count =0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)

# 책예시 6
import sys
input = lambda : sys.stdin.readline().rstrip()

now = input()

x = int(now[1])
y = ord(now[0]) - 96

dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        answer += 1

print(answer)

# 책예시 7
import sys
input = lambda : sys.stdin.readline().rstrip()

n,m = map(int,input().split())

chk = [[False] * m for _ in range(n)]
# 0:북 1:동 2:남 3:서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

x,y,d = map(int,input().split())

array= []
for _ in range(n):
    array.append(list(map(int,input().split())))

chk[x][y] = True

def turnleft():
    global d
    d -= 1
    if d == -1:
        d = 3
    
count = 1
turn_time = 0

while True:
    turnleft()
    nx = x+dx[d]
    ny = y+dy[d]

    if not chk[nx][ny] and array[nx][ny] == 0:
        chk[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x -dx[d]
        ny = y -dy[d]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time=0
print(count)