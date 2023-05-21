# 10994 - 별 찍기 - 19

import sys

N = int(sys.stdin.readline())
len = (4 * N) - 3 # 입력값에 따른 가로세로 길이

result = [[' ' for j in range(len)] for i in range(len)] # 결과 배열을 준비해줌
center = len // 2 # 중앙 좌표
result[center][center] = '*' # 중앙에 *을 넣어줌

# 입력값이 2 이상일 때부터 테두리를 둘러줌
for i in range(2,N+1):
    padding = 2 * (i-1)
    # 기존 모양의 2칸씩 위아래에 *을 덮어줌
    for j in range(center-padding, center+padding+1):
        result[center-padding][j] = '*'
        result[center+padding][j] = '*'

    # 기존 모양의 1칸 위부터 1칸 아래까지 양쪽으로 '* '와 ' *'을 붙여줌
    for k in range(center-padding+1, center+padding):
        result[k][center-padding] = '*'
        result[k][center+padding] = '*'

# 결과 출력
for row in result:
    for r in row:
        print(r,end='')
    print('')