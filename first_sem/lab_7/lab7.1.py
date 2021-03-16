# Лабораторная работа номер 7. Задчание 1.
# Выполнил: Ивахненко Дмитрий
# ИУ7-16Б
# Поворот квадратной матрицы, заданной с клавиатуры, по часовой и против часовой на 90 градусов
def rightMatrix(a: list):
    SIZE = len(a)
    if SIZE % 2 == 0:
        numOfCircle = int(SIZE / 2)  # определить кол-во кругов
    else:
        numOfCircle = int((SIZE + 1) / 2)
    tempSize = SIZE # размер матрицы на текущем круге
    F = 0 # index of First element
    L = SIZE - 1 # index of Last element
    for _ in range(numOfCircle):
        for i in range(tempSize - 1):
            a[F][F + i], a[F + i][L], a[L][L - i], a[L - i][F] = \
                a[L - i][F], a[F][F + i], a[F + i][L], a[L][L - i]
        tempSize -= 2 #На каждом кргуе откидывает крайние столбцы
        # Последний элемент уменьшаем, а первый увеличиваем
        L -= 1
        F += 1

N = 0 # Размер матрицы
check_correct = False # Флаг корректности ввода
value = ""
while not check_correct:
    check_correct = True
    value = input("Введите размер квадратной матрицы (1 <= size <= 9): ")

    if len(value) != 0: # подготовка числа
        num = value
        if num[0] in "-+": num = num[1:]
        check_correct = num.isdigit() # проверяю на принадлежность только цифрам
    else:
        check_correct = False

    if check_correct and (int(value) < 1 or int(value) > 9):
        check_correct = False
        print(end="Размер матрицы указан неверно! ")

    if not check_correct: # вывод ошибки
        print("Некорректный ввод")

# Исходная матрица и ее размер:
N = int(value)
matrix = []

for i in range(1, N + 1):
    check_correct = False
    values = ""

    while not check_correct:
        check_correct = True
        values = input("Введите строку №{:d}: ".format(i)).split()

        for value in values:
            if len(value) != 0:
                mantiss, exp = "0", "0" # определяю мантиссу и экпоненту
                value_splited = value.split("e") # делим строку на мантиссу и экспоненту
                # проверка на валидность
                if len(value_splited) == 2:  # Если есть и мантиссса, и экспонента
                    mantiss, exp = value_splited # число вида 1e4
                elif len(value_splited) == 1:  # Только мантисса
                    mantiss = value_splited[0] # число вида 10000
                else:
                    check_correct = False # неправильный формат

                if len(mantiss) != 0 and len(exp) != 0:
                    if mantiss[0] in "-+": # откидываю первый плюс и минус
                        mantiss = mantiss[1:]
                    if exp[0] in "-+": # откидываю первый плюс и минус
                        exp = exp[1:]
                    # проверяю на принадлежность только цифрам
                    check_correct = check_correct and mantiss.replace('.', '', 1).isdigit() and exp.isdigit()
                else:
                    check_correct = False
            else:
                check_correct = False
        # если введено неправильное количество элементов
        if len(values) != N:
            check_correct = False
            print(end="Введено неправильное количество элементов. Введите {:d}. ".format(N))
        # вывод ошибки
        if not check_correct:
            print("Некорректный ввод")
    matrix.append(list(map(float, values)))

print('\nНачальная матрица: ')
for i in range(len(matrix)):
    print(matrix[i])

rightMatrix(matrix)
print('\n Матрица после поворота на 90 градусов ПО часовой стрелке: ')
for i in range(len(matrix)):
    print(matrix[i])

rightMatrix(matrix)
rightMatrix(matrix)
print('\n Матрица после поворота на 90 градусов ПРОТИВ часовой стрелки: ')
for i in range(len(matrix)):
    print(matrix[i])