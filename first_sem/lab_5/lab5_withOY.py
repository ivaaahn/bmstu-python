from math import sin
def f(x: float) -> float:
    return  x*x

# Ввод начального и конечного значений. Проверка на валидность:
xFrom, xTo = map(float, input('Введите начальное и конечное значения x: ').split())
while xTo < xFrom:
    xFrom, xTo = map(float, input('Конечное должно быть больше начального!\nПовторите ввод: ').split())

# Ввод шага изменений x и проверка, что он положительный
step = float(input('Введите шаг: '))
while step <= 0:
    step = float(input('Шаг должен быть больше нуля!\nПовторите ввод: '))

# Ввод кол-ва засечек и проверка, что он положительный
serif = int(input('Введите количество засечек: '))
while not 4 <= serif <= 8:
    serif = int(input('Введите количество засечек: '))

# инициализация начального минимума, значения, при котором он достигается
xMin = xCur = xFrom
yMin = yMax = f(xFrom)

# Вывод верхней границы таблицы
print("┌" + "─"*12 + "┬" + "─"*12 +  "┐")
print("│     b      │     r      │")

negative_value_exists = False # отметим, существуют ли отрицательные значения функции или нет

# Основная часть программы - подсчет y и составление таблички
while xCur <= xTo:
    print("├" + "─" * 12 + "┼" + "─" * 12 + "┤")
    yCur = f(xCur)
    if yCur < 0: negative_value_exists = True
    print("│{:^12.5}│{:^12.5}│".format(xCur, yCur))
    if yCur < yMin:
        yMin = yCur
        xMin = xCur
    if yCur > yMax:
        yMax = yCur
    xCur+=step

# Вывожу нижнюю границу таблицы
print("└" + "─"*12 + "┴" + "─"*12 + "┘")

print('\nМинимум функции y = {:.5}'.format(yMin))
print('Минимум достигается при x = {:.5}'.format(xMin))

dial_length = 12 # длина отступа слева
label = "График функции y = x^9 + 34x^8 - 2x^7 + 24x^6 - 76x^5 + 33x^4 - x^3 + 3x^2 + 7x - 33"
print(dial_length * ' ' + label)


LEN_Y = (yMax - yMin) + (yMax == yMin) # нахожу разницу между крайними значениями(если оно ноль, то 1)
RATIO = LEN_Y / 80 # масштаб
eps = RATIO/2 # погрешность
distBetwSerif = int(80/serif)

pace = yMin
print(' '*dial_length, end='')
for _ in range(serif):
    print('{1:<{0}.4g}'.format(distBetwSerif, pace), end='')
    pace+=LEN_Y/serif

print('')
print(dial_length*' ' + serif*('|'+ distBetwSerif*' ') + (82-distBetwSerif*serif)*' ')

AXIS_X_POS = abs(int(-yMin/RATIO)) # где будет ОХ: 300 * ( f(x0) - yMin  /  yMax - yMin )
if (AXIS_X_POS > 80): #если выходим за границу, то ставим только +1.
    AXIS_X_POS = 81

while xFrom <= xTo: # стартуем из верхнего икса
    yCur = f(xFrom)

    # разница между текущим и минимальным игреком(причем = 0, if yMin!=yMax and yCur=yMin и ==1 if yMin=yMax and yCur=yMin)
    yMin_yCur_dif = (yCur - yMin) + (yCur == yMin) * (yMax == yMin)
    yPos = int(80 * yMin_yCur_dif/LEN_Y)



    if -10**(-8) < xFrom < 10**(-8):
        xFrom = 0.0

    print("{1:^{0}.5g}".format(dial_length, xFrom), end='') #вывод левого столбца.

    if -10**(-8) < xFrom < 10**(-8):
        if negative_value_exists:
            if yCur <= 0 - eps:
                dist_oX_yPos = AXIS_X_POS - yPos
                if (dist_oX_yPos != 0):  # Если погрешность не помешала
                    print(yPos * '─' + '*' + (dist_oX_yPos - 1) * '─' + '|' + (82-yPos-dist_oX_yPos)*'─' + '> y')
                else:
                    print((AXIS_X_POS - 1) * '─' + '*|' + (81-AXIS_X_POS)*'─' + '> y')
            elif yCur >= 0 + eps:
                dist_oX_yPos = yPos - AXIS_X_POS
                if (dist_oX_yPos != 0):
                    print(AXIS_X_POS * '─' + '|' + (dist_oX_yPos - 1) * '─' + '*' + (81 - AXIS_X_POS - dist_oX_yPos)*'─' + '> y' )
                else:
                    print(AXIS_X_POS * '─' + '|*' + (80 - AXIS_X_POS)*'─' + '> y')
            else:
                print(AXIS_X_POS * '─' + '*' + (81-AXIS_X_POS)*'─' + '> y')
        else:
            print('|' + (yPos)*'─' + '*' + (81-yPos)*'-' + '> y')
            AXIS_X_POS = 0
        xFrom += step

    else:
        if negative_value_exists:
            if yCur <= 0 - eps:
                dist_oX_yPos = AXIS_X_POS - yPos
                if (dist_oX_yPos != 0): #Если погрешность не помешала
                    print(yPos*' ' + '*' + (dist_oX_yPos-1)*' ' + '|')
                else:
                    print((AXIS_X_POS-1)*' ' + '*|')
            elif yCur >= 0 + eps:
                dist_oX_yPos = yPos - AXIS_X_POS
                if (dist_oX_yPos != 0):
                    print(AXIS_X_POS * ' ' + '|' + (dist_oX_yPos - 1) * ' ' + '*')
                else:
                    print(AXIS_X_POS*' ' + '|*')
            else:
                print(AXIS_X_POS*' ' + '*')
        else:
            print('|' + yPos*' ' + '*')
            AXIS_X_POS = 0

        if xFrom < 0 and xFrom + step > 10**(-8):
            print(dial_length*' ' + 82 * '─' + '> y')
        xFrom += step

print((dial_length + AXIS_X_POS) * ' ' + '|\n',
      (dial_length + AXIS_X_POS - 3) * ' ' + 'x V')