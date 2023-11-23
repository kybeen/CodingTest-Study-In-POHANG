# 다익스트라 알고리즘 구현2 - 힙(Heap) 사용
# 노드 개수가 10,000개 이상이라면 힙(Heap)을 사용해야 한다.
"""
[입력]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 3
4 3 3
4 5 1
5 3 1
5 6 2

[출력]
0
2
3
1
2
4
"""
import sys
import heapq

n, m = map(int, sys.stdin.readline().split()) # n: 노드의 개수 / m: 간선의 개수
start = int(sys.stdin.readline()) # 시작 노드
INF = 1e8 # 임의의 큰 값

graph = [[] for _ in range(n+1)] # 노드의 연결 정보를 담을 리스트
distance = [INF] * (n+1) # 시작 노드에서 각 노드까지의 최단거리 테이블

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split()) # a: 출발노드, b: 도착노드, c: 연결된 간선의 가중치
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # q가 비어있지 않다면
    while q:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리됐다면 skip (더 작은 값이라면 이미 처리된것이기 때문)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거치면 이동 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])