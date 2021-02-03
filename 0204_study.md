[백준2750 - 수 정렬하기](https://www.acmicpc.net/problem/2750)

```python
N = [int(input()) for _ in range(int(input()))]
# 이건 다른사람이 1줄로 적은걸 본거고
# 뭔가 깔끔하게 입력값을 정리 못하겠음

# 처음엔 이렇게 적었었음
# N = int(input())
# numbers = []
# for i in range(N):
#     numbers.append(int(input()))
# 내가 적는 수준임

set_N = set(N)
sort_N = sorted(set_N)
for number in sort_N:
    print(number)
# 브1 문제라 살짝 긴장했는데 너무 간단했다.
# set이랑 sort없이 풀어야 했나 싶음
```

