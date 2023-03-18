# # 1874 - 스택 수열
# import sys
# from collections import deque

# n = int(sys.stdin.readline())
# arr = deque() # 수열
# my_arr = []
# result = []

# for i in range(n):
#     num = int(sys.stdin.readline())
#     arr.append(num)

# my_arr.append(1)
# result.append("+")

# i = 2
# while True:
#     if my_arr[-1] == arr[0]:
#         result.append("-")
#         my_arr.pop()
#         arr.popleft()
#     elif i <= n:
#         result.append("+")
#         my_arr.append(i)
#         i += 1
#     else:
#         break

# if len(arr) == 0:
#     for r in result:
#         print(r)
# else:
#     print("NO")