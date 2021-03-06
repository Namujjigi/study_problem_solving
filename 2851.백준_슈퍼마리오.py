mushroom = []
for _ in range(10):
    N = int(input())
    mushroom += [N]

total_lst = []
i = 0 # index로 접근
while i < 10:
    total = 0
    for j in range(i + 1):
        total += mushroom[j]
    total_lst += [total]
    i += 1

abs_lst = []
abs_cnt = 0
for i in total_lst:
    abs_cnt = abs(100 - i)
    abs_lst += [abs_cnt]

min_number = 10000000
a= 0 # 나중에 출력할 때 index로 접근할 거
for i in range(len(abs_lst)):
    if min_number >= abs_lst[i]:
        min_number = abs_lst[i]
        a = i
print(total_lst[a])