total_price = int(input())
less_price = [int(input()) for _ in range(9)]

while less_price:
    total_price -= less_price.pop()

print(total_price)