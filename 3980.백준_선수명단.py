def backtrack(n, result):
    global ans
    if n == 11:
        if ans < result:
            ans = result
        return

    for i in range(11):
        if visit[i] == 0 and player[n][i] != 0:
            visit[i] = 1
            backtrack(n + 1, result + player[n][i])
            visit[i] = 0

T = int(input())
for _ in range(T):
    player = [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11
    ans = 0
    backtrack(0, 0)
    print(ans)