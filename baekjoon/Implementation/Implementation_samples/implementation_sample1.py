# 예시1 <상하좌우>
import sys

N = int(sys.stdin.readline())
plan = list(sys.stdin.readline().split())

location = [0,0]
for p in plan:
    if p == "R":
        if location[1] <= N-1:
            location[1] += 1
    elif p == "L":
        if location[1] > 0:
            location[1] -= 1
    elif p == "U":
        if location[0] > 0:
            location[0] -= 1
    elif p == "D":
        if location[0] <= N-1:
            location[0] += 1

print(location[0]+1, end=' ')
print(location[1]+1)






# import sys

# n = int(sys.stdin.readline())
# x, y = 1, 1
# plans = sys.stdin.readline().split()

# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# # 이동 계획을 하나씩 확인하기
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny

# print(x, y)