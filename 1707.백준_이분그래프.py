from collections import deque

def bfs(x):
    Q = deque()
    flag = [0] * (V + 1) # 1/ -1로 구분할거다
    flag[x] = 1 # 1번부터 무줙권 시작한다 이거
    Q.append(x) # 1넣고
    while Q:
        s = Q.popleft()
        color = flag[s]
        visit[s] = 1

        for i in G[s]:
            if flag[i] == 0:
                flag[i] = -color
                Q.append(i)
            else:
                if flag[i] == color:
                    return 'NO'

    return 'YES' # 여기까지 오면 성공한거임


T = int(input())
for t_c in range(T):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    visit[1] = 1

    for _ in range(E):
        v, u = map(int, input().split())
        G[v].append(u)
        G[u].append(v)

    result = 'YES'
    for i in range(1, V + 1):
        if visit[i] == 0:
            result = bfs(i)

        if result == 'NO':
            break
    print(result)
