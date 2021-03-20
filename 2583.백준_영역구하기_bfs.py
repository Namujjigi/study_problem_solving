from collections import deque

M, N, K = map(int, input().split())
square = [[0] * N for _ in range(M)]
visit = [[0] * N for _ in range(M)]

for i in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for j in range(sy, ey):
        for k in range(sx, ex):
            square[j][k] = '-'


Q = deque()
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
cnt_lst = []
for i in range(M):
    for j in range(N):
        if square[i][j] == 0:
            cnt = 1
            square[i][j] = 1
            Q.append([i, j])

            while Q:
                v = Q.popleft()
                cr, cc = v[0], v[1]

                for k in range(4):
                    nr, nc = cr + dr[k], cc + dc[k]
                    if nr >= 0 and nr < M and nc >= 0 and nc < N and square[nr][nc] == 0:
                        square[nr][nc] = 1
                        Q.append([nr, nc])
                        cnt += 1
            cnt_lst.append(cnt)

print(len(cnt_lst))
print(*sorted(cnt_lst))