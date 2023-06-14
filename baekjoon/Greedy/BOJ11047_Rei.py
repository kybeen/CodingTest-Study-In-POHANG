# 11047 - 동전 0
# 모든 화폐 단위가 배수관계이기 때문에 일반적인 거스름돈 문제처럼 풀면 됨 (가능한 가장 큰 화폐단위부터 거슬러주기)

import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

enable_coins = []
# 사용 가능한 동전만 추리기 (K원보다 작은 금액의 동전만 사용 가능)
for c in coins:
    enable_coins.append(c)
    if c > K:
        break

result = 0
enable_coins.sort(reverse=True) # 내림차순으로 정렬 (큰 금액부터)
# 큰 금액부터 거슬러주기
for coin in enable_coins:
    if K == 0:
        break
    result += K // coin
    K = K % coin

print(result)