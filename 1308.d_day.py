a = list(map(int, input().split()))
b = list(map(int, input().split()))

def daycount(st_year, en_year):
    leap_year = []
    for i in range(1, 10000):
        if i % 4 == 0 and i % 100 != 0:
            leap_year += [i]

        if i % 400 == 0 :
            leap_year += [i]
    # 조건의 윤년을 박스에 담음
    # 년/ 월/ 일 따로 접근할거임# for 문으로 범위주면서
    # 2월은 직접찾으면 되지 않을까?
    more_month = [1, 3, 5, 7, 8, 10, 12]
    less_month = [4, 6, 9, 11]
    day = 0

    # 방금 생각을 잘못한게 년 > 월 > 일 순으로 더해갔는데
    # 일 > 월 > 년으로 해야 달/년이 바뀌는걸 생각할 수 있음

    if st_year[0] + 1000 <= en_year[0]:
        if st_year[0] + 1000 < en_year[0]:
            return 'gg'

        if st_year[0] + 1000 == en_year[0]:
            if st_year[1] < en_year[1]:
                return 'gg'

            if st_year[1] == en_year[1]:
                if st_year[2] < en_year[2]:
                   return 'gg'

                if st_year[2] == en_year[2]:
                    return 'gg'

                if st_year[2] > en_year[2]:
                    pass

            if st_year[1] > en_year[1]:
                pass
    # '일'부분
    if st_year[0] < en_year[0]:
        if st_year[1] in more_month:
            day += 31 - st_year[2]

        elif st_year[2] in less_month:
            day += 30 - st_year[2]

        else:
            if st_year[0] in leap_year:
                day += 29 - st_year[2]

            else:
                day += 28 - st_year[2]

        # '월'부분
        if st_year[1] + 1 == 13:
            day += 0 # 12월이었으면 년도가 바뀜

        for j in range(st_year[1] + 1, 13): #12월까지 계산
            if j in more_month:
                day += 31

            if j in less_month:
                day += 30

            if j == 2:
                if st_year[0] in leap_year:
                    day += 29
                else:
                    day += 28

        for k in range(st_year[0] + 1, en_year[0]): # 마지막 전년도까지 다 더할 것
            if k in leap_year:
                day += 366

            else:
                day += 365

        for l in range(1, en_year[1]): # 월 더하기
            if en_year[0] in leap_year:
                if l in more_month:
                    day += 31

                if l in less_month:
                    day += 30

                if l == 2:
                    day += 29

            else:
                if l in more_month:
                    day += 31

                if l in less_month:
                    day += 30

                if l == 2:
                    day += 28

        day += en_year[2]

    if st_year[0] == en_year[0]: # 년도가 같을 때
        for h in range(st_year[1], en_year[1]):
            if h in more_month:
                day += 31
            if h in less_month:
                day += 30
            if h == 2:
                if st_year[0] in leap_year:
                    day += 29
                else:
                    day += 28
        day += en_year[2] - st_year[2]

    return 'D-' + str(day)

print(daycount(a, b))