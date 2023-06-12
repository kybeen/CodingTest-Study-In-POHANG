# 2217 - 로프

import sys

N = int(sys.stdin.readline())
ropes = []
for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

# 가장 강한 로프 1개만 쓰는 경우부터 다음으로 강한 로프들을 하나씩 추가해보며 최대 무게를 구해보기
ropes.sort(reverse=True)
rope_test = [] # 로프를 하나씩 추가해볼 리스트

result = ropes[0]
for rope in ropes:
    rope_test.append(rope)
    minimum = rope_test[-1] # 현재 rope_test레스트에서 가장 약한 로프의 무게
    temp = minimum * len(rope_test) # 현재의 로프 조합으로 감당 가능한 가장 큰 무게 (가장 약한 로프 무게 * 모든 로프 개수)

    if temp >= result: # 최대 무게가 크면 결과를 갱신해준다.
        result = temp
    else:
        pass
    
print(result)