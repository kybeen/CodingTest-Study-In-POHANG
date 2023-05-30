# 17073 - 나무 위의 빗물
# =========> BFS를 W만큼 반복하면서 루트 노드의 물이 모두 내려갈때까지 반복한 뒤 실제 리프 노드에 남아 있는 물의 양을 구해서 평균 구해줌
# 근데 시간 초과가 안 날 수가 없는 코드임
# 질문 게시판 봤다가 그냥 리프 노드 개수만 구해준 다음 (W/리프노드개수) 해주면 된다는 것을 알아버림
# -----> 리프 노드의 특징 : 간선이 하나
# @@@@@ 일반적인 방법으로 풀면 안 될 수도 있으니 제한시간이랑 입력값 체크해보고 시간 초과 잘 날지 안 날지 여부 빠르게 확인해서 로직 생각하기

# import sys
# from collections import deque
# import random

# N, W = map(int, sys.stdin.readline().split())
# nodes = [[] for _ in range(N+1)] # 노드의 연결 정보
# for i in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     nodes[a].append(b)
#     nodes[b].append(a)

# dq = deque()
# water = [0 for _ in range(N+1)] # 각 노드에 담긴 물
# water[1] = W

# def bfs(now):
#     visited[now] = True # 방문 표시
#     children = []
#     # 방문 여부를 체크하여 자식 노드만 담아줌
#     for n in nodes[now]:
#         if visited[n] == False:
#             children.append(n)

#     # 자식 노드가 있을 때
#     if children != []:
#         random_number = 0
#         # 2개면 랜덤으로 1개만 선택
#         if len(children) == 2:
#             random_number = random.randint(0,1)
        
#         next = children[random_number] # 물을 전달받을 노드 번호
#         dq.append(next)
#         # 물을 넘겨줌
#         water[now] -= 1
#         water[next] += 1

# for _ in range(W):
#     visited = [False for _ in range(N+1)] # 노드 방문 여부 초기화
#     dq.append(1)
#     while dq:
#         bfs(dq[0])
#         dq.popleft()
    
# leaf_num = 0
# for w in water:
#     if w != 0:
#         leaf_num += 1
# print(sum(water) / leaf_num)







# import sys
# from collections import deque
# import random

# N, W = map(int, sys.stdin.readline().split())
# nodes = [[] for _ in range(N+1)] # 노드의 연결 정보
# children = [[] for _ in range(N+1)] # 자식 노드 정보만 담긴 리스트
# for i in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     nodes[a].append(b)
#     nodes[b].append(a)

# dq = deque()
# water = [0 for _ in range(N+1)] # 각 노드에 담긴 물
# water[1] = W
# visited = [False for _ in range(N+1)] # 노드 방문 여부 초기화

# # 자식 노드 정보를 만들어 주기 위한 탐색 함수
# def bfs1(now):
#     visited[now] = True # 방문 표시
#     connected = nodes[now]
#     for c in connected:
#         if visited[c] == False:
#             children[now].append(c)
#             dq.append(c)

# dq.append(1)
# while dq:
#     bfs1(dq[0])
#     dq.popleft()


# # 물을 전달해주는 탐색 함수
# def bfs2(now):
#     child_nodes = children[now]

#     # 자식 노드가 있을 때
#     if child_nodes != []:
#         random_number = 0
#         # 2개면 랜덤으로 1개만 선택
#         if len(child_nodes) == 2:
#             random_number = random.randint(0,1)
        
#         next = child_nodes[random_number] # 물을 전달받을 노드 번호
#         dq.append(next)
#         # 물을 넘겨줌
#         water[now] -= 1
#         water[next] += 1


# for _ in range(W):
#     dq.append(1)
#     while dq:
#         bfs2(dq[0])
#         dq.popleft()
    
# leaf_num = 0
# for w in water:
#     if w != 0:
#         leaf_num += 1
# print(sum(water) / leaf_num)





# 다른 코드 참고함
# ==> 리프 노드 개수 구해서 W에 나눠주기만 하면 됨
import sys
from collections import deque
import random

N, W = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(N+1)] # 노드의 연결 정보
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

dq = deque()
visited = [False for _ in range(N+1)] # 노드 방문 여부
leaf_count = 0

def bfs(now):
    global leaf_count

    visited[now] = True # 방문 표시
    children = []
    # 방문 여부를 체크하여 자식 노드만 담아줌
    for n in nodes[now]:
        if visited[n] == False:
            children.append(n)

    # 자식 노드가 있을 때
    if children != []:
        for c in children:
            dq.append(c)
    else:
        leaf_count += 1 # 자식 노드면 개수 카운트

dq.append(1)
while dq:
    bfs(dq[0])
    dq.popleft()
    
print(W / leaf_count)