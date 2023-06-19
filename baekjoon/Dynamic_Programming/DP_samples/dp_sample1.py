# 예시1 <개미 전사>
import sys

N = int(sys.stdin.readline())
stores = list(map(int, sys.stdin.readline().split())) # 모든 식량 정보 입력

dp = [0]*N # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 (0으로)
dp[0] = stores[0]
dp[1] = max(stores[0], stores[1])

# 다이나믹 프로그래밍 진행 (바텀업 방식)
for i in range(2, N):
    a = dp[i-1] # 바로 뒤의 최대값 (현재 창고는 털지 않는 경우)
    b = dp[i-2] + stores[i] # 2칸 뒤의 최대값 (현재 창고도 터는 경우)
    dp[i] = max(a, b) # 위의 2가지 경우 중 더 큰 경우로 dp테이블에 넣어준다.

print(dp[N-1])