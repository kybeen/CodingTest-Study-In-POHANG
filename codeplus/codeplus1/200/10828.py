# 10828 - 스택
import sys

stk = []
N = int(sys.stdin.readline())

for i in range(N):
    cmd = str(sys.stdin.readline())
    cmd2 = cmd.split()

    if len(cmd2) == 2:
        stk.append(int(cmd2[1])) # push
    else:
        if cmd2[0] == "pop":
            if len(stk) == 0:
                print(-1)
            else:
                a = stk.pop()
                print(a)
        elif cmd2[0] == "size":
            print(len(stk))
        elif cmd2[0] == "empty":
            if len(stk) == 0:
                print(1)
            else:
                print(0)
        elif cmd2[0] == "top":
            if len(stk) == 0:
                print(-1)
            else:
                print(stk[-1])