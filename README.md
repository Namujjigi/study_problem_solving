## [핸드폰 번호 가리기](https://programmers.co.kr/learn/courses/30/lessons/12948)

```python

def solution(phone_number):
    ph_nb = len(phone_number) -4 #뒤에 4자리를 제외하고 *표시 
    answer = ph_nb * '*' + phone_number[-4:] #뒤에 4자리만 출력
    return answer
    
```