n = int(input())

t_list = []
p_list = []

dp = [0 for _ in range(n + 1)]

for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n-1, -1, -1):
    if t_list[i] + i > n:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], dp[t_list[i] + i] + p_list[i])

print(dp[0])

