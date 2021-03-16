def get_amount(num_of_rows: int, column: int, mat: list):
    gl = 'уеэоаыяию'
    counter = 0
    counter_max = 0
    for row in range(num_of_rows):
        if mat[row][column] in gl:
            counter += 1
        else:
            if counter > counter_max:
                counter_max = counter
            counter = 0
        counter_max = max(counter, counter_max)
    return counter_max


def get_start_values():
    m, n = map(int, input('Введите количество строк и столбцов через запятую: ').split(','))
    return m, n


def get_matrix(rows: int) -> list:
    m = []
    for i in range(rows):
        m.append(input('Введите строку №{}: '.format(i + 1)).split())
    return m


def get_best_column(a: list):
    best_col = 0
    index = 0
    for j in range(COLS):
        cur_col = get_amount(ROWS, j, matrix)
        if cur_col > best_col:
            best_col = cur_col
            index = j
    return index, best_col


def print_matrix(m: list):
    for row in range(ROWS):
        print(m[row])


def swap_cols(col1, col2, data: list):
    for row in range(COLS):
        data[row][col1], data[row][col2] = data[row][col2], data[row][col1]


ROWS, COLS = get_start_values()
matrix = get_matrix(ROWS)

print('Исходная матрица: ')
print_matrix(matrix)

BEST_COL, AMOUNT = get_best_column(matrix)
print('\nМаксимальное кол-во гласных подряд ({}) находится в столбце #{}'.format(AMOUNT, BEST_COL + 1))
print('Данный столбец: ', end='')
for i in range(ROWS):
    print(matrix[i][BEST_COL], end=' ')

for i in range(BEST_COL, COLS - 1):
    swap_cols(i, i + 1, matrix)

for i in range(ROWS):
    matrix[i] = matrix[i][:-1]

print('\n\nМатрица без искомого столбца: ')
print_matrix(matrix)
