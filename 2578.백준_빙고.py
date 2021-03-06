def check(arr):
    cnt_five = 0
    for i in range(5):
        cnt_row = 0
        cnt_col = 0
        for j in range(5):
            if arr[i][j] == 0:
                cnt_row += 1
            if arr[j][i] == 0:
                cnt_col += 1

            if cnt_row == 5:
                cnt_five += 1
            if cnt_col == 5:
                cnt_five += 1
    # 어짜피 대각선은 2개밖에 없는데 그냥 하드코딩이 더 빠를듯?
    # 대각
    if arr[0][0] == 0 and arr[1][1] == 0 and arr[2][2] == 0 and arr[3][3] == 0 and arr[4][4] == 0:
        cnt_five += 1
    # 역대각
    if arr[0][4] == 0 and arr[1][3] == 0 and arr[2][2] == 0 and arr[3][1] == 0 and arr[4][0] == 0:
        cnt_five += 1
    return cnt_five

bingo = [list(map(int, input().split())) for _ in range(5)] # 철수의 빙고판
answer = [list(map(int, input().split())) for _ in range(5)] # 사회자가 부르는거

check_lst = []
for i in range(5):
    for j in range(5):
        remove = answer[i][j]
        for k in range(5):
            for l in range(5):
                if bingo[k][l] == remove:
                    bingo[k][l] = 0
                    check_lst.append(check(bingo))

for i in range(len(check_lst)):
    if check_lst[i] >= 3: # 4가될수도있음 한번에 여러개가 늘 수 도이 ㅆ엄
        print(i + 1)
        break