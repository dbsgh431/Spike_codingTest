import sys
import copy


def combination(numbers: list, idx: int, result: list):
    result_copy = copy.deepcopy(result)
    result_copy.append(numbers[idx])

    if len(result_copy) > 5:

        for j in range(len(result_copy) - 1):
            print(int(result_copy[j]), end=" ")
        print(int(result_copy[-1]))

    else:
        for i in range(idx + 1, len(numbers)):
            combination(numbers, i, result_copy)


while True:
    input_string = list(sys.stdin.readline().split())

    if input_string[0] == "0":
        break

    else:
        k = input_string[0]

        numbers = input_string[1:]
        for idx, n in enumerate(numbers):
            combination(numbers, idx, [])
        print()
