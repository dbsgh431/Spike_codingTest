import sys

n, x = map(int, input().split())

visitors = list(map(int, sys.stdin.readline().split()))

max_visit = sum(visitors[:x])
result = max_visit
day = 1

for i in range(x, n):

    max_visit += visitors[i]
    max_visit -= visitors[i - x]

    if max_visit > result:
        day = 1
        result = max_visit
    elif max_visit == result:
        day += 1

if max_visit != 0:
    print(result)
    print(day)
else:
    print("SAD")



