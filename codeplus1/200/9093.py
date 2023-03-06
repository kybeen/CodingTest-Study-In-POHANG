# 9093 - 단어 뒤집기
# 리스트 슬라이싱으로 [::-1] 하면 거꾸로 된 리스트 출력
import sys

T = int(sys.stdin.readline())
for i in range(T):
    sentence = str(sys.stdin.readline())
    sentence = sentence.split() # [ I, am, happy, today ]

    for j in range(len(sentence)): # 4
        word = sentence[j]
        print(word[::-1], end=' ')