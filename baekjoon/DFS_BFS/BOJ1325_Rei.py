# 1325 - 효율적인 해킹
# #### 2차 풀이 BFS -> 시간초과
# import sys
# from collections import deque

# N, M = map(int, sys.stdin.readline().split())
# trust = [[] for _ in range(N+1)] # 신뢰관계 배열 ex) trust[1] : 1번 컴퓨터를 신뢰하는 컴퓨터들
# hacking = [0] * (N+1) # 해당 컴퓨터를 해킹했을 때 해킹할 수 있는 컴퓨터의 수
# # 신뢰관계 입력
# for _ in range(M):
#     a, b  = map(int, sys.stdin.readline().split())
#     trust[b].append(a)

# for i in range(N+1):
#     visited = [0] * (N+1)
#     queue = deque([i])
#     hacking[i] += 1
#     while queue:
#         now = queue.popleft()
#         for t in trust[now]:
#             if visited[t] == 0:
#                 queue.append(t)
#                 visited[t] = 1
#                 hacking[i] += 1

# maximum = max(hacking)
# for i in range(N+1):
#     if hacking[i] == maximum:
#         print(i, end=' ')


# ### 1차 풀이 DFS -> 시간초과
# import sys

# def dfs(graph, now, visited):
#     for t in graph[now]:
#         if visited[t] == 0:
#             visited[t] = 1
#             dfs(graph, t, visited)

# N, M = map(int, sys.stdin.readline().split())
# trust = [[] for _ in range(N+1)] # 신뢰관계 배열 ex) trust[1] : 1번 컴퓨터를 신뢰하는 컴퓨터들
# hacking = [0 for _ in range(N+1)] # 해당 컴퓨터를 해킹했을 때 해킹할 수 있는 컴퓨터의 수
# # 신뢰관계 입력
# for _ in range(M):
#     a, b  = map(int, sys.stdin.readline().split())
#     trust[b].append(a)

# # 컴퓨터 한개씩 DFS 수행
# for i in range(1, N+1):
#     visited = [0 for _ in range(N+1)]
#     dfs(trust, i, visited)
#     hacking[i] = sum(visited)

# # 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 인덱스 출력
# result = []
# maximum = max(hacking)
# for i in range(N+1):
#     if hacking[i] == maximum:
#         result.append(i)
# for r in result:
#     print(r, end=' ')





# ##### 3차 풀이
#### BFS에서 자잘하게 수정함
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
trust = [[] for _ in range(N+1)] # 신뢰관계 배열 ex) trust[1] : 1번 컴퓨터를 신뢰하는 컴퓨터들
hacking = [0] * (N+1) # 해당 컴퓨터를 해킹했을 때 해킹할 수 있는 컴퓨터의 수
# 신뢰관계 입력
for _ in range(M):
    a, b  = map(int, sys.stdin.readline().split())
    trust[b].append(a)

for i in range(1, N+1):
    visited = [0] * (N+1)
    queue = deque([i])
    hacking[i] += 1
    visited[i] = 1
    while queue:
        now = queue.popleft()
        for t in trust[now]:
            if visited[t] == 0:
                queue.append(t)
                visited[t] = 1
                hacking[i] += 1

for i in range(1, N+1):
    if hacking[i] == max(hacking):
        print(i, end=' ')