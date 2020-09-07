# 프로그래머스 기능개발
def solution(progresses, speeds):
    chk = [] 
    for p,s in zip(progresses,speeds):
        temp = (100-p)//s
        if (100-p)%s != 0:
            temp += 1
        
        if not chk:
            chk.append([temp,1])
        else:
            day, cnt = chk.pop()
            if day >= temp:
                chk.append([day,cnt+1])
            else:
                chk.append([day,cnt])
                chk.append([temp,1])
                
    return [c[1] for c in chk]

# 다른 코드
def solution(progresses, speeds):
    answer=[]
    for progress, speed in zip(progresses, speeds):
        # Q가 비어있거나 Q[-1]> Q의 마지막 이 작으면 append 크면 출력에 +1
        if not answer or answer[-1][0]< -((progress-100)//speed):
            # 음수의 값은 남는경우까지 계산되어 나머지를 확인하고 숫자를 늘려줄 필요가 없다.
            answer.append([-((progress-100)//speed),1])
        else:
            answer[-1][1]+=1
    return [q[1] for q in answer]

print(solution([93, 30, 55],[1, 30, 5]))