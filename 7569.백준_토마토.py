from collections import deque
import sys
input = sys.stdin.readline

M, N, H = (map(int, input().split()))
tomato = [list(map(int, input().split())) for _ in range(N * H)]
A = N * H
Q = deque()
for i in range(A):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append([i, j])

dr = [-1, 0, 1, 0, N, -N]
dc = [0, -1, 0, 1, 0, 0]
result = 0
while Q:
    v = Q.popleft()
    cr, cc = v[0], v[1]

    for i in range(6):
        nr, nc = cr + dr[i], cc + dc[i]
        if i == 4 or i == 5:
            if nr >= 0 and nr < A and nc >= 0 and nc < M and cr % N == nr % N and tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[cr][cc] + 1
                result = tomato[nr][nc]
                Q.append([nr, nc])
        elif nr >= 0 and nr < A and nc >= 0 and nc < M and cr // N == nr // N and tomato[nr][nc] == 0:
            tomato[nr][nc] = tomato[cr][cc] + 1
            result = tomato[nr][nc]
            Q.append([nr, nc])

answer = 0
for i in range(A):
    for j in range(M):
        if tomato[i][j] == 0:
            answer = -1

if answer == -1:
    print(answer)
elif result == 0:
    print(result)
else:
    print(result - 1)