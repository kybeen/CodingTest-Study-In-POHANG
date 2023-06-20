# 11053 - 가장 긴 증가하는 부분수열
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * (N)
for i in range(1, N):
    # 배열의 처음부터 현재 위치까지 수열의 값을 비교했을 때 현재 수보다 작으면 수열이 성립하므로 비교해서 최대값을 갱신해준다.
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))