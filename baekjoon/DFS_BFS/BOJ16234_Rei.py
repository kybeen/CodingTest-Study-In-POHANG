# 16234 - 인구 이동
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = [] # 나라별 인구수
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
unionCnt = 0 # 연합 번호
day = 0

def BFS(start):
    global N, L, R, unionCnt, endFlag, totalPopulation, totalCountry
    dq = deque()
    dq.append([start[0], start[1]])
    
    while dq:
        now = dq.popleft()
        r, c = now[0], now[1]
        unions[r][c] = unionCnt # 시작점 연합 번호 부여
        
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            # 연합 체크 --> 유효한 자리인지 + 연합이 없는지 + 국경선을 열 수 있는지
            if 0 <= newR < N and 0 <= newC < N:
                if L <= abs(A[r][c] - A[newR][newC]) <= R:
                    if unions[newR][newC] == 0:
                        unions[newR][newC] = unionCnt # 연합 등록
                        totalPopulation += A[newR][newC] # 현재 연합의 인구수에 더해줌
                        totalCountry += 1 # 현재 연합의 국가 수에 더해줌
                        indicies.append([newR, newC])
                        dq.append([newR, newC])
                        endFlag = False
    
    # 연합국들의 인구를 똑같이 나누어준다.
    newValue = totalPopulation // totalCountry
    for union in indicies:
        A[union[0]][union[1]] = newValue

# 종료 플래그
endFlag = False

while True:
    unions = [[0]*N for _ in range(N)] # 연합 여부

    if endFlag == True:
        day -= 1
        break
    else:
        endFlag = True
        for i in range(N):
            for j in range(N):
                if unions[i][j] == 0:
                    unionCnt += 1
                    totalPopulation = A[i][j] # 현재 연합국의 총 인구수
                    totalCountry = 1 # 현재 연합국의 총 국가수
                    indicies = [[i,j]] # 현재 연합국의 인덱스들
                    BFS([i,j])
        day += 1
print(day)








# =====> 시간초과
# # 16234 - 인구 이동
# import sys
# from collections import deque

# N, L, R = map(int, sys.stdin.readline().split())
# A = [] # 나라별 인구수
# for _ in range(N):
#     row = list(map(int, sys.stdin.readline().split()))
#     A.append(row)

# unionsInfo = [[0,0]] # 연합이 된 나라들에 대한 정보 [총인구수, 국가수]
# unionCnt = 0 # 연합 번호
# day = 0

# def BFS(start):
#     global N, L, R, unionCnt, endFlag
#     dq = deque()
#     dq.append([start[0], start[1]])
    
#     while dq:
#         now = dq.popleft()
#         r, c = now[0], now[1]
#         unions[r][c] = unionCnt # 시작점 연합 번호 부여
        
#         # 연합 체크 -> 유효한 자리인지 + 연합이 없는지 + 국경선을 열 수 있는지
#         if c-1 >= 0 and unions[r][c-1] == 0 and L <= abs(A[r][c]-A[r][c-1]) <= R:
#             unions[r][c-1] = unionCnt # 연합 등록
#             unionsInfo[unionCnt][0] += A[r][c-1] # 현재 연합의 인구수에 더해줌
#             unionsInfo[unionCnt][1] += 1 # 현재 연합의 국가 수에 더해줌
#             dq.append([r, c-1])
#             endFlag = False
#         if c+1 < N and unions[r][c+1] == 0 and L <= abs(A[r][c]-A[r][c+1]) <= R:
#             unions[r][c+1] = unionCnt
#             unionsInfo[unionCnt][0] += A[r][c+1]
#             unionsInfo[unionCnt][1] += 1
#             dq.append([r, c+1])
#             endFlag = False
#         if r-1 >= 0 and unions[r-1][c] == 0 and L <= abs(A[r][c]-A[r-1][c]) <= R:
#             unions[r-1][c] = unionCnt
#             unionsInfo[unionCnt][0] += A[r-1][c]
#             unionsInfo[unionCnt][1] += 1
#             dq.append([r-1, c])
#             endFlag = False
#         if r+1 < N and unions[r+1][c] == 0 and L <= abs(A[r][c]-A[r+1][c]) <= R:
#             unions[r+1][c] = unionCnt
#             unionsInfo[unionCnt][0] += A[r+1][c]
#             unionsInfo[unionCnt][1] += 1
#             dq.append([r+1, c])
#             endFlag = False
    
#     # 연합국들의 인구를 똑같이 나누어준다.
#     newValue = unionsInfo[unionCnt][0] // unionsInfo[unionCnt][1]
#     for a in range(N):
#         for b in range(N):
#             if unions[a][b] == unionCnt:
#                 A[a][b] = newValue

# # 종료 플래그
# endFlag = False

# while True:
#     unions = [[0 for _ in range(N)] for _ in range(N)] # 연합 여부

#     if endFlag == True:
#         day -= 1
#         break
#     else:
#         endFlag = True
#         for i in range(N):
#             for j in range(N):
#                 if unions[i][j] == 0:
#                     unionCnt += 1
#                     unionsInfo.append([A[i][j], 1])
#                     BFS([i,j])
#         day += 1
# print(day)