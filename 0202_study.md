## [분해합](https://www.acmicpc.net/problem/2231)

```python
# 오답인데 왜지...?
# 접근 방법의 문제점
# while과 for문을 같이 써야함
# 마지막에 결과가 없다면 0을 출력해야하는데 이 부분과 같이 작성하려니
# 출력할 때 오류가 발생함
# map을 사용하지 않고 풀어서 해보려고했는데 건방진 생각이었음
N = int(input())

# while문으로 숫자가 N보다 작을때만 검사
# for문으로 enumerate 쓰면 안될까? idx값으로 각각 접근
# 같은 순간 break하고 출력할거임

i = 1
while i < N:
    answer = 0
    for idx, number in enumerate(str(i)):
        answer += int(str(i)[idx])
        result = i + answer
        if result == N:
            print(i)
            break
        elif i == N-1:
            print(0)
            i += 1
        else:
            i += 1

```

```python
# 여기가 정답
N = int(input())
answer = 0
for number in range(1, N+1):
    number_list = list(map(int, str(number))) #map을 쓰면 for문 한번으로 해결
    answer = number + sum(number_list)
    if answer == N:
        print(number)
        break # 왜 위 처럼 했을 땐 break가 작동을 안했지?
    if number == N:
        print(0)
```

