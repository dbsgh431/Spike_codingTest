N = int(input())

N_input = list(map(int, input().split()))

result = []

def next(n_input: list):
    for i in range(N - 1, 0, -1):
        if n_input[i] < n_input[i - 1]:
            x, y = i - 1, i
            for j in range(N - 1, x, -1):
                if n_input[j] < n_input[x]:
                    n_input[j], n_input[x] = n_input[x], n_input[j]
                    break
            break

    try:
        result = [*n_input[:x + 1], *sorted(n_input[y:],reverse=True)]
        for k in result:
            print(k, end=' ')
    except:
        print(-1)


# run
next(N_input)
