def solution(board, moves):
    box = []
    count = 0
    for move in moves: # moves에서 하나씩 list를 빼옴
        # moves에서 빼온 숫자로 board 에 접근
        for bd in board:
            if bd[move-1] != 0:
                # box로 옮겨주는 작업을 해야 됨
                # append 이 기능을 통해 box 쌓고/ append는 list에 붙어있는 method
                box.append(bd[move-1])
                bd[move-1] = 0 # 빼온건 빈상자로 만들어줘야하니까
                # if box에 같은숫자 2개면:
                # box list의 길이를 검사하고 같은 숫자를 판별해야하니 len(box)가 먼저와야함
                if len(box) >= 2 and box[-2] == box[-1]: # -1이 마지막거 불러오는거임/ 사실 -2도 됨 ㅎㅎ;; ㅈㅅ -3도됨 ㅅㅂ
                                        # len(box) -1 이것도 방법으로 쓸 수 있음
                    box.pop() # 비어있으면 마지막걸 알아서빼고/ 숫자를 쓰면 인덱스로 찾아가서 제거해줌
                    box.pop()  # 숫자 2개 제거            
                    count += 2 # count 쌓아서 +1 * 2/ +2 하던지 택1
                break  # 하나만 쌓아야 하니까 멈춰야함(아니면 폭주기관차됨)/ 가까운 for문, while문을 탈출하는 역할/ 
    return count                                    
    # return에 몇개를 제거하게됐는지 입력

result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(result)
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# 이러면 보기힘듬