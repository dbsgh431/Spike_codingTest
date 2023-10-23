N, S = map(int, input().split(" "))

n_input = list(map(int, input().split()))

result = []


count = 0

def bactrack(i, n_input: list, M):
    global count
    if len(result) == M:
        print(result)
        if sum(result) == S:
            count += 1
        return

    for j in range(i, len(n_input)):

        result.append(n_input[j])
        n_input.pop(j)
        bactrack(j, n_input, M)
        n_input.insert(j, result.pop())

    return


# run
for i in range(1, N + 1):
    bactrack(0, n_input, i)
print(count)
