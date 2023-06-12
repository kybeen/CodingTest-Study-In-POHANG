# 1343 - 폴리오미노

import sys

board = sys.stdin.readline().rstrip()
board_list = []

# .와 X들을 분리해주기
temp_x = "" # 'X' 담는 리스트
temp_dot = "" # '.' 담는 리스트
for b in board:
    if b == 'X':
        temp_x += "X"
        if temp_dot != "":
            board_list.append(temp_dot)
        temp_dot = ""
    else:
        temp_dot += "."
        if temp_x != "":
            board_list.append(temp_x)
        temp_x = ""
if temp_x != "":
    board_list.append(temp_x)
if temp_dot != "":
    board_list.append(temp_dot)

result = ""
for each in board_list:
    if each[0] == '.': # '.'는 그대로 결과에 붙여주기
        result += each

    else: # 'X' 채워주기
        if len(each) % 4 == 0: # 4의 배수라면
            result += "A"*len(each)
        else:
            if len(each) % 2 == 0: # 2의 배수라면
                if len(each) == 2: # 2일 경우
                    result += "BB"
                else:
                    # AAAA부터 채워주기
                    A_length = len(each) // 4
                    result += "AAAA"*A_length
                    result += "BB"
            else: # 채울 수 없는 경우
                result = -1
                break

print(result)