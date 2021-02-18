# 어떤경우든 8바이 8을 따오고
# delta 좌/하 만 접근해서
# B일때는 W인지/ W일때는 B인지 확인하고
    # 같으면 바꾸고 cnt +1
    # 다르면 pass

# 목록받고
N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

start_points = [] # 8바이 8을 검사하는 시작점을 받아옴
for i in range(N - 7): # N, M 크기만큼만 돌리면되니까
    for j in range(M - 7):
        point = [i, j]
        start_points += [point]

cnt_box = []
for start_point in start_points: # 시작점을 기준으로 8칸씩 검사한다
    cnt_w = 0  # 바뀐횟수 셀거다 하얀색을 기준으로 바꿀 때
    cnt_b = 0  # 검은색을 기준으로 바꿀 때
    for row in range(start_point[0], start_point[0] + 8):
        for col in range(start_point[1], start_point[1] + 8):
            # 4가지 경우 시작이 홀 + B/ 홀 + W/ 짝 + B/ 짝 + W
            if (row + col) % 2 == 0: # 시작이 짝수기준
                if chess[row][col] == 'W':
                    cnt_b += 1
                else:
                    cnt_w += 1
            else:
                if chess[row][col] == 'W':
                    cnt_w += 1
                else:
                    cnt_b += 1

    cnt_box.append(cnt_w)
    cnt_box.append(cnt_b)

print(min(cnt_box))