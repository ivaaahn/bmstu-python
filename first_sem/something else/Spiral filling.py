COLS = 3
ROWS = 3
a = [[0 for _ in range(COLS)] for _ in range(ROWS)]

numOfCircle = min(COLS, ROWS) // 2 + min(COLS, ROWS) % 2

k = 0
start_col = 0
end_col = COLS

start_row = 0
end_row = ROWS

for c in range(numOfCircle):
    for i in range(start_col, end_col):
        a[c][i] = k
        k += 1

    for j in range(start_row + 1, end_row - 1):
        a[j][COLS - 1 - c] = k
        k += 1

    if start_row != end_row - 1:
        for i in range(end_col - 1, start_col - 1, -1):
            a[ROWS - 1 - c][i] = k
            k += 1

    if start_col != end_col - 1:
        for j in range(end_row - 2, start_row, -1):
            a[j][c] = k
            k += 1

        start_col += 1
        end_col -= 1

        start_row += 1
        end_row -= 1

for i in range(ROWS):
    print(a[i])
