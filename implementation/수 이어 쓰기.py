n = list(input())

count = 1
target = n[0]


while True:
    str_count = list(str(count))

    for s in str_count:

        if s in target[0] and len(n) != 0:
            n.pop(0)
            if len(n) == 0:
                break
            target = n[:len(str_count)]
    if len(n) == 0:
        break
    count += 1
print(count)
