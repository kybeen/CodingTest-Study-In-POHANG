# 1991 - 트리 순회

import sys

# 전위순회 (루트 -> 왼쪽자식 -> 오른쪽자식)
def dfs(root):
    # 루트부터 바로 출력하며 탐색
    print(root, end='')
    # 왼쪽 자식 -> 오른쪽 자식 순서대로
    for i in range(2):
        child = nodes[root][i]
        if child != '.':
            dfs(child)

# 중위순회 (왼쪽자식 -> 루트 -> 오른쪽자식)
def dfs2(root):
    left = nodes[root][0]
    if left != '.':
        dfs2(left)
    print(root, end='') # 왼쪽 끝까지 탐색하고 나면 출력

    # 왼쪽 탐색 끝났으면 오른쪽 탐색 시작
    right = nodes[root][1]
    if right != '.':
        dfs2(right)

# 후위순회 (왼쪽자식 -> 오른쪽자식 -> 루트)
def dfs3(root):
    left = nodes[root][0]
    if left != '.':
        dfs3(left)
        print(left, end='') # 가장 왼쪽 끝의 자식까지 탐색하면 출력
    
    right = nodes[root][1]
    if right != '.':
        dfs3(right)
        print(right, end='') # 가장 오른쪽 끝의 자식까지 탐색하면 출력

N = int(sys.stdin.readline())
nodes = {}
for i in range(N):
    root, left, right = sys.stdin.readline().split()
    nodes[root] = [left, right]

dfs('A') # 전위순회 A부터 시작
print('')
dfs2('A') # 중위순회 A부터 시작
print('')
dfs3('A') # 후위순회 A부터 시작
print('A') # 후위순회의 끝에 루트 출력해주기