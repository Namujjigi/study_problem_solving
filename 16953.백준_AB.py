A, B = map(int, input().split())

cnt = 0
while B > A:
    if B % 10 == 1:
        B = (B - 1)/10
    else:
        B = B/2
    cnt += 1

if B == A:
    print(cnt + 1)
else:
    print(-1)