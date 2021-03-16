def f(x: float) -> float:
    return x*x*x

def F(x: float) -> float:
    return x*x*x*x/4

def right(a, b, nseg):
    h = (b - a) / nseg
    ans = f(b)
    for i in range(1, nseg):
        ans += f(a + i * h)
    ans *= h
    return ans


a = float(input('Введите a: '))
b = float(input('Введите b: '))
N = int(input('Введите число разбиений N: '))

answer = right(a, b, N)
print('Интеграл равен: {}'.format(answer))