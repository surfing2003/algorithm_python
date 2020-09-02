# baekjoon 2440 별찍기-3

# n = int(input())
# for i in range(n):
#     print('*'*(n-i))


# baekjoon 1316 그룹단어체커

import sys
input = lambda : sys.stdin.readline().rstrip()

# n = int(input())
# answer = 0
# for _ in range(n):
#     word = input()
#     word_length = len(word)

#     for j in range(word_length):
#         if j != word_length-1:
#             if word[j] == word[j+1]:
#                 pass
#             elif word[j] in word[j+1:]:
#                 break
#         else:
#             answer += 1 
# print(answer)

result = 0
n = int(input())

for i in range(n):
    word = input()
    print(list(word))
    print(sorted(word,key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)