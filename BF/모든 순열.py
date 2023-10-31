import time
N = int(input())

n_input = [n + 1 for n in range(N)]


def log_console(result):
    print(" ".join(map(str, result)))


def cal_factorial(n):
    if n == 1:
        return n
    return n * cal_factorial(n - 1)


# 1. 브루트포스를 이용한 다음순열 탐색
def permutation(n, n_input):
    for _ in range(cal_factorial(n)):
        log_console(n_input)
        for i in range(n - 1, 0, -1):
            if n_input[i] > n_input[i - 1]:
                x, y = i - 1, i
                for j in range(n - 1, x, -1):
                    if n_input[j] > n_input[x]:
                        n_input[j], n_input[x] = n_input[x], n_input[j]
                        break
                break
        try:
            n_input = [*n_input[:x + 1], *sorted(n_input[y:])]


        except:
            return

start = time.time()
permutation(N, n_input)
print("방법 1", time.time() - start)


n_input = sorted(n_input)
print("________")

result2 = []


# 2. 백트래킹을 통한 풀이
def backtrack(n_input):
    if len(result2) == N:
        log_console(result2)
        return

    for j in range(len(n_input)):
        result2.append(n_input[j])
        n_input.pop(j)
        backtrack(n_input)
        n_input.insert(j, result2.pop())
    return


start = time.time()
backtrack(n_input)
print("방법 2", time.time() - start)