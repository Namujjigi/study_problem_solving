from collections import deque

N, M = map(int, input().split())
wall = [list(map(int, input())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
Q = deque()
Q.append([0, 0]) # 무줙권 0,0 시작 끝은 N - 1, M - 1
wall[0][0] = '-' # 방문표시
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for k in wall:
    print(k, end='\n')

cnt_break = 0
cnt_way = 1
while Q:
    v = Q.popleft()
    sr, sc = v[0], v[1]
    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        if nr >= 0 and nr < N and nc >= 0 and nc < M and wall != '-':
            if wall[nr][nc] == 0: # 방문조건도 만족하고/ 벽도 없다면
                Q.append([nr, nc])
                wall[nr][nc] = '-'
            elif wall[nr][nc] == 1 and cnt_break != 2: # 방문조건은 만족하지만/ 벽이 있다면 한 번 까지 뿌술 수 있다.
                Q.append([nr, nc])
                wall[nr][nc] = '-'
            elif cnt_break == 2:
                break
    cnt_way += 1

for k in wall:
    print(k, end='\n')

if cnt_way == 0:
    print(-1)
else:
    print(cnt_way)