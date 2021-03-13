from collections import deque

N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
visit = [[0] * N for _ in range(M)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
Q = deque()

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            Q.append([i, j])
result = 0
while Q:
    v = Q.popleft()
    cr, cc = v[0], v[1]
    for k in range(4):
        nr, nc = cr + dr[k], cc + dc[k]
        if nr >= 0 and nr < M and nc >= 0 and nc < N and tomato[nr][nc] == 0:
            tomato[nr][nc] = tomato[cr][cc] + 1
            result = tomato[nr][nc]
            Q.append([nr, nc])

answer = 0
for i in range(M):
    for j in range(N):
        if tomato[i][j] == 0:
            answer = -1

if answer == -1:
    print(answer)
elif result == 0:
    print(result)
else:
    print(result - 1)