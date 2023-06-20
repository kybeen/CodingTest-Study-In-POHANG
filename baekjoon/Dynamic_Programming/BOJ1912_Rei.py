# 1912 - 연속합
import sys

n = int(sys.stdin.readline())
# dp[i] : i번째까지만 봤을 때 i번째 수가 사용될 가장 때 큰 연속합
dp = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1]+dp[i])

print(max(dp))