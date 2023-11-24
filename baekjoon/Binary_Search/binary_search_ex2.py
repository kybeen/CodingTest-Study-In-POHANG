# 예시2 <정렬된 배열에서 특정 수의 개수 구하기>
import sys
from bisect import bisect_left, bisect_right

N, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)
cnt = right - left
if cnt == 0:
    print(-1)
else:
    print(cnt)