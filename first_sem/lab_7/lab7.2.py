# Лабораторная работа номер 7. Задчание 2.
# Выполнил: Ивахненко Дмитрий
# ИУ7-16Б
# Построение матрицы на основе заданного массива и счетчика

from math import sin, sqrt
def error():
    print('Неверный ввод!')
    return False

# Проверка корректности натуральных чисел + на принадлженость числа заданному отрезку
def checkNatural(x: int, upLimit: int) -> bool:
    checkInp = True
    if len(x) > 0:
        for j in range(len(x)):
            if not (('1' <= x[j] <= '9') or (x[j] == '0' and j > 0) or (x[j] == '+' and j == 0 and len(x) > 1)):
                checkInp = error()
                break
    else:
        checkInp = error()
    # Проверка на принадлежность заданному в условии отрезку
    if checkInp and int(x) > upLimit:
        checkInp = False
        print('Значение должно быть <= {}'.format(upLimit))
    return checkInp

# Проверка корректности вещественных чисел чисел
def checkFloat(x: float) -> bool:
    checkP = checkEps = checkInp = False
    checkInp = True
    if ('0' <= x[0] <= '9') or (len(x) > 1 and x[0] in '-+.' and '0' <= x[1] <= '9'):
        if x[0] == '.': checkP = True
        for j in range(1, len(x)):
            if ('0' <= x[j] <= '9') or (x[j] == '.' and not checkP) or (x[j] == 'e' and len(x) > j + 1 \
                and not checkEps) or (x[j] in '+-' and x[j - 1] == 'e'):
                if x[j] == '.': checkP = True
                if x[j] == 'e': checkEps = checkP = True
            else:
                checkInp = error()
                break
    else:
        checkInp = error()
    return checkInp

# Ввод K (кол-во строк в искомой матрице)
K = input('Введите K(длину массива f): ').strip()
while not checkNatural(K, 14):
    K = input('Введите K(длину массива f): ').strip()
K = int(K)

# Ввод I (кол-во столбцов в искомой матрице)
I= input('Введите I(кол-во итераций х): ').strip()
while not checkNatural(I, 20):
    I= input('Введите I(кол-во итераций х): ').strip()
I= int(I)

# Инициализация массива f[]. Реализация ввода ее пользователем
print('Ввод массива f: ')
f = []
for q in range(K):
    x = input('Введите {} элемент: '.format(q + 1)).strip()
    while not checkFloat(x):
        x = input('Введите {} элемент: '.format(q + 1)).strip()
    f.append(float(x))

# Объявление искомой матрицы z[], ее запонение, поиск мин и макс
z=[[0 for __ in range(I)] for _ in range(K)]
x = 1
maxEl = minEl = z[0][0]
minHere = maxHere = 0
for k in range(K):
    for i in range(I):
        z[k][i] = sin(f[k]) + sqrt(x)

        # Поиск мин и макс
        if z[k][i] > maxEl:
            maxEl = z[k][i]
            maxHere = i
        if z[k][i] < minEl:
            minEl = z[k][i]
            minHere = i
        x += 0.1
print('\nF: ', f, end='\n\n')

# Вывод матрицы z[]
for i in range(K):
    for j in range(I):
        print('{:^10.5}'.format(z[i][j]),end=' ')
    print('')

# Объявление и заполнение вектора Y[]
Y = []
for k in range(K):
    Y.append(z[k][minHere])
for k in range(K):
    Y.append(z[k][maxHere])

# Вывод вектора z[]
print('\nY:',end=' ')
for q in range(len(Y)):
    print('{:.5}'.format(Y[q]),end=' ')

