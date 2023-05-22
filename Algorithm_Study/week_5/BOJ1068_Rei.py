# 1068 - 트리

import sys

def dfs(n):
    global result # 함수 안에서 전역변수를 사용하려면 함수 내부에서 global 키워드로 한 번 더 선언해야함
    
    if visited[n] == True:
        return
    else:
        visited[n] = True
        if tree[n] == []:
            result += 1
            return
        else:
            # @@반례@@ : 자식 노드가 삭제돼서 리프 노드가 된 경우도 체크해줘야함
            if len(tree[n]) == 1:
                if tree[n][0] == delete:
                    result += 1
                    return
            
            for i in range(len(tree[n])):
                child = tree[n][i]
                dfs(child)

N = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())

tree = [[] for i in range(N)]
start = [] # 트리가 하나가 아닐수도
for i in range(N):
    if nodes[i] == -1:
        start.append(i) # 루트(트리의 시작지점) 설정
    else:
        tree[nodes[i]].append(i)

visited = [False for i in range(N)]
visited[delete] = True # 삭제할 노드에 방문 표시를 해놓으면 그 이후의 자식 노드들도 모두 탐색하지 않게 됨
result = 0

for s in start:
    dfs(s)
print(result)


# [ 반례 - 자식노드가 있었는데 삭제돼서 없어진 경우 ]
# 6
# 4 2 -1 4 2 3
# 5
# ==> 출력 3이 나와야 하는데 2가 나옴