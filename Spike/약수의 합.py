import sys

MAX = 1000000
case = int(input())
# DP 1로 초기화
dp = [1] * (MAX + 1)

sum_result = [0] * (MAX +1)

for i in range(2, MAX + 1):
    t = 1
    while i * t <= MAX:
        dp[i * t] += i
        t += 1

for i in range(1, MAX + 1):
    sum_result[i] = sum_result[i-1] + dp[i]


for _ in range(case):
    n = int(sys.stdin.readline())

    print(sum_result[n])
