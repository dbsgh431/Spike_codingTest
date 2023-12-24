import sys
from collections import deque

cases = int(sys.stdin.readline())

for _ in range(cases):
    lane = deque([])
    kids = list(map(int, sys.stdin.readline().split()))
    case_num = kids[0]
    kids.pop(0)
    back_count = 0
    lane.append(kids[0])

    for i in range(1, 20):
        for j in range(0, i):
            if kids[i] < lane[j]:
                back_count += len(lane) - j
                lane.insert(j, kids[i])
                break

        if kids[i] > lane[j]:
            lane.append(kids[i])

    print(case_num, back_count)
