V = int(input()) # 제일 큰 컴퓨터?라고 해야하나(정점)
E = int(input()) # 간선
G = [[] for _ in range(V + 1)] # 정보를 담을 것
visit = [0] * (V + 1)
stack = []

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v) # 연결이라 양방향으로 했어야 했음
    G[v].append(u)

start = v = 1 # 1번컴퓨터에서 갈 수 있는 것만 볼거라 ㅎ 고정

visit[start] = 1 # 1번 방문하고 시작함
stack.append(start)

while stack:

    for w in G[v]:
        if visit[w] == 0:
            stack.append(v)
            visit[w] = 1
            v = w
            break

    else:
        v = stack.pop()

cnt = 0
for i in range(2, len(visit)):
    if visit[i] == 1:
        cnt += 1
print(cnt)