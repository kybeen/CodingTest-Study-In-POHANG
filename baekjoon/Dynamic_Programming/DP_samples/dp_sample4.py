# 예시4 <금광>
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    gold = [[] for _ in range(m)]
    temp = list(map(int, sys.stdin.readline().split()))
    # 금광 입력을 1줄로 했기 때문에 2차원 배열로 변환해줘야함
    gold[0].append(temp[0])
    for i in range(1, len(temp)):
        gold[i%m].append(temp[i])
    
    dp = [[0]*n for _ in range(m)]
    dp[0] = gold[0] # DP테이블 초기화

    # 다이나믹 프로그래밍 수행
    for i in range(1, m):
        for j in range(n):
            if j == 0: # 시작 부분에 있는 경우
                dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + gold[i][j]
            elif j == n-1: # 끝 부분에 있는 경우
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + gold[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + gold[i][j]
    
    print(max(dp[-1])) # 마지막 줄에서 최대값 출력




# # 예시4 <금광>
# import sys

# # 테스트케이스 입력
# for tc in range(int(sys.stdin.readline())):
#     # 금광 정보 입력
#     n, m = map(int, sys.stdin.readline().split())
#     array = list(map(int, sys.stdin.readline().split()))
#     # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index + m])
#         index += m
#     # 다이나믹 프로그래밍 진행
#     for j in range(1, m):
#         for i in range(n):
#             # 왼쪽 위에서 오는 경우
#             if i == 0: left_up = 0
#             else: left_up = dp[i-1][j-1]
#             # 왼쪽 아래에서 오는 경우
#             if i == n - 1: left_down = 0
#             else: left_down = dp[i+1][j-1]
#             # 왼쪽에서 오는 경우
#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left_up, left_down, left)
#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m-1])
#     print(result)