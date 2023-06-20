# 10844 - 쉬운 계단 수
import sys

N = int(sys.stdin.readline())
number = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(N)]
dp = [[0 for _ in range(10)] for _ in range(N)]

# 첫번째 자리 수에서 0은 제외해야 하기 때문에 카운트하지 X
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1])%1000000000)