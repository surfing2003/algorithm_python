# 프로그래머스 크레인인형뽑기게임
def solution(board, moves):
    answer = 0
    fin = []
    for move in moves:
        temp = 0
        for i in range(len(board)):
            if board[i][move-1] != 0:
                temp = board[i][move-1]
                board[i][move-1] = 0
                if len(fin)==0:
                    fin.append(temp)
                elif len(fin) > 0 and fin[-1] != temp:
                    fin.append(temp)
                else :
                    fin.pop()
                    answer += 2
                break
    return answer

# 프로그래머스 위장
def solution(clothes):
    answer = 0
    temp = []
    for c in clothes:
        temp.append(c[1])

    return eval('*'.join(map(str,[temp.count(x)+1 for x in set(temp)]))) -1

# 다른코드
from collections import Counter
from functools import reduce
def solution(clothes):
    return reduce(lambda x, y: x*y,[x+1 for x in Counter([c[1] for c in clothes]).values()])-1
    # Counter는 몇번나오는지 체크하는 빈도표 함수? 딕셔너리로 return 되어서 여기는 values를 이용해서 카운트된 숫자만 활용
    # reduce 들어오는 순서대로 정해진 함수계산 여기에서는 ((x*y) * y) 이런식

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


