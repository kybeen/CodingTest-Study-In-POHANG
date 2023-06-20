# 17626 - Four Squares
import sys

n = int(sys.stdin.readline())
# dp[i] : i가 되기 위해 필요한 최소 개수 제곱수
dp = [50001] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    j = 1
    while j**2 <= i:
        dp[i] = min(dp[i], dp[i - (j**2)] + 1)
        j += 1

# print(dp)
print(dp[-1])