n = int(input())

count = 0
if n == 1 or n == 3:
    print(-1)
else:
    count += n // 5
    n %= 5

    if n == 1:
        count += 2
    if n == 2:
        count += 1
    if n == 3:
        count += 3
    if n == 4:
        count += 2

    print(count)

