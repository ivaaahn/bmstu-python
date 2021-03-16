# Вычисление значения функции.
# Выполнил: Ивахненко Дмитрий
# Группа: ИУ7-16Б
from math import tan, e, pi, sin

# Ввод данных с клавиатуры
a, b, x = map(float, input('Введите a, b, x: ').split(' '))

# ctg(a*b) > 0 <=> tg(a*b) > 0
if tan(a*b) > 0:
    f = 1/tan(a*b) - e*e
    print('f =', f)

# ctg(a*b) < 0 <=> tg(a*b) < 0
# ctg(a*b) = 0 <=> a*b % 360 = 90 или 270 (+-pi/2 + 2*pi*n, n - целое)
elif tan(a*b) < 0 or a*b % 360 == 90 or a*b % 360 == 270:
    f = (0.93*pi*pi*sin(x))**(-1/5)
    print('f =', f)

# обработка случая, когда котангенс не определен
else:
    print('Котангенс не определен!')
