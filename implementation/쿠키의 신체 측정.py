import sys

n = int(input())

board = []


def calculate_length(heart: list):
    results = []

    left_arm, right_arm = 0, 0
    for y in range(n):
        if board[heart[0]][y] == "*":
            if y < heart[1]:
                left_arm += 1
            if y > heart[1]:
                right_arm += 1
    results.extend([left_arm, right_arm])

    waist = 0
    for x in range(heart[0] + 1, n):
        if board[x][heart[1]] == "*":
            waist += 1
    results.append(waist)

    left_leg, right_leg = 0, 0
    for x in range(heart[0] + waist + 1, n):
        if board[x][heart[1] - 1] == "*":
            left_leg += 1
        if board[x][heart[1] + 1] == "*":
            right_leg += 1
    results.extend([left_leg, right_leg])

    print(*results)


for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if board[i][j] == "*":
            if board[i][j - 1] + board[i][j + 1] + board[i - 1][j] + board[i + 1][j] == "****":
                heart = [i, j]
                break
print(heart[0] + 1, heart[1] + 1) # 좌표의 시작이 (1,1) 이므로

calculate_length(heart)
