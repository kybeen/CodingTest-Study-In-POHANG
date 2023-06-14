# 11000 - 강의실 배정

import sys

N = int(sys.stdin.readline())
lectures = {}
# 시작시간:종료시간 쌍의 강의 딕셔너리를 만들어줌
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    if S not in lectures.keys():
        lectures[S] = [T]
    else:
        lectures[S].append(T)

def dfs(start):
    if lectures[start] != []:
        end = lectures[start][0]
        lectures = lectures[1:]
        dfs(end)
    else:
        result += 1
    return

result = 0
start_time = lectures.keys()
for start in start_time:
        dfs(start)


print(result)