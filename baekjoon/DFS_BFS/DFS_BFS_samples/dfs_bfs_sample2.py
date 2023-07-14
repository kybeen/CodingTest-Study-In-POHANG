# 예시2 <미로 탈출>
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
miro = []
for _ in range(N):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[0 for _ in range(M)] for _ in range(N)] # 최단 이동 거리를 표시하는 배열

queue = deque([[0, 0]]) # 시작 위치 큐에 넣기
visited[0][0] = 1

while queue:
    now = queue.popleft()
    a, b = now[0], now[1]
    up = a-1
    down = a+1
    left = b-1
    right = b+1
    # 상,하,좌,우로 갈 수 있고, 아직 방문하지 않았다면 현재 칸의 visited 값에서 1을 더한 값을 넣어준다.
    if up >= 0 and miro[up][b] == 1 and visited[up][b] == 0:
        queue.append([up ,b])
        visited[up][b] = visited[a][b] + 1
    if down <= N-1 and miro[down][b] == 1 and visited[down][b] == 0:
        queue.append([down, b])
        visited[down][b] = visited[a][b] + 1
    if left >= 0 and miro[a][left] == 1 and visited[a][left] == 0:
        queue.append([a, left])
        visited[a][left] = visited[a][b] + 1
    if right <= M-1 and miro[a][right] == 1 and visited[a][right] == 0:
        queue.append([a, right])
        visited[a][right] = visited[a][b] + 1

print(visited[N-1][M-1])




# # 답안 코드
# import sys
# from collections import deque

# # BFS 소스코드로 구현
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n-1][m-1]

# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, sys.stdin.readline().split())
# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().rstrip())))

# # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS를 수행한 결과 출력
# print(bfs(0, 0))