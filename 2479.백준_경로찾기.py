# pypy로 하긴 했음 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
from collections import deque

N, M = map(int, input().split())
code = [input() for _ in range(N)]
G = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
answer = [[] for _ in range(N + 1)]
# 해밍 확인해서 담기
for i in range(N): # 전체 코드의 범위에서
    for j in range(N):
        if i != j:
            cnt = 0
            for k in range(M): # 자리 수 하나씩 비교할거다
                if code[i][k] != code[j][k]:
                    cnt += 1
            if cnt == 1:
                G[i + 1].append(j + 1) # for문을 두번 갈겼으니 양방향은 자동임


s, g = map(int, input().split())
Q = deque()
Q.append(s)
visit[s] = 1

while Q:
    p = Q.popleft()

    for w in G[p]:
        if visit[w] == 0:
            visit[w] = 1
            Q.append(w)
            answer[w].append(p)

lst = [g]
if answer[g]:
    v = answer[g][0]
    lst.append(v)
    while v != s:
        v = answer[v][0]
        lst.append(v)
    print(*lst[::-1])
else:
    print(-1)