N = int(input())
apart = [input() for _ in range(N)]
visit = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt_lst = []

for i in range(N):
    for j in range(N):
        if apart[i][j] == '1' and visit[i][j] == 0:
            sr, sc = i, j
            visit[i][j] = 1
            Q = []
            cnt = 1
            Q.append([sr, sc])
            while Q:
                v = Q.pop(0)
                cr, cc = v[0], v[1]

                for k in range(4):
                    nr, nc = cr + dr[k], cc + dc[k]

                    if nr >= 0 and nr < N and nc >= 0 and nc < N and visit[nr][nc] == 0 and apart[nr][nc] == '1':
                        visit[nr][nc] = 1
                        cnt += 1
                        Q.append([nr, nc])
            cnt_lst.append(cnt)

print(len(cnt_lst), end=' ')
for l in sorted(cnt_lst):
    print(l, end=' ')