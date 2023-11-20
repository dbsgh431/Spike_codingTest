import copy

n = int(input())

dp = [1] * 10
temp = [1] * 10
result = [sum(temp[1::])]

for _ in range(n):
    for i in range(0, 10):
        if i < 1:
            dp[0] = temp[1]
        elif i > 8:
            dp[9] = temp[8]
        if 0 < i < 9:
            dp[i] = temp[i - 1] + temp[i + 1]
    result.append(sum(dp[1::]) % 1000000000)

    temp = copy.deepcopy(dp)

print(result[n - 1])
