n = int(input())

n_input = list(map(int, input().split(" ")))


def get_difference(result: list):
    global sum_result
    summation = 0

    for i in range(1, len(result)):
        summation += abs(result[i - 1] - result[i])

    sum_result = max(sum_result, summation)

    return sum_result



result = []
sum_result = 0

def backtrack(n_input):
    if len(result) == n:
        return get_difference(result)

    for j in range(len(n_input)):
        result.append(n_input[j])
        n_input.pop(j)
        backtrack(n_input)
        n_input.insert(j, result.pop())

    return get_difference(result)


print(backtrack(n_input))
