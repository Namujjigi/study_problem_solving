from collections import deque

def check(now, next):
    if now == next:
        return 0
    elif (now == 0 and next ==1) or (now == 1 and next == 0):
        return 2
    elif (now == 2 and next == 3) or (now == 3 and next == 2):
        return 2
    else:
        return 1

N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
goal = list(map(int, input().split()))
for i in range(3):
    start[i] -= 1
    goal[i] -= 1

# 동/ 서/ 남/ 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

Q = deque()
Q.append(start)
visit = [[[0] * 4 for _ in range(M)] for _ in range(N)] # N, M 크기에 각 방향마다 담으려고 0을 4개씩 넣은거임
answer = 0

while Q:
    v = Q.popleft()
    sr, sc, dir = v[0], v[1], v[2]

    if sr == goal[0] and sc == goal[1] and dir == goal[2]:
        answer = visit[sr][sc][dir]
        break

    for i in range(1, 4): # 3칸까지 한번에 이동 할 수 있음
        nr, nc = sr + dr[dir] * i, sc + dc[dir] * i
        if nr < 0 or nc < 0 or nr >= N or nc >= M: # 범위를 벗어남
            break
        if factory[nr][nc] == 1: # 경로가 없음
            break
        if visit[nr][nc][dir] == 0:
            Q.append([nr, nc, dir])
            visit[nr][nc][dir] = visit[sr][sc][dir] + 1

    for i in range(4):
        if visit[sr][sc][i] == 0:
            Q.append([sr, sc, i]) # 현재 기준으로 방향 튼거 담는건데
            visit[sr][sc][i] = visit[sr][sc][dir] + check(dir, i) # 다른 방향으로 갈땐 check해서

print(answer)