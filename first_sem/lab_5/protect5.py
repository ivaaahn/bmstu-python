x, eps = map(float, (input('Через пробел введите x, eps: ')).split(' '))

# S = 0.0
# n = 1
# elNext = x
# k = n + 1
#
# while abs(elNext) > eps:
#     S += elNext
#     n += 1
#     elNext = -elNext * x * x / k / (k + 1)
#     k = k + 2

s = 0.0
n = 2
nextEl = x

while abs(nextEl) >= eps:
    s += nextEl
    nextEl *= -  x * x * (n-1) / (n * (n + 1) * (n + 1))
    n += 2

print('S = {:.5}'.format(s))
