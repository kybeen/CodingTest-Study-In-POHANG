# 11725 - 트리의 부모 찾기
# 최대 재귀 깊이 참고 (https://help.acmicpc.net/judge/rte/RecursionError)

import sys
sys.setrecursionlimit(10**6) # 최대 재귀 깊이 늘려주기 (안해주면 런타임 에러)

def tree(n):
    for i in range(len(nodes[n])):
        leafIdx = nodes[n][i]
        if result[leafIdx] == 0:
            result[leafIdx] = n
            tree(leafIdx)

N = int(sys.stdin.readline())
nodes = [[] for i in range(N+1)]
# 노드 연결관계 리스트 생성
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)
# 정답 리스트 생성
result = [0 for i in range(N+1)]

tree(1)
for i in range(2,N+1):
    print(result[i])