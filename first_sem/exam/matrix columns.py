# Задача у меня была: в матрице отсортировать столбцы по среднему арифм положительных
# элементов, новые массивы использовать нельзя. И потом еще посчитать где больше чисел кратных 5-
# в нижнетреугольной или в верхнетреугольной


def swap_cols(rows, col1, col2, data: list):
    for row in range(rows):
        data[row][col1], data[row][col2] = data[row][col2], data[row][col1]


def search(rows, column, data: list):
    ans = 0
    for row in range(rows):
        ans += data[row][column]
    return ans / rows


def five(rows, a):
    cols = rows
    top = 0
    bottom = 0
    for i in range(rows):
        for j in range(i + 1, cols):
            if a[i][j] % 5 == 0:
                top += 1

    for i in range(rows):
        for j in range(0, i):
            if a[i][j] % 5 == 0:
                bottom += 1
    if top > bottom:
        print('\nЧисел кратных пяти больше в верхнетреугольной({}), чем в нижнетреугольной({}).'.format(top, bottom))
    elif top < bottom:
        print(
            '\nЧисел кратных пяти больше в ниженетреугольной({}), чем в верхнетреугольной({}).'.format(bottom, bottom))
    else:
        print('\nКоличество чисел кратных пяти в верхнетреугольной и в нижнетреугольной совпадает ({}).'.format(top))


SIZE = int(input('Введите размерность матрицы: '))
matrix = []
for i in range(SIZE):
    matrix.append(list(map(int, input('Введите строку №{}: '.format(i + 1)).split())))

print('\n\nНачальная матрица: ')
for i in range(SIZE):
    print(matrix[i])

print('Средние арифметическое каждого столбца: ')
for col in range(SIZE):
    s = search(SIZE, col, matrix)
    print('#{:d}: {:.3f}'.format(col + 1, s))

swapped = True
while swapped:
    swapped = False
    for i in range(SIZE - 1):
        for j in range(SIZE - 1 - i):
            if search(SIZE, j, matrix) > search(SIZE, j + 1, matrix):
                swap_cols(SIZE, j, j + 1, matrix)
                swapped = True

print('\n\nМатрица после сортировки: ')
for i in range(SIZE):
    print(matrix[i])

print('Средние арифметическое каждого столбца после сортировки: ')
for col in range(SIZE):
    s = search(SIZE, col, matrix)
    print('#{:d}: {:.5f}'.format(col + 1, s))

five(SIZE, matrix)