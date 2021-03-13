def area(arr, N):
    visit = [[0] * N for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                color = arr[i][j]
                visit[i][j] = 1
                sr, sc = i, j
                Q.append([sr, sc])

                while Q:
                    v = Q.pop(0)
                    cr, cc = v[0], v[1]

                    for k in range(4):
                        nr, nc = cr + dr[k], cc + dc[k]
                        if nr >= 0 and nr < N and nc >= 0 and nc < N and visit[nr][nc] == 0 and arr[nr][nc] == color:
                            visit[nr][nc] = 1
                            Q.append([nr, nc])
                cnt += 1 # Q를 한번 다 돌리고 돌아야지
    return cnt

N = int(input())
colors = [input() for _ in range(N)]
color_weak = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if colors[i][j] == 'R':
            color_weak[i][j] = 'G'
        else:
            color_weak[i][j] = colors[i][j]
print(area(colors, N), end=' ')
print(area(color_weak, N))