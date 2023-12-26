import sys

n, game_type = sys.stdin.readline().rstrip().split(" ")

game_player = {'Y': 1, 'F': 2, 'O': 3}

names_set = set()
for i in range(int(n)):
    nickname = sys.stdin.readline().rstrip()
    names_set.add(nickname)

print(len(names_set)  // game_player[game_type])
