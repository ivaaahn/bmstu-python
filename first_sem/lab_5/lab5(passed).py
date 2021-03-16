'''
Построение графика звездочками в консоли
Горизонтальная ось - y
Вертикальная ось - x
Обязательно вывести y_min and y_max
Отмечать засечки
Формула для рассчета кол-во пробелов до очередной звездочки:
r = [f(x_cur) - f(min)] / [f(x_max) - f(x_min)]  *   k + 1
k - коэф, который зависит от того, сколько места консоли отдается под график (около 50-70)
Отдельное внимание надо уделить оси икс, которая расположена вертикально
Конкретнее, расположению звездочки и оси
*| |* *
Необходимо учитывать погрешность eps = ratio/2 = (ymax-ymin)/k/2
Звезда попадает на ось не только, когда f(x) = 0, но +-eps
1) *|' (f(x) <= 0 — EPS),
2) '|*' (f(x) >= 0 + EPS),
3) '*' (0 — EPS < y1(x) < 0 + EPS)
Расстояние от начала строки до оси икс по формуле выше при (f(x_cur) = 0)
'''

xFrom, xTo = map(float, input('Введите начальное и конечное значения x: ').split())
while xTo < xFrom:
    xFrom, xTo = map(float, input('Конечное должно быть больше начального!\nПовторите ввод: ').split())
if xFrom == 0:
    xFrom += 0.01

step = float(input('Введите шаг: '))
while step <= 0:
    step = float(input('Шаг должен быть больше нуля!\nПовторите ввод: '))

serif = int(input('Введите количество засечек: '))
while not 4 <= serif <= 8:
    serif = int(input('Введите количество засечек: '))

xMin = xCur = xFrom
yMin = yMax = xFrom * xFrom - 4

negative_value_exists = False
while xCur <= xTo:
    if xCur != 0:
        yCur = xCur * xCur - 4
        if yCur < 0: negative_value_exists = True
        if yCur < yMin:
            yMin = yCur
            xMin = xCur
        if yCur > yMax:
            yMax = yCur
    xCur += step

dial_length = 12  # длина отступа слева

LEN_Y = (yMax - yMin) + (yMax == yMin)  # нахожу разницу между крайними значениями(если оно ноль, то 1)
RATIO = LEN_Y / 80  # масштаб
eps = RATIO / 2  # погрешность
distBetwSerif = int(80 / serif)

pace = yMin
print(' ' * dial_length, end='')
for _ in range(serif):
    print('{1:<{0}.3g}'.format(distBetwSerif, pace), end='')
    pace += LEN_Y / serif

print('')
print(dial_length * ' ' + serif * ('┼' + distBetwSerif * '-') + (82 - distBetwSerif * serif) * '-' + '> y')

AXIS_X_POS = abs(int(-yMin / RATIO))  # где будет ОХ: 300 * ( f(x0) - yMin  /  yMax - yMin )
if (AXIS_X_POS > 80):  # если выходим за границу, то ставим только +1.
    AXIS_X_POS = 81

while xFrom <= xTo:  # стартуем из верхнего икса
    if not (-10 ** (-8) < xFrom < 10 ** (-8)):

        yCur = xFrom * xFrom - 4

        # разница между текущим и минимальным игреком(причем = 0, if yMin!=yMax and yCur=yMin и ==1 if yMin=yMax and yCur=yMin)
        yMin_yCur_dif = (yCur - yMin) + (yCur == yMin) * (yMax == yMin)
        yPos = int(80 * yMin_yCur_dif / LEN_Y)

        print("{1:^{0}.5g}".format(dial_length, xFrom), end='')  # вывод левого столбца.

        if negative_value_exists:
            if yCur <= 0 - eps:
                dist_oX_yPos = AXIS_X_POS - yPos
                if (dist_oX_yPos != 0):  # Если погрешность не помешала
                    print(yPos * ' ' + '*' + (dist_oX_yPos - 1) * ' ' + '|')
                else:
                    print((AXIS_X_POS - 1) * ' ' + '*|')
            elif yCur >= 0 + eps:
                dist_oX_yPos = yPos - AXIS_X_POS
                if (dist_oX_yPos != 0):
                    print(AXIS_X_POS * ' ' + '|' + (dist_oX_yPos - 1) * ' ' + '*')
                else:
                    print(AXIS_X_POS * ' ' + '|*')
            else:
                print(AXIS_X_POS * ' ' + '*')
        else:
            print('|' + yPos * ' ' + '*')
            AXIS_X_POS = 0
    xFrom += step

print((dial_length + AXIS_X_POS) * ' ' + '|\n',
      (dial_length + AXIS_X_POS - 3) * ' ' + 'x V')
