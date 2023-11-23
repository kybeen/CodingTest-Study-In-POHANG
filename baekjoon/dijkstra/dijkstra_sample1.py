# 다익스트라 알고리즘 구현1
# 단계마다 방문하지 않는 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인한다.
# 전체 노드 개수가 5,000개 이하라면 이 방법으로 해결 가능. 노드 개수가 10,000개 이상이라면 힙(Heap)을 사용한 개선된 알고리즘을 써야 한다.
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

n, m = map(int, sys.stdin.readline().split()) # n: 노드의 개수 / m: 간선의 개수
start = int(sys.stdin.readline()) # 시작 노드
INF = 1e8 # 임의의 큰 값

graph = [[] for _ in range(n+1)] # 노드의 연결 정보를 담을 리스트

visited = [False] * (n+1) # 방문 체크
distance = [INF] * (n+1) # 시작 노드에서 각 노드까지의 최단거리 테이블

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split()) # a: 출발노드, b: 도착노드, c: 연결된 간선의 가중치
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대한 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우라면 갱신
            distance[j[0]] = min(distance[j[0]], cost)

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])