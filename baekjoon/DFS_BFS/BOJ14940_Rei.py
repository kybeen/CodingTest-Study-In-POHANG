# 14940 - 쉬운 최단거리
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
field = []
visited = [] # 방문 여부
result = [] # 결과

for _ in range(n):
    visited.append([False for _ in range(m)])
    result.append([0 for _ in range(m)])
    row = list(map(int, sys.stdin.readline().split()))
    field.append(row)

dq = deque()
# 도착치 deque에 추가 및 방문 처리
for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            dq.append([i,j])
            visited[i][j] = True

while dq:
    now = dq.popleft()
    i, j = now[0], now[1]
    
    if j-1 >= 0 and field[i][j-1] == 1 and visited[i][j-1] == False: # 방문 가능한 자리를 방문하지 않았다면
        result[i][j-1] = result[i][j] + 1
        visited[i][j-1] = True
        dq.append([i,j-1])
    if j+1 < m and field[i][j+1] == 1 and visited[i][j+1] == False:
        result[i][j+1] = result[i][j] + 1
        visited[i][j+1] = True
        dq.append([i,j+1])
    if i-1 >= 0 and field[i-1][j] == 1 and visited[i-1][j] == False:
        result[i-1][j] = result[i][j] + 1
        visited[i-1][j] = True
        dq.append([i-1,j])
    if i+1 < n and field[i+1][j] == 1 and visited[i+1][j] == False:
        result[i+1][j] = result[i][j] + 1
        visited[i+1][j] = True
        dq.append([i+1,j])

# 갈 수 없는 경우 처리
for i in range(n):
    for j in range(m):
        if field[i][j] == 1 and visited[i][j] == False: # 밟을 수 있는 땅인데 방문하지 못한 땅들 처리
            result[i][j] = -1

for row in result:
    for r in row:
        print(r, end=' ')
    print()