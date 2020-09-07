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
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

