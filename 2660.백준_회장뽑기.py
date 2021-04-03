from collections import deque

N = int(input())
lst = [[] for _ in range(N + 1)]
while True:
    g, v = map(int, input().split())
    if g != -1:
        lst[g].append(v)
        lst[v].append(g)
    else:
        break

cnt = 123456789
answer_lst = []
Q = deque()
for j in range(1, N + 1):
    visit = [0 for _ in range(N + 1)]
    Q.append(j)
    visit[j] = 1
    while Q:
        v = Q.popleft()

        for i in lst[v]:
            if visit[i] == 0:
                Q.append(i)
                visit[i] = visit[v] + 1
    answer_lst.append(max(visit))
    if cnt > max(visit):
        cnt = max(visit)

candidate = 0
cand_lst = []
for i in range(len(answer_lst)):
    if answer_lst[i] == cnt:
        candidate += 1
        cand_lst.append(i + 1)
print(cnt - 1, candidate)
print(*cand_lst)
