T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(N):
        idx, dir = map(int, input().split())
        idx -= 1
        moves = [[idx, dir]]
        # 좌
        each_dir = dir
        for i in range(idx - 1, -1, -1): # 기준점부터 0까지 역순으로 확인
            if magnets[i][2] != magnets[i + 1][6]: # 확인해야하는 자석의 2번과 비교해야할 자석의 6번이 만남
                each_dir *= -1 # 방향 바꿔주기
                moves.append([i, each_dir]) # 몇번째 자석을 어느 방향으로 돌릴지
            else:
                break # 아니라면 for문 전체를 탈출해야함


        # 우
        each_dir = dir
        for i in range(idx + 1, 4): # 기준점부터 4번째까지
            if magnets[i][6] != magnets[i - 1][2]:  # 오른쪽은 왼쪽 반대로 진행
                each_dir *= -1
                moves.append([i, each_dir])
            else:
                break

        for move in moves:
            idx, dir = move[0], move[1]
            if dir == 1:
                magnets[idx] = [magnets[idx].pop()] + magnets[idx]
            else:
                magnets[idx].append(magnets[idx].pop(0))

    answer = 0
    score_lst = [1, 2, 4, 8]
    for i in range(4):
        answer += magnets[i][0] * score_lst[i]

    print('#{} {}'.format(t_c, answer))