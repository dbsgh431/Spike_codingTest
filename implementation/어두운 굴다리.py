import math

n = int(input())
m = int(input())
x = list(map(int, input().split()))

# 1.가로등이 1개인 경우) 해당 가로등 위치를 기준으로 좌, 우 거리 중 최댓값이 높이가 된다.
if m == 1:
    distance = max(abs(n - x[0]), x[0])
else:
    # 2. 가로등이 2개 이상인 경우)
    # 2-1. 먼저 양 끝에서 가장 처음 만나는 가로등 까지의 거리를 구한다.
    # 2-2. 이후 가로등 사이의 간격을 계산하는데, 올림 연산을 통해 중간에 불이 끊기는 길을 생기지 않도록 한다.
    distance = max(abs(n - x[-1]), x[0])
    for i in range(1, len(x)):
        distance = max(math.ceil((x[i] - x[i - 1]) / 2), distance)

print(distance)
