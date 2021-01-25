## [김서방 찾기](https://programmers.co.kr/learn/courses/30/lessons/12919)



```shell
def solution(seoul):
    answer = ''
    for index,name in enumerate(seoul):
    # enumerate는 각각의 값의 index와 값을 tuple형태로 반환하는 method
    # seoul = ['Jane', 'Kim']일때
    # ex) for name in enumerate(seoul)
    # (0, Jane), (1, Kim) 이런식으로
    # ex) for index, name in enumerate(seoul) 이렇게 따로도 할 수 있습니다.
        if name == 'Kim':
            answer = f'김서방은 {index}에 있다'
            #마침표를 찍어서 오류가 났는데... 시키는대로 똑같이 하자 제발..
    return answer

```



