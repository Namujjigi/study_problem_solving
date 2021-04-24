def backtrack(r):
    global result
    if r == M + 1:
        print(*result)
        return

    for i in range(1, N + 1):
        if len(result) == 0 or result[-1] < i:
            result.append(i)
            backtrack(r + 1)
            result.pop()


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
result = []
answer = []
visit = [0] * (N + 1)

backtrack(1)