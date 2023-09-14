import sys


def find_year_v2(m, n, x, y):
    result = -1
    step = m
    k = x
    x = x % m
    y = y % n

    while k <= m * n:
        if (k % m) == x and (k % n) == y:
            return k
        k += step

    return  result


case = int(sys.stdin.readline())

for _ in range(case):
    m, n, x, y = map(int, sys.stdin.readline().split(" "))
    print(find_year_v2(m, n, x, y))


def find_year_v1(m, n, x, y):
    result = -1

    x_prime, y_prime = 0, 0
    k = 1
    while k <= (m * n):

        if x == x_prime:
            if y == y_prime:
                return k

        if x_prime < m:
            x_prime += 1
        else:
            x_prime = 0

        if y_prime < n:
            y_prime += 1
        else:
            y_prime = 0

        k += 1

    return result






