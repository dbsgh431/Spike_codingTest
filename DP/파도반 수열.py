import sys

T = int(input())
arr = [0 for _ in range(100)]
arr[0] = 1
arr[1] = 1
arr[2] = 1


# 규칙성 메모이제이션
for i in range(3,100):
    arr[i] = arr[i-3] + arr[i-2]


for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(arr[n-1])