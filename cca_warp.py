def display(arr):
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()


def cca():
    board2 = []
    el = []
    c = 1
    for i in range(rows):
        board2.append([])
        for j in range(cols):
            board2[i].append(0)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                board2[i][j] = "X"
    display(board2)
    print()
    for i in range(1, rows):
        for j in range(1, cols):
            if board2[i][j] == "X":
                if board2[i - 1][j] == 0 and board2[i][j - 1] == 0:
                    board2[i][j] = c
                    c = c + 1
                elif board2[i - 1][j] == 0 or board2[i][j - 1] == 0:
                    board2[i][j] = max(board2[i - 1][j], board2[i][j - 1])
                else:
                    board2[i][j] = min(board2[i - 1][j], board2[i][j - 1])
                if not board2[i - 1][j] == board2[i][j - 1]:
                    if not (board2[i - 1][j] == 0 or board2[i][j - 1] == 0):
                        el.append(
                            [
                                max(board2[i - 1][j], board2[i][j - 1]),
                                min(board2[i - 1][j], board2[i][j - 1]),
                            ]
                        )
    display(board2)
    print()
    print(el)
    print()


rows, cols = (10, 10)

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

cca()
