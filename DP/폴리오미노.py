board = input()

if ("XXXX" in board):
    board = board.replace("XXXX", "AAAA")

if ("XX" in board):
    board = board.replace("XX", "BB")

if ("X" in board):
    print(-1)
else:
    print(board)