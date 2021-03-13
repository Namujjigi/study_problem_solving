for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] = 1
                Q.append([i, j])

                while Q:
                    v = Q.pop()
                    sr, sc = v[0], v[1]

                    for k in range(4):
                        nr, nc = sr + dr[k], sc + dc[k]
                        if nr >= 0 and nr < N and nc >= 0 and nc < M and visit[nr][nc] == 0 and cabbage[nr][nc] == 1:
                            visit[nr][nc] = 1
                            Q.append([nr, nc])
                cnt += 1
    print(cnt)