# 예시1 <떡볶이 떡 만들기>
import sys

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (end + start) // 2
    total_length = 0 # 잘린 떡의 총 길이
    for i in array:
        cut = i - mid # 각 떡을 자른 길이 (음수일 경우 안잘린거)
        if cut > 0:
            total_length += cut
    if total_length == target: # 잘린 떡의 총 길이가 target과 같으면 리턴
        return mid
    elif total_length > target: # 잘린 떡의 길이가 남으면 길이를 더 늘린다.
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

N, M = map(int, sys.stdin.readline().split())
ddeok = list(map(int, sys.stdin.readline().split()))
print(binary_search(ddeok, M, 0, max(ddeok)))



# # 예시 풀이
# import sys

# N, M = map(int, sys.stdin.readline().split())
# array = list(map(int, sys.stdin.readline().split()))

# start = 0
# end = max(array)

# # 이진 탐색 수행
# result = 0
# while(start <= end):
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         # 잘랐을 때 떡의 양 계산
#         if x > mid:
#             total += x-mid
#     # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
#     if total < M:
#         end = mid - 1
#     # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
#     else:
#         result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
#         start = mid + 1

# # 정답 출력
# print(result)
