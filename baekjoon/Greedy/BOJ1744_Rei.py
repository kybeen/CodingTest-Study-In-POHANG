# 1744 - 수 묶기

import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

negative = [] # 0이하의 수들
positive = [] # 양수들
result = 0
for a in arr:
    if a <= 0:
        negative.append(a)
    else:
        positive.append(a)

# 0 이하 수들 처리
negative.sort()
i = 0
while i < len(negative):
    if i < len(negative)-1:
        result += negative[i]*negative[i+1] # [음수*음수] or [음수*0] or [0*0] 의 3가지 케이스 : 인접한 2개 수를 곱해준다.
        i += 2
    else: # 마지막 1개가 남는다면 그냥 더해줌
        result += negative[i]
        i += 1

# 양수들 처리
positive.sort(reverse=True)
i = 0
while i < len(positive):
    if i < len(positive)-1:
        if positive[i] > 1 and positive[i+1] > 1:
            result += positive[i]*positive[i+1]
            i += 2
        else:
            result += positive[i]
            i += 1
    else:
        result += positive[i]
        i += 1

print(result)