from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
q = deque([])
for _ in range(n):
    order = input().split()
    if order[0] == 'push_back':
        q.append(int(order[1]))
    elif order[0] == 'push_front':
        q.appendleft(int(order[1]))
    elif order[0] == 'pop_front':
        if q : print(q.popleft())
        else: print(-1)
    elif order[0] == 'pop_back':
        if q : print(q.pop())
        else: print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q : print(0)
        else: print(1)
    elif order[0] == 'front':
        if q : print(q[0])
        else: print(-1)
    elif order[0] == 'back':
        if q : print(q[-1])
        else: print(-1)