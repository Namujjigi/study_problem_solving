V = int(input()) # 간선개수?
a, b = map(int, input().split()) # 찾아야되는 두놈
N = int(input()) # 이 만큼 for문 돌림
G = [[] for _ in range(V + 1)]
visit = [0] * (V + 1)
stack = []
for _ in range(N):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

stack.append(a)
visit[a] = 1
while stack:
    w = stack.pop()

    for f in G[w]:
        if visit[f] == 0:
            visit[f] = visit[w] + 1
            stack.append(f)

if visit[b] == 0:
    print(-1)
else:
    print(visit[b] - 1)