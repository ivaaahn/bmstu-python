# Лабораторная работа №3
# Выполнил: Ивахненко Дмитрий
# Группа: ИУ7 - 16Б

# Обозначения:
# xA, yA - координаты точки А
# xB, yB - координаты точки B
# xC, yC - координаты точки C
# xM, yM - координаты точки M
# lenAB - длина стороны AB
# lenBC - длина стороны BC
# lenAC - длина стороны AC
# lenAM - длина стороны AM
# lenBM - длина стороны BM
# lenCM - длина стороны CM
# lenMax - длина максимальной стороны в треугольнике ABC
# lenMin - длина минимальной стороны в треугольнике ABC
# lenMid - длина средней по длине стороны в треугольнике ABC
# PMain - периметр ABC
# pMain - полупериметр ABC
# SMain - площадь ABC
# median - медиана в треугольнике ABC, проведенная из большего угла
# pABM - полупериметр треугольника ABM
# pBCM - полупериметр треугольника BCM
# pACM - полупериметр треугольника ACM
# S_ABM - площадь треугольника ABM
# S_BCM - площадь треугольника BСM
# S_ACM - площадь треугольника AСM
# eps - погрешность для сравнения типа float
# hAB - расстояние от точки M до прямой, содержащей сторону AB треугольника ABC
# hBC - расстояние от точки M до прямой, содержащей сторону BC треугольника ABC
# hAC - расстояние от точки M до прямой, содержащей сторону AC треугольника ABC
# hMax - расстояние от точки M до прямой, содержащей наиболее удаленную сторону треугольника ABC
# typeOfTriangle - значение выражения, определяющего тип треугольника ABC
from math import sqrt, hypot

# Чтобы сравнить переменные типа float введем eps = 10^-6 - погрешность
epsTR = 10 ** (-10)
epsMain = 10**(-8)

# Проверка того, что три точки, введнные пользователем не лежат на одной прямой
# Ввод данных пользователем
xA, yA = map(int, input('Введите координаты (x,y) точки A треугольника ABC: ').split(','))
xB, yB = map(int, input('Введите координаты (x,y) точки B треугольника ABC: ').split(','))
xC, yC = map(int, input('Введите координаты (x,y) точки C треугольника ABC: ').split(','))

# Считаем длины сторон заданного треугольника
lenAB = hypot(xB - xA, yB - yA)
lenBC = hypot(xC - xB, yC - yB)
lenAC = hypot(xC - xA, yC - yA)

# Три точки образуют треугольник, если выполнены три следующих равнества
if abs(lenBC + lenAB - lenAC) < epsMain or abs(lenBC + lenAC - lenAB) < epsMain or abs(lenAC + lenAB - lenBC) < epsMain:
    print('Данные три точки не могут задавать треугольник, так как лежат на одной прямой!')
else:
    # Вывод длин сторон заданного треугольника
    print('\nДлина стороны AB = {:.5}\n'
          'Длина стороны BC = {:.5}\n'
          'Длина стороны AC = {:.5}\n'.format(lenAB, lenBC, lenAC))

    # Определяем большую и среднюю стороны
    lenMax = max(lenAB, lenAC, lenBC)
    lenMin = min(lenAB, lenAC, lenBC)

    # Определяем среднюю сторону, вычитая из периметра
    # трегольника длины максимальной и минимальной сторон
    PMain = lenAB + lenAC + lenBC
    lenMid = PMain - (lenMax + lenMin)

    # Определяем длину медианы, проведенную из большего угла и выводим ее
    # (прим.: больший угол треугольника лежит против большей стороны)
    median = 0.5 * sqrt(2*(lenMin * lenMin + lenMid * lenMid) - lenMax*lenMax)
    print('Длина медианы, проведенной из вершины большего угла = {:.5}\n'.format(median))

    # Ввод произвольной точки M и определение, принадлежности точки M треугольнику ABC
    xM, yM = map(int, input('Введите координаты (x,y) произвольной точки M: ').split(','))

    # Находим длины AM, BM, CM
    lenAM = hypot(xM - xA, yM - yA)
    lenBM = hypot(xM - xB, yM - yB)
    lenCM = hypot(xM - xC, yM - yC)

    # Находим площадь основного трегольника
    pMain = PMain/2
    SMain = sqrt(pMain * (pMain-lenAC) * (pMain-lenBC) * (pMain-lenAB))

    # Находим полумериметры треугольников с вершиной в точке M и основаниями AB, BC, AC
    pABM = 0.5*(lenAB + lenAM + lenBM)
    pBCM = 0.5*(lenBC + lenBM + lenCM)
    pACM = 0.5*(lenAC + lenAM + lenCM)

    # Находим площадь треугольников с вершиной в точке M и основаниями AB, BC, AC
    S_ABM = sqrt(pABM * (pABM - lenAB) * (pABM - lenAM) * (pABM - lenBM))
    S_BCM = sqrt(pBCM * (pBCM - lenBC) * (pBCM - lenBM) * (pBCM - lenCM))
    S_ACM = sqrt(pACM * (pACM - lenAC) * (pACM - lenAM) * (pACM - lenCM))

    # Если сумма данных площадей == площади исходного треугольника, точка М лежит внутри ABC
    if abs(SMain - (S_ABM + S_ACM + S_BCM)) <= epsTR:
        print('Точка M принадлежит треугольнику ABC\n')
        # Найдем расстояние от точки М до дальней стороны треугольника
        hAB = (2 * S_ABM) / lenAB
        hBC = (2 * S_BCM) / lenBC
        hAC = (2 * S_ACM) / lenAC
        hMax = max(hAB, hAC, hBC)

        print('Расстояние от точки М до наиболее удаленной стороны треугольника - {:.5}'.format(hMax))

    else:
        print('Точка M не принадлежит треугольнику ABC\n')

    # Определим, является ли треугольник остроугольным
    # Для этого проверим знак выражения lenMin^2 + lenMid^2 - lenMax^2
    # Если выражение равно нулю, то треугольник прямоугольный
    # Если выражение меньше нуля, то треугольник тупоугольный
    # Если выражение больше нуля, то больший угол треугольника остроугольный =>
    # => треугольник остроугольный

    typeOfTriangle = lenMin * lenMin + lenMid * lenMid - lenMax * lenMax
    if abs(typeOfTriangle) < epsTR:
        print('Треугольник ABC прямоугольный!')
    elif typeOfTriangle - epsTR > 0:
        print('Треугольник ABC является остроугольным!')
    else:
        print('Треугольник ABC тупоугольный!')



