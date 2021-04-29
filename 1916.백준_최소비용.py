from heapq import heappush, heappop

def dijkstra(s, e):
    key = [1234566789] * (V + 1)
    visit = [0] * (V + 1)
    key[s] = 0
    Q = [[0, s]] # 시작점은 가중치 0으로
    while Q:
        w, u = heappop(Q)
        if w > key[u]:
            continue

        if u == e:
            return key[u]

        visit[u] = 1

        for a, b in G[u]: # 정점/ 가중치 순서
            if visit[a] == 0 and key[a] > key[u] + b:
                key[a] = key[u] + b
                heappush(Q, [key[a], a])


V = int(input())
E = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    v, u, w = map(int, input().split())
    G[v].append([u, w])

s, e = map(int, input().split())
print(dijkstra(s, e))