# 예시1 <음료수 얼려 먹기>
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
frame = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().rstrip()))
    frame.append(row)

result = 0
# 얼음 틀 전체를 탐색
for i in range(N):
    for j in range(M):
        if frame[i][j] == 0:
            result += 1
            queue = deque([[i, j]])
            frame[i][j] = 1
            while queue:
                now = queue.popleft()
                a, b = now[0], now[1]
                up = a-1
                down = a+1
                left = b-1
                right = b+1
                if up >= 0 and frame[up][b] == 0:
                    queue.append([up, b])
                    frame[up][b] = 1
                if down <= N-1 and frame[down][b] == 0:
                    queue.append([down, b])
                    frame[down][b] = 1
                if left >= 0 and frame[a][left] == 0:
                    queue.append([a, left])
                    frame[a][left] = 1
                if right <= M-1 and frame[a][right] == 0:
                    queue.append([a, right])
                    frame[a][right] = 1

print(result)



# 예시 풀이 (DSF)
# import sys

# # DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#     return False

# n, m = map(int, sys.stdin.readline().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().rstrip())))

# # 모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i,j) == True:
#             result += 1

# print(result) # 정답 출력