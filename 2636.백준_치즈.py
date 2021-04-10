from collections import deque

def delete(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                arr[i][j] = 0

def check(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cnt += 1
    return cnt

def oven(arr):
    while Q:
        v = Q.popleft()
        sr, sc = v[0], v[1]

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr >= 0 and nr < N and nc >= 0 and nc < M and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 2
                else:
                    Q.append([nr, nc])
    return arr

N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1] # delta로 접근

time = 0
answer = 0
while check(cheese):
    visit = [[0] * M for _ in range(N)]  # 방문 표시
    Q = deque()
    Q.append([0, 0])
    visit[0][0] = 1
    cheese = oven(cheese)

    if check(cheese) != 0:
        answer = check(cheese)

    time += 1
    delete(cheese) # check에서 같이하면 한번만에 치즈가 녹을때 문제가 생김 따로 나눠서 해줘야함
print(time)
print(answer)