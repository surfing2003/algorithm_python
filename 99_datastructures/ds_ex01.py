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
    Q=[]
    for p, s in zip(progresses, speeds):
        # Q가 비어있거나 Q[-1]> Q의 마지막 이 작으면 append 크면 출력에 +1
        if not Q or Q[-1][0]< -((p-100)//s):
            # 음수의 값은 남는경우까지 계산되어 나머지를 확인하고 숫자를 늘려줄 필요가 없다.
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]