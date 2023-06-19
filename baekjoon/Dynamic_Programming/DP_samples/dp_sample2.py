# 예시2 <1로 만들기>
import sys

X = int(sys.stdin.readline())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# dp[i] : i를 1로 만들기 위한 최소 연산 횟수
dp = [0]*30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (바텀업)
for i in range(2, X+1): # 1일 때는 계산이 필요 없기 때문에 2부터 시작
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[X])