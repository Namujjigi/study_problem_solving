arr = [list(map(int, input().split())) for _ in range(9)]
visit = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            visit.append([i, j])

print(arr)
print(visit)

# def 가능성있는 놈들 찾기 해당칸에서
# 가로 세로 3바이3 확인해서

# DFS로 가면되려나...?