# 1141 - 접두사
# 길이가 짧은 순서대로 정렬한 뒤 순회하며 접두어가 되는지 확인 후, 접두어가 되는 단어라면 제외

import sys

N = int(sys.stdin.readline())
words = []

# 단어 입력
for i in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(word)

words.sort(key=len) # 문자열 길이대로 정렬

result = N
for i in range(N):
    flag = False # 현재 단어가 접두어가 되는지 표시하기 위한 변수
    prefixLen = len(words[i]) # 현재 단어의 길이
    for j in range(i+1, N): # 현재 단어보다 긴 단어들을 확인
        if words[j][:prefixLen] == words[i]: # 현재 단어가 접두어가 되는 단어가 존재한다면
            flag = True
            break
    if flag == True:
        result -= 1
print(result)