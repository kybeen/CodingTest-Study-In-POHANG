# 1758 - 알바생 강호

import sys

N = int(sys.stdin.readline())
tip_list = [] # 원래 주려던 팁의 리스트
for _ in range(N):
    tip_list.append(int(sys.stdin.readline()))

tip_list.sort(reverse=True) # 내림차순 정렬
result = 0
for i in range(len(tip_list)):
    tip = tip_list[i] - i
    if tip < 0: # 음수일 경우 팁 계산 X
        pass
    else: # 순서에 맞게 차감된 금액을 더해준다.
        result += tip

print(result)