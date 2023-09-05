import sys


def make_candidate(arr: list):
    for i in range(2, 1000000):
        cnt = 2
        if (arr[i] == True):
            while i * cnt <= 1000000:
                arr[i * cnt] = False
                cnt += 1
    return arr


def find_case(case: int, arr: list):
    k = 3
    while k <= case - 3:
        if arr[k] and arr[case - k]:
            result = f"{case} = {k} + {case - k}"
            return result
        else:
            k += 2
    result = "Goldbach's conjecture is wrong."
    return result


arr = [1 for i in range(0, 1000001)]
arr[0], arr[1] = False, False
arr = make_candidate(arr)

while True:
    case = int(sys.stdin.readline())
    if case == 0:
        break
    else:
        print(find_case(case, arr))

