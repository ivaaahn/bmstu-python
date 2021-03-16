def shaker_with_flag(arr):
    swapped = True
    r = len(arr) - 1
    l = 0
    while swapped:
        swapped = False
        for i in range(l, r):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        r -= 1

        for i in range(r, l, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        l += 1


def shell_sort(a: list):
    dist = len(a) // 2
    while dist:
        for index, el in enumerate(a):
            while index - dist >= 0 and a[index - dist] > el:
                a[index] = a[index - dist]
                index -= dist
            a[index] = el
        dist = 1 if dist == 2 else int(dist * 5.0 / 11)


x, eps = map(float, (input('Через пробел введите x, eps: ')).split(' '))

s = 0.0
n = 2
nextEl = x

while abs(nextEl) >= eps:
    s += nextEl
    nextEl *= -  x * x * (n - 1) / (n * (n + 1) * (n + 1))
    n += 2

print('S = {:.5}'.format(s))

arr = [float(i) for i in input('Введите числа: ').split()]
print(arr)
shell_sort(arr)

index = 0
for i in range(len(arr)):
    if arr[i] > s:
        index = i
        break

arr = arr[:index]
print(arr)
