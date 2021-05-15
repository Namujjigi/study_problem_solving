def backtrack(sr, sc, result):
    global answer
    if len(result) == 6:
        answer.add(result)
        return

    for k in range(4):
        nr, nc = sr + dr[k], sc + dc[k]
        if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
            backtrack(nr, nc, result + arr[nr][nc])

arr = [list(map(str, input().split())) for _ in range(5)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
answer = set()
for i in range(5):
    for j in range(5):
        backtrack(i, j, arr[i][j])

print(len(answer))