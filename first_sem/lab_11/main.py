from math import sin, cos
from sys import exit

# Основная функция f(x)
def f(x: float):
    try:
        return sin(x)
    except ZeroDivisionError:
        print('Некорректная функция')
        exit(0)


def df(x: float):
    return cos(x)


# Функция, уточняющая корень методом секущих
def secants(x0: float, x1: float, eps: float):
    num_of_iter = 0

    while not (abs(x1 - x0) < eps):
        x1, x0 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)), x1
        num_of_iter += 1

    return x1, num_of_iter


# Проверка на корректность ввода типа float
def check_float(a: str) -> bool:
    try:
        float(a)
        return True
    except:
        return False


# Проверка на ошибку(выход за интервал)
def check_error(a: float, b: float, x: float) -> bool:
    return a < x < b


# Функция, проверяющая существование корня на отрезке
def root_exist(left: float, right: float):
    return f(left) * f(right) <= 0  # одинаковые знаки


# Функция ввода начальных значений
def input_start_values():
    a = input('Введите левую границу. x = ').strip()
    while not check_float(a):
        print('Неверный ввод')
        a = input('Введите левую границу. x = ').strip()

    b = input('Введите правую границу. x = ').strip()
    while check_float(b) == False or float(b) < float(a):
        print('Неверный ввод')
        b = input('Введите правую границу. x = ').strip()

    h = input('Введите шаг h: ').strip()
    while not check_float(h):
        print('Неверный ввод')
        h = input('Введите шаг h: ').strip()

    eps = input('Задайте точность: ').strip()
    while not check_float(eps):
        print('Неверный ввод')
        eps = input('Задайте точность: ').strip()

    return float(a), float(b), float(h), float(eps)


# Печать верхней части таблицы
def print_header():
    print("┌───────────┬────────────────┬──────────────────┬──────────────────┬───────────────┬─────────────────┐")
    print('│ № отрезка │Границы отрезка │  Значение корня  │ Значение функции │Кол-во итераций│      Ошибки     │')


# Печать основной части таблицы
def print_roots(num: int, left: float, right: float, x: float, num_of_iter, error: str):
    print("├───────────┼────────────────┼──────────────────┼──────────────────┼───────────────┤─────────────────┤")
    print('│{:^11}│{:>7.3g}; {:<7.3g}│{:^18.6}│{:^18.0e}│{:^15}│{:^17}│'.format(num, left, right, x, f(x), num_of_iter,
                                                                                error))


# Печать нижней части таблицы
def print_footer():
    print('└───────────┴────────────────┴──────────────────┴──────────────────┴───────────────┴─────────────────┘')


def start():
    a, b, h, eps = input_start_values()
    cur_start = a
    interval_num = 0
    print_header()
    while cur_start < b:
        cur_end = (cur_start + h >= b) * b + (cur_start + h < b) * (cur_start + h)

        if interval_num == 0 and f(cur_start) == 0:
            cur_x = cur_start
            num_of_iter = 0

            print_roots(interval_num + 1, cur_start, cur_end, cur_x, num_of_iter, 'Корень на границе')
            cur_start += h
            interval_num += 1

        if root_exist(cur_start, cur_end) and f(cur_end) == 0:
            cur_x = cur_end
            num_of_iter = 0

            print_roots(interval_num + 1, cur_start, cur_end, cur_x, num_of_iter, 'Корень на границе')
            cur_start += 2 * h
            interval_num += 1

        elif root_exist(cur_start, cur_end):
            cur_x, num_of_iter = secants(cur_start, cur_end, eps)

            error = 'Ошибок нет'
            print_roots(interval_num + 1, cur_start, cur_end, cur_x, num_of_iter, error)
            cur_start += h
            interval_num += 1

        else:
            cur_start += h

    print_footer()


start()
