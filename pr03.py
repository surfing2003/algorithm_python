
### 초기풀이
# def change(numbers,length):
#     dic = {
#         "A":10,
#         "B":11, 
#         "C":12,
#         "D":13,
#         "E":14,
#         "F":15
#     }
#     answer = 0

#     for i, v in enumerate(numbers):
#         if v in dic.keys():
#             answer += pow(16,(length-i-1))*dic[v]
#         else:
#             answer += pow(16,(length-i-1))*int(v)
#     return answer
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, K = map(int,input().split())
#     number = list(input())
#     number += number

#     length = N // 4
#     chk = set()

#     for i in range(length):
#         for j in range(0,N,length):
#             chk.add(change(number[(j+i):(j+i+length)],length))
#     print("#"+str(test_case),sorted(list(chk),reverse=True)[K-1])

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    number = list(input())

    length = N // 4
    chk = set()

    for _ in range(length):
        for i in range(4):
            chk.add(''.join(number[(i*length):(i+1)*length]))
        number.append(number.pop(0))
    my_list = []
    for i in chk:
        my_list.append(int(i,16))
    my_list.sort(reverse=True)
    print("#{} {}".format(test_case,my_list[K-1]))