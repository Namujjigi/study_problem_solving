## [지영 공주님의 마법 거울](https://www.acmicpc.net/problem/11586)

```shell
N = int(input())
mirror = []
for i in range(N):
    mirror.append(input())
feeling = int(input())
# 백준 문제가 처음이라 input하는 방법을 잘 몰랐음
# mirror 처럼 for문으로 input도 가능

for idx in range(N):
    if feeling == 1:
        print(mirror[idx])
    if feeling == 2:
        print(mirror[idx][::-1])
    if feeling == 3:
        print(mirror[::-1][idx])
# 코드 부분은 list 배열을 새롭게 정렬하는 문제라 크게 어렵지 않게 풀었음
# if feeling == 3:인 경우 상하반전을 시켜야되기 때문에 
# mirror원래 list를 [::-1] 역순으로 먼저 재배치
# 후에 idx갯수만큼 쌓음
```