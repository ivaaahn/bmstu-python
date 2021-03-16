# Лабораторная работа номер 8
# Выполнил: Ивахненко Дмитрий
# ИУ7-16Б
# Подсчет интегралов по методам трапеций и 3/8
from math import sin, cos


# исходная функция f(x)
def f(x: float) -> float:
    return sin(x)


# первообразная F(x). (f(x) = F`(x))
def F(x: float) -> float:
    return -cos(x)


# метод трапеций
def trapezoid(a: float, b: float, nseg=1):
    # h - длина каждого из отрезков
    h = (b - a) / nseg

    # ans - искомое значение
    ans = 0.5 * (f(a) + f(b))
    for i in range(1, nseg):
        ans += f(a + i * h)
    ans *= h
    return ans


# метод 3/8
def method3_8(a: float, b: float, nseg=1):
    # h - длина каждого из отрезков
    h = (b - a) / nseg

    # ans - искомое значение
    sum1 = sum2 = 0.0
    for i in range(1, nseg):
        if i % 3 != 0:
            sum1 += f(a + i * h)
        else:
            sum2 += f(a + i * h)

    ans = (3 * h / 8) * (f(a) + f(b) + 3 * sum1 + 2 * sum2)
    return ans


# функция, выводящая  ошибку
def error():
    print('Неверный ввод!')
    return False


# функция, выполняющая проверку на корректность (float)
def checkFloat(x: float) -> bool:
    checkP = checkEps = checkInp = False
    checkInp = True
    if ('0' <= x[0] <= '9') or (len(x) > 1 and x[0] in '-+.' and '0' <= x[1] <= '9'):
        if x[0] == '.': checkP = True
        for j in range(1, len(x)):
            if ('0' <= x[j] <= '9') or (x[j] == '.' and not checkP) or (x[j] == 'e' and len(x) > j + 1 \
                                                                        and not checkEps) or (
                    x[j] in '+-' and x[j - 1] == 'e'):
                if x[j] == '.': checkP = True
                if x[j] == 'e': checkEps = checkP = True
            else:
                checkInp = error()
                break
    else:
        checkInp = error()
    return checkInp


# функция, выполняющая проверку на корректность (натуральные числа)
def checkNatural(x: int) -> bool:
    checkInp = True
    if len(x) > 0:
        for j in range(len(x)):
            if not (('1' <= x[j] <= '9') or (x[j] == '0' and j > 0) or (x[j] == '+' and j == 0 and len(x) > 1)):
                checkInp = error()
                break
    else:
        checkInp = error()
    return checkInp


# Ввод участка [a,b] на котором происходит интегрирование и проверка A <= B
checkAB = False
while not checkAB:
    a = input('Введите a: ').strip()
    while not checkFloat(a):
        a = input('Введите a: ').strip()

    b = input('Введите b: ').strip()
    while not checkFloat(b):
        b = input('Введите b: ').strip()
    checkAB = float(b) >= float(a)
    if float(b) < float(a):
        print('b < a - повторите ввод')

a = float(a)
b = float(b)

# Ввод участка первого и второго количеств разбиений:
first = input('Введите первое количество разбиений: ').strip()
while not checkNatural(first):
    first = input('Введите первое количество разбиений: ').strip()

second = input('Введите второе количество разбиений: ').strip()
while not checkNatural(second):
    second = input('Введите второе количество разбиений: ').strip()

first = int(first)
second = int(second)

# вывожу табличку
print("┌─────────────┬───────────────┬───────────────┐")
print("│ Метод       │{:^15}│{:^15}│".format(first, second))
print("├─────────────┼───────────────┼───────────────┤")
print("│ a) трапеций │{:^15.7}│{:^15.7}│".format(trapezoid(a, b, first), trapezoid(a, b, second)))

if first % 3 != 0 and second % 3 != 0:
    print("│ b) 3/8      │      ---      │       ---      │")
elif first % 3 != 0:
    print("│ b) 3/8      │      ---      │{:^15.7}│".format(method3_8(a, b, second)))
elif second % 3 != 0:
    print("│ b) 3/8      │{:^15.7}│      ---      │".format(method3_8(a, b, first)))
else:
    print("│ b) 3/8      │{:^15.7}│{:^15.7}│".format(method3_8(a, b, first), method3_8(a, b, second)))

print("└─────────────┴───────────────┴───────────────┘")

# Square - эталон, посчитанный через первообразную.
Square = F(b) - F(a)
print('Эталон = ', Square)

eps = input('Введите точность eps: ')
while not checkFloat(eps):
    eps = input('Введите точность eps: ')
eps = float(eps)

# Подсчет с заданной точностью
nseg = second
if abs(trapezoid(a, b, nseg) - Square) > abs(method3_8(a, b, nseg) - Square):
    s_cur = trapezoid(a, b, nseg)
    print('Выполним подсчет с заданной точностью с помощью метода трапеций')
    while abs(trapezoid(a, b, nseg) - trapezoid(a, b, 2 * nseg)) > eps:
        s_cur = trapezoid(a, b, 2 * nseg)
else:
    s_cur = method3_8(a, b, nseg)
    print('Выполним подсчет с заданной точностью с помощью метода 3/8')
    while abs(method3_8(a, b, nseg) - method3_8(a, b, 2 * nseg)) > eps:
        s_cur = method3_8(a, b, 2 * nseg)

print('Интеграл, высчитанный с заданной точностью: {}'.format(s_cur))
print('Для подсчета интеграла с заданной точностью eps'
      ' = {} понадобилось {} разбиений: '.format(eps, nseg))
