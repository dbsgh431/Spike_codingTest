N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]
num = K - 1
result = []

for _ in range(N):
    if len(arr) > num:
        result.append(arr.pop(num))

    elif len(arr) <= num:
        num %= len(arr)
        result.append(arr.pop(num))

    num += K - 1
print("<" + ', '.join(str(i) for i in result) + ">")
