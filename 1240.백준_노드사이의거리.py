from heapq import heappush, heappop

def dijkstra(s, e):
    key = [123456789] * (V + 1)
    visit = [0] * (V + 1)
    key[s] = 0
    visit[s] = 1
    Q = [[0, s]]

    while Q:
        w, u = heappop(Q)
        if w > key[u]:
            continue

        if u == e:
            return key[u]

        visit[u] = 1

        for a, b in G[u]:
            if visit[a] == 0 and key[a] > key[u] + b:
                key[a] = key[u] + b
                heappush(Q, [key[a], a])



V, M = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    v, u, w = map(int, input().split())
    G[v].append([u, w])
    G[u].append([v, w])

for _ in range(M):
    s, e = map(int, input().split())
    print(dijkstra(s, e))