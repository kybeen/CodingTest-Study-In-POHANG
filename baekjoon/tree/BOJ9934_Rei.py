# 9934 - 완전 이진 트리
# 입력으로 받는 건물 리스트를 가운데를 기준으로 쪼개 가면서 정답에 넣어준다.

import sys
from collections import deque

def split_tree(node):
    arr = node[0]
    depth = node[1]

    nodes_count = len(arr)
    center_idx = nodes_count // 2
    left, center, right = arr[:center_idx], arr[center_idx], arr[center_idx+1:]
    result[depth].append(center)
    if left != []:
        dq.append((left, depth+1))
    if right != []:
        dq.append((right, depth+1))

K = int(sys.stdin.readline()) # 깊이
buildings = list(map(int, sys.stdin.readline().split())) # 방문한 건물 리스트

nodes_count = 2**K-1 # 노드의 개수 2^K-1
result = [[] for _ in range(K)]
dq = deque()
dq.append((buildings, 0)) # (리스트, 깊이) 쌍의 튜플을 dq에 넣어줌

# 반복문을 돌며 dq를 가운데를 기준으로 쪼개며 정답 리스트를 만들어준다.
while dq:
    split_tree(dq[0])
    dq.popleft()

for row in result:
    for r in row:
        print(r, end=" ")
    print()