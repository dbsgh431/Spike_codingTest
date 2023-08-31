
n = int(input())
sum_result = 0
for i in range(1, n + 1):
    sum_result += i * (n//i)

print(sum_result)
# import math
#
# n = int(input())
#
# f = [0] * (n + 1)
# f[0] = 0
# f[1] = 1
#
# g = [0] * (n + 1)
# g[0] = 0
# g[1] = f[1]
#
#
# def sumofdivisors(i):
#     result = 0
#     for j in range(1, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             result += j
#             if ((j**2) != i):
#                 result += (i // j)
#     # print(i, result + i)
#     return result
#
#
# for i in range(2, n + 1):
#     f[i] = sumofdivisors(i)
#
# for i in range(2, n + 1):
#     g[i] = g[i - 1] + f[i]
#
# print(g[n])
