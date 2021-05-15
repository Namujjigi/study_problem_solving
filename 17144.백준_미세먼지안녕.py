from copy import deepcopy

def airDiffusion():
    dust_location = []
    for i in range(R):
        for j in range(C):
            if dust[i][j] != 0 and dust[i][j] != -1:
                dust_location.append([i, j, dust[i][j]])

    while dust_location:
        sr, sc, now_dust = dust_location.pop()
        diffuse_dust = now_dust // 5
        tmp = 0
        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr >= 0 and nr < R and nc >= 0 and nc < C and dust[nr][nc] != -1:
                dust[nr][nc] += diffuse_dust
                tmp += 1
        dust[sr][sc] -= (diffuse_dust * tmp)
    return

def airCleaner(arr):
    global air_cleaner
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                air_cleaner.append([i, j])
                air_cleaner.append([i + 1, j])
                return

def airMove():
    new_dust = deepcopy(dust)

    x1, y1 = air_cleaner[0][0], air_cleaner[0][1]
    x2, y2 = air_cleaner[1][0], air_cleaner[1][1]

    sr, sc = x1, y1 + 1
    dust[sr][sc] = 0
    for r, c in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
        while True:
            nr, nc = sr + r, sc + c
            if nr < 0 or nr > x1 or nc < 0 or nc >= C:
                break
            if dust[nr][nc] == -1:
                break
            else:
                dust[nr][nc] = new_dust[sr][sc]
            sr, sc = nr, nc

    sr, sc = x2, y2 + 1
    dust[sr][sc] = 0
    for r, c in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        while True:
            nr, nc = sr + r, sc + c
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                break
            if dust[nr][nc] == -1:
                break
            else:
                dust[nr][nc] = new_dust[sr][sc]
            sr, sc = nr, nc

def dustCount():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if dust[i][j] != -1:
                cnt += dust[i][j]
    return cnt

R, C, T = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

air_cleaner = []
airCleaner(dust)
tmp = 1
while tmp <= T:
    airDiffusion()
    airMove()
    tmp += 1

print(dustCount())
