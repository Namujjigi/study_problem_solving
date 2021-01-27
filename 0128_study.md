## [블랙잭](https://www.acmicpc.net/problem/2798)

```python
N, M = map(int, input().split())
cards = [int(i) for i in input().split()]
# 백준은 입력하는 방식에 익숙해질것!

sum_box = []
for idx1 in range(len(cards)-1):
    for idx2 in range(idx1+1, len(cards)): # for 중첩해서 쓸 때 범위 조심해야함
        for idx3 in range(idx2+1, len(cards)):
            answer = cards[idx1] + cards[idx2] + cards[idx3]
            if answer <= M:
                sum_box.append(answer)
result = max(sum_box) # 여기서 sum_box를 한번 더 돌아야하는 불편함 
print(result)
```



```python
N, M = map(int, input().split())
Cs = [int(c) for c in input().split()]

res = -1
for i in range(len(Cs)):
    for j in range(i+1, len(Cs)):
        for k in range(j+1, len(Cs)):
            tmp = Cs[i] + Cs[j] + Cs[k]
            if res < tmp <= M:
                res = tmp #이런식으로 변수를 바꿔가면서 비교하면 따로 list를 만들지 않아도 됨

print(res)
```



