from collections import deque

def backtrack(s):
    Q = deque()
    Q.append(s)
    while Q:
        v = Q.popleft()
        if v == M:
            return visit[v]
        if v * 2 <= 100000 and visit[v * 2] == 0:
            visit[v * 2] = visit[v] + 1
            Q.append(v * 2)
        if v + 1 <= 100000 and visit[v + 1] == 0:
            visit[v + 1] = visit[v] + 1
            Q.append(v + 1)
        if v - 1 >= 0 and visit[v - 1] == 0:
            visit[v - 1] = visit[v] + 1
            Q.append(v - 1)

N, M = map(int, input().split())
visit = [0] * 100001
visit[N] = 1
print(backtrack(N) - 1)