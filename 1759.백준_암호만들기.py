def backtrack(cnt, idx):
    global ans, result

    if cnt == N:
        tmp_v = 0
        tmp_c = 0
        word = ''.join(result)
        for k in word:
            if k in 'aieou':
                tmp_v += 1
            else:
                tmp_c += 1
        if tmp_v >= 1 and tmp_c >= 2:
            print(word)
        return

    for i in range(idx, M):
        if visit[i] == 0:
            visit[i] = 1
            result.append(words[i])
            backtrack(cnt + 1, i + 1)
            visit[i] = 0
            result.pop()

N, M = map(int, input().split())
words = list(map(str, input().split()))
words = sorted(words)
visit = [0] * M
ans = {}
result = []
backtrack(0, 0)
