import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and visit[nx][ny] == 0:
            visit[nx][ny] = 1 # 방문하면 1로만들고
            cnt += 1 # 방문할때마다 몇갠지 세고
            dfs(nx, ny)
    else:
        return cnt
        

M, N, K = map(int, input().split())
visit = [[0] * N for _ in range(M)]

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(M - ey, M - sy):
        for j in range(sx, ex):
            visit[i][j] = '-' # 0이 벽이고

# 여기서 visit을 dfs하면 안되나?

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = []
for i in range(M):
    for j in range(N):
        if visit[i][j] == 0:
            x, y = i, j
            visit[x][y] = 1 # 방문하니까 1로 만들고
            cnt = 1
            value = dfs(x, y)
            answer.append(value)

print(len(answer))
for i in sorted(answer):
    print(i, end=' ')