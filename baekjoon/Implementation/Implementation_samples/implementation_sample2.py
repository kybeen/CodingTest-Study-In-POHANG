# 예시2 <시각>
import sys

N = int(sys.stdin.readline())
hour, minute, second = 0, 0, 0
result = 0
while True:
    second += 1
    if second == 60: # 60초 됐을 때
        minute += 1
        second = 0
    if minute == 60: # 60분 됐을 때
        hour += 1
        minute = 0
    if ('3' in str(hour)) or ('3' in str(minute)) or ('3' in str(second)):
        result += 1
    
    if hour == N: # 종료 조건
        if minute == 59 and second == 59:
            break

print(result)




# import sys

# # H 입력 받기
# h = int(input())

# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(l):
#                 count += 1

# print(count)