# 11000 - 강의실 배정

# import sys
# import heapq

# N = int(sys.stdin.readline())
# lectures = {}
# # 시작시간:종료시간 쌍의 강의 딕셔너리를 만들어줌
# for _ in range(N):
#     S, T = map(int, sys.stdin.readline().split())
#     if S not in lectures.keys():
#         lectures[S] = [T]
#     else:
#         heapq.heappush(lectures[S], T) # 가장 빠른 종료시간부터 꺼낼 수 있도록 최소 힙으로 저장

# result = 0
# start_times = sorted(list(lectures.keys()))
# start_time = start_times[0]
# while True:
#     isTrailing = False # 이어서 할 수 있는 강의가 있는지
#     end_time = heapq.heappop(lectures[start_time]) # 현재의 시작 시간에서 가장 일찍 끝나는 시간을 추출
#     for start in start_times:
#         if start >= end_time: # 현재 종료 시간 이후의 시작 시간에 해당하는 강의가 있으면
#             start_time = start
#             isTrailing = True
#             break
#     if isTrailing == False: # 이어서 할 수 있는 강의가 더이상 없으면
#         result += 1
#         temp = []
#         for s in start_times:
#             # 아직 확인할게 남아있는 강의들 추리기
#             if lectures[s] != []:
#                 temp.append(s)
#         if temp == []: # 더 이상 확인할 강의가 없으면 종료
#             break
#         else:
#             start_times = temp # 남아 있는 강의 갱신
#             start_time = start_times[0]
#     else:
#         continue

# print(result)




###### 구글링한 방법 - 우선순위 큐 사용
import sys
import heapq

N = int(sys.stdin.readline())
lectures = [] # [시작시간, 종료시간] 꼴의 강의 리스트를 담은 리스트
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    lectures.append(temp)

lectures.sort() # 강의 리스트를 정렬
result_queue = [] # 우선순위 큐에 남아 있는 종료 시간의 개수가 필요한 강의실의 개수입
heapq.heappush(result_queue, lectures[0][1]) # 첫번째 강의의 종료시간을 넣어줌
for i in range(1, N): # 다음 강의부터 확인
    if lectures[i][0] < result_queue[0]: # 강의의 시작 시간이 우선순위 큐에 있는 가장 빠른 종료시간보다 이전이라면 그 강의의 종료 시간을 우선순위 큐에 추가해준다. 
        heapq.heappush(result_queue, lectures[i][1])
    else: # 강의의 시작 시간이 우선순위 큐에 있는 가장 빠른 강의의 종료시간 이후라면 가장 빠른 종료시간을 pop해주고, 현재 강의의 종료시간을 추가해줌
        heapq.heappop(result_queue)
        heapq.heappush(result_queue, lectures[i][1])
print(len(result_queue))