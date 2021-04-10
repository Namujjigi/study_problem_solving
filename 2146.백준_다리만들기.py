from collections import deque

def check(spot):
    c_visit = [[0] * N for _ in range(N)]
    cq = deque()
    a = island[spot[0]][spot[1]]
    c_visit[spot[0]][spot[1]] = 1
    cq.append(spot)
    while cq:
        v = cq.popleft()
        sr, sc = v[0], v[1]

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr >= 0 and nr < N and nc >= 0 and nc < N and c_visit[nr][nc] == 0:
                if island[nr][nc] == 0:
                    cq.append([nr, nc])
                    c_visit[nr][nc] = c_visit[sr][sc] + 1
                elif island[nr][nc] != a:
                    answer.append(c_visit[sr][sc] - 1)
                    return

N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visit = [[0] * N for _ in range(N)]
s_visit = [[0] * N for _ in range(N)]
cnt = 1
search = []
answer = []
# 각 섬마다 번호를 매김
for i in range(N):
    for j in range(N):
        if island[i][j] == 1 and visit[i][j] != 1:
            visit[i][j] = 1
            Q.append([i, j])
            island[i][j] = cnt
            while Q:
                v = Q.popleft()
                sr, sc = v[0], v[1]

                for k in range(4):
                    nr, nc = sr + dr[k], sc + dc[k]
                    if nr >= 0 and nr < N and nc >= 0 and nc < N:
                        if visit[nr][nc] == 0 and island[nr][nc] == 1:
                            visit[nr][nc] = 1
                            island[nr][nc] = cnt
                            Q.append([nr, nc])
                        elif s_visit[sr][sc] == 0 and island[nr][nc] == 0:
                            s_visit[sr][sc] = 1
                            search.append([sr, sc])
            cnt += 1

for lst in search:
    check(lst)
print(min(answer))