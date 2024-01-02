import sys

n, k = map(int, input().split())

rank = []

for i in range(n):
    nation, gold, silver, bronze = map(int, sys.stdin.readline().rstrip().split(" "))

    rank.append([nation, gold, silver, bronze, 0])

rank.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank_medals = [rank[0][1], rank[0][2], rank[0][3]]
rank[0][4] = 1
rank_count = 1
same_count = 1

for i in range(1, len(rank)):
    if (rank_medals[0] == rank[i][1]) and (rank_medals[1] == rank[i][2]) and (rank_medals[2] == rank[i][3]):
        rank[i][4] = rank_count
        same_count += 1
    else:
        rank_medals = [rank[i][1], rank[i][2], rank[i][3]]
        rank_count += same_count
        same_count = 1

    rank[i][4] = rank_count

for i in range(n):
    if rank[i][0] == k:
        print(rank[i][4])
        exit()
