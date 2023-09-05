import sys
case = int(input())
sum_result = [0] * 1000001
for i in (1, 1000000):
    sum_result[i] = (i * (n // i))
for i in range(case):
    n = int(sys.stdin.readline())
    sum_result = 0

    print(sum_result)
