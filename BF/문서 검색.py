doc = input()
target = input()

start = 0
end = len(target)
cnt = 0

while len(doc) >= end:

    if target == doc[start:end]:
        cnt += 1
        start = end
        end += len(target)
    else:
        start += 1
        end += 1

print(cnt)