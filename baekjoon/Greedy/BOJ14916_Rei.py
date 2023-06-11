# 14916 - 거스름돈

import sys

n = int(sys.stdin.readline())
result = 0

while True:
    if n < 0: # 다 확인해봤지만 거슬러 줄 수 없다면
        break

    if n % 5 == 0:  # 5원으로 거슬러지면
        result += n//5
        n = n % 5
        break
    else:
        # 5로 거슬러질때까지 2원씩 거슬러줌
        n -= 2
        result += 1

# 다 거슬러 줬다면
if n == 0:
    print(result)
else: # 거슬러 줄 수 없다면
    print(-1)