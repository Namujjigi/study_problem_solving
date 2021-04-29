from heapq import heappush, heappop

def dijkstra(s, e):
    key = [123456789] * (V + 1)
    visit = [0] * (V + 1)
    Q = []
    heappush(Q, [0, s])
    key[s] = 0
    while Q:
        w, u = heappop(Q) # 가중치/ 정점
        if u == e: # 방문점이 내가 원하는 곳에 왔으면
            return key[u] # 해당 지점 방문했다면
        
        if visit[u]:
            continue
        
        visit[u] = 1
        for a, b in G[u]: # 여긴 정점, 가중치 순서임
            if visit[a] == 0 and key[a] > key[u] + b:
                key[a] = key[u] + b
                heappush(Q, [key[a], a]) # 지금 가중치랑 그 점에서 갈 수 잇는거 봐야하니까
    return key[e] # 못돌았다면 최대값이 있겠지?
        

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    v, u, w = map(int, input().split())
    G[v].append([u, w])
    G[u].append([v, w])

goal_a, goal_b = map(int, input().split())

# 순서가
# 1. 시작 a b V        2. 시작 b a V/ 일 수 있음

answer_a = dijkstra(1, goal_a) + dijkstra(goal_a, goal_b) + dijkstra(goal_b, V)
answer_b = dijkstra(1, goal_b) + dijkstra(goal_b, goal_a) + dijkstra(goal_a, V)
answer = min(answer_a, answer_b)
if answer < 123456789:
    print(answer)
else:
    print(-1)