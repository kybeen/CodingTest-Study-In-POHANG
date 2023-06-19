# 예시5 <병사 배치하기>
import sys

N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    # 현재 위치 병사의 전투력을 앞의 병사들과 비교함
    # 수열이 성립하는 경우마다의 dp값에서 1 더한 값으로 갱신해줌 (가장 큰 경우로 갱신)
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

# max(dp)값은 최대 길이 수열이기 때문에 N에서 max(dp)를 빼준 값이 열외해야 하는 최소 병사 수가 된다.
print(N - max(dp))




# # 예시5 <병사 배치하기>
# import sys

# n = int(sys.stdin.readline())
# array = list(map(int, sys.stdin.readline().split()))
# # 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
# array.reverse()

# # 다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
# dp = [1] * n

# # 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
# for i in range(1, n):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j]+1)

# # 열외해야 하는 병사의 최소 수를 출력
# print(n - max(dp))



