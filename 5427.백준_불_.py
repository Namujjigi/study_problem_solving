from collections import deque

def fire():
    fq_cnt = len(fq)
    while fq_cnt:
        v = fq.popleft()
        sr, sc = v[0], v[1]
        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr >= 0 and nr < M and nc >= 0 and nc < N and fvisit[nr][nc] == 0 and maze[nr][nc] == '.':
                maze[nr][nc] = '*'
                fvisit[nr][nc] = 1
                fq.append([nr, nc])
        fq_cnt -= 1

def bfs():
    answer = False
    cnt = 0
    while q:
        q_cnt = len(q)
        while q_cnt:
            v = q.popleft()
            sr, sc = v[0], v[1]
            for i in range(4):
                nr, nc = sr + dr[i], sc + dc[i]
                if nr >= 0 and nr < M and nc >=0 and nc < N and visit[nr][nc] == 0 and maze[nr][nc] == '.':
                    visit[nr][nc] = 1
                    maze[nr][nc] = '@'
                    maze[sr][sc] = '.'
                    q.append([nr, nc])
                elif nr < 0 or nr >= M or nc < 0 or nc >= N:
                    answer = True
                    return answer, cnt + 1
            q_cnt -= 1
        fire()
        cnt += 1
    return answer, cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    maze = [list(input()) for _ in range(M)]

    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    fq = deque()
    q = deque()

    visit = [[0] * N for _ in range(M)]
    fvisit = [[0] * N for _ in range(M)]

    # 시작 점 잡기
    for i in range(M):
        for j in range(N):
            if maze[i][j] == '@':
                q.append([i, j])
                visit[i][j] = 1
                maze[i][j] = '.'
            elif maze[i][j] == '*':
                fq.append([i, j])
                fvisit[i][j] = 1
                maze[i][j] = '*'

    fire()
    answer = bfs()

    if answer[0] == True:
        print(answer[1])
    else:
        print('IMPOSSIBLE')
