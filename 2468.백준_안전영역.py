from collections import deque

def bfs(arr, height): # 지역 리스트랑 물에 잠기는 지점 받을 거임
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    visit = [[0] * N for _ in range(N)]
    Q = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and visit[i][j] != 1:
                Q.append([i, j])
                visit[i][j] = 1
                while Q:
                    v = Q.popleft()
                    sr = v[0]
                    sc = v[1]
                    for k in range(4):
                        nr, nc = sr + dr[k], sc + dc[k]
                        if nr >= 0 and nr < N and nc >= 0 and nc < N and arr[nr][nc] > height and visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            Q.append([nr, nc])
                cnt += 1
    return cnt

N = int(input())
area = []
danger = []
answer_lst = []
for _ in range(N):
    A = list(map(int, input().split()))
    area.append(A)
    danger.append(max(A))

for i in range(max(danger) + 1):
    answer_lst.append(bfs(area, i))

print(max(answer_lst))