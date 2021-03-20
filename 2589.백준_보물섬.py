from collections import deque

def bfs(lst):
    answer = 0
    visit = [[0] * M for _ in range(N)]
    Q = deque()
    idx = lst
    visit[idx[0]][idx[1]] = 1
    Q.append(idx)

    while Q:
        # 방문점 1만들어주고
        v = Q.popleft()
        sr, sc = v[0], v[1]
        # visit[sr][sc] = 1

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr >= 0 and nr < N and nc >= 0 and nc < M and visit[nr][nc] == 0 and map[nr][nc] == 'L':
                Q.append([nr, nc])
                visit[nr][nc] = visit[sr][sc] + 1
                if visit[nr][nc] > answer:
                    answer = visit[nr][nc]
    return answer

N, M = map(int, input().split())
map = [list(input()) for _ in range(N)]

# 땅 다 받아서 땅마다 돌릴거임
stack = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 'L':
            stack.append([i, j])

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

cnt = 0
for i in stack:
    if cnt < bfs(i):
        cnt = bfs(i)
print(cnt - 1)
