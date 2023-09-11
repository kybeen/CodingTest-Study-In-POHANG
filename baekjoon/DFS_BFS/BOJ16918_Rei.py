# 16918 - 봄버맨
import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
field = []
for _ in range(R):
    inputRow = sys.stdin.readline().rstrip()
    row = [item for item in inputRow]
    field.append(row)

bombs = deque() # 터질 폭탄의 좌표들

# 터질 폭탄의 좌표를 큐에 추가하는 함수
def addBombs():
    global R, C
    for i in range(R):
        for j in range(C):
            if field[i][j] == "O":
                bombs.append([i,j])

# 폭탄으로 채워주는 함수
def fillBombs():
    global R, C
    for i in range(R):
        for j in range(C):
            field[i][j] = "O"

# 폭탄을 터뜨리는 BFS 함수
def explodeBFS():
    while bombs:
        now = bombs.popleft()
        i, j = now[0], now[1]
        
        # 상하좌우로 폭탄이 터진다.
        if j-1 >= 0:
            field[i][j-1] = "."
        if j+1 < C:
            field[i][j+1] = "."
        if i-1 >= 0:
            field[i-1][j] = "."
        if i+1 < R:
            field[i+1][j] = "."
        field[i][j] = "."

for sec in range(1,N+1):
    if sec % 2 == 0: # 짝수 초 - 폭탄 채우기
        fillBombs()
    else: # 홀수 초 - 터질 폭탄 큐에 넣기
        if sec == 1:
            pass
        else:
            # 폭탄 터뜨리기 (BFS)
            explodeBFS()
        addBombs()

# 결과 출력
for i in range(R):
    for j in range(C):
        print(field[i][j], end='')
    print()