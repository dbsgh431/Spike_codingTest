import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for i in range(T):
    teams = int(sys.stdin.readline())

    scores = list(map(int, sys.stdin.readline().rstrip().split()))

    team_set = set(scores)
    total_team_score = dict()

    for t in team_set:
        if scores.count(t) == 6:
            total_team_score[t] = [t, 0, 0, 0]

    point = 1
    for team in scores:
        if team in total_team_score.keys():
            if total_team_score[team][2] == 4:
                total_team_score[team][3] = point
            if total_team_score[team][2] < 4:
                total_team_score[team][1] += point
            total_team_score[team][2] += 1
            point += 1


    total_team_score = sorted(total_team_score.values(), key=lambda x: (x[1], x[3]))

    print(total_team_score[0][0])
