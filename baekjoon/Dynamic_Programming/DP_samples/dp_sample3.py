# 예시3 <효율적인 화폐 구성>
import sys

N, M = map(int, sys.stdin.readline().split())
money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

big_value = M+100
# dp[i] : i원을 만들기 위해 필요한 최소 화폐 개수
# 초기값은 만들 수 없는 큰 값으로 설정해준다. (화폐의 단위 중 가장 작은 경우는 1이기 때문에 M보다 큰 수면 됨)
dp = [big_value] * (M+1)

# 각 화폐 단위만큼의 가격의 경우 dp테이블을 먼저 초기화해줌
for m in money:
    try:
        dp[m] = 1
    except:
        pass

# 다이나믹 프로그래밍 (바텀업)
for i in range(money[0], M+1):
    for j in range(0, N):
        # 현재 가격에서 가능한 화폐 단위만큼 뺐을 때의 가격이 현재 화폐 단위들로 구성 가능하다면 그 dp테이블의 값에서 1을 더한 값을 비교해서 넣어줌
        if dp[i - money[j]] != big_value:
            dp[i] = min(dp[i], dp[i - money[j]] + 1)

if dp[M] == big_value:
    print(-1)
else:
    print(dp[M])






# # 예시3 <효율적인 화폐 구성>
# import sys

# # 정수 N, M을 입력 받기
# n, m = map(int, sys.stdin.readline().split())
# # N개의 화폐 단위 정보를 입력받기
# array = []
# for i in range(n):
#     array.append(sys.stdin.readline())

# # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [10001] * (m+1)

# # 다이나믹 프로그래밍(Dynamic Programming) 진행(바텀엄)
# d[0] = 0
# for i in range(n):
#     for j in range(array[i], m+1):
#         if d[j - array[j]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j], d[j - array[i]] + 1)

# # 계산된 결과 출력
# if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
#     print(-1)
# else:
#     print(d[m])




