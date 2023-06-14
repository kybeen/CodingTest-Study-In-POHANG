# 21313 - 문어

import sys

N = int(sys.stdin.readline())

result = [1]
for i in range(1, N):
    if i == N-1:
        if result[i-1] == 2:
            result.append(3)
        else:
            result.append(2)
    else:
        if result[i-1] == 1:
            result.append(2)
        else:
            result.append(1)

for r in result:
    print(r, end=' ')