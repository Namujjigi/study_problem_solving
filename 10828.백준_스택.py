import sys
input=sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = input().split()

    # push일때 # 123이런게 들어오면 123 이 들어가야함
    if order[0] == 'push':
        stack.append(order[1])

    #pop
    if order[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())

    #size
    if order[0] == 'size':
        print(len(stack))

    #empty
    if order[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')

    #top
    if order[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])