ROWS = 5
COLS = 6
matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for i in range(ROWS):
    for j in range(COLS):
        if i % 2 == 0:
            matrix[i][COLS -1 - j] = int(input('Введите элеменет [{}][{}]: '.format(i,COLS-1-j)))
        else:
            matrix[i][j] = int(input('Введите элеменет [{}][{}]: '.format(i, j)))

for i in range(ROWS):
    print(matrix[i])