# 11399 - ATM

import sys

N = int(sys.stdin.readline())
extract_time = list(map(int, sys.stdin.readline().split()))

extract_time.sort() # 빨리 끝나는 사람부터 오름차순 정렬
result_list = []
temp = 0
for time in extract_time:
    temp += time
    result_list.append(temp)

print(sum(result_list))