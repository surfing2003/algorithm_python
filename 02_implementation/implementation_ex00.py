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