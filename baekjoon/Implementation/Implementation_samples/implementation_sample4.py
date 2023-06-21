# 예시4 <문자열 재정렬>
import sys

string = sys.stdin.readline().rstrip()
start = ord("A")
end = ord("Z")

front = [] # 정답 앞부분 (알파벳))
back = [] # 정답 뒷부분 (숫자 합)
for s in string:
    if start <= ord(s) <= end: # 알파벳일 경우
        front.append(s)
    else: # 숫자일 경우
        back.append(int(s))

result = ""
try:
    front.sort() # 알파벳 정렬
    for f in front: # 결과 문자열에 알파벳을 먼저 넣어준다.
        result += f
except:
    pass
if sum(back) != 0:
    result += str(sum(back)) # 숫자의 합을 결과에 붙여줌
print(result)






# import sys

# data = sys.stdin.readline().rstrip()
# result = []
# value = 0

# # 문자를 하나씩 확인하며
# for x in data:
#     # 알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():
#         result.append(x)
#     # 숫자는 따로 더하기
#     else:
#         value += int(x)

# # 알파벳을 오름차순으로 정렬
# result.sort()

# # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#     result.append(str(value))

# # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print(''.join(result))