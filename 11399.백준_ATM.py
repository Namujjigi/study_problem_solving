N = int(input())
people = list(map(int, input().split()))
people.sort()
answer = 0
for i in range(N):
    for j in people[:i + 1]:
        answer += j

print(answer)