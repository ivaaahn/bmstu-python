def bubble_sort_flag(l: list):
    swapped = True
    while swapped:
        swapped = False
        for n in range(len(l) - 1):
            if l[n] > l[n + 1]:
                l[n], l[n + 1] = l[n + 1], l[n]
                swapped = True


def bubble_sort(l: list):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def bubble_sort_start(l: list):
    for i in range(len(l) - 1):
        for j in range(len(l) - 2, i - 1, -1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def bubble_sort_end(l: list):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def selection_sort(data: list):
    for i in range(len(data) - 1):
        index_min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[index_min]:
                index_min = j
        data[i], data[index_min] = data[index_min], data[i]


def simple_insertion(data: list):
    for i, temp in enumerate(data):
        while i - 1 >= 0 and data[i - 1] > temp:
            data[i] = data[i - 1]
            i -= 1
        data[i] = temp


def shellSort(data: list):
    dist = len(data) // 2
    while dist:
        for i, temp in enumerate(data):
            while i - dist >= 0 and data[i - dist] > temp:
                data[i] = data[i - dist]
                i -= dist
            data[i] = temp
        dist = 1 if dist == 2 else int(dist * 5.0 / 11)


def bin_insertion(data):
    for i, temp in enumerate(data):
        left, right = 0, i
        while right > left:
            mid = left + (right - left) // 2
            if data[mid] <= temp:
                left = mid + 1
            else:
                right = mid
        for j in range(i, right, -1):
            data[j] = data[j - 1]
        data[right] = temp


from random import randint


def quicksort(a, left, right):
    if left >= right: return

    i, j = left, right
    x = a[randint(left, right)]

    while i <= j:  # пока левая часть левее правой
        # скипаем элементы, которые уже норм стоят
        while a[i] < x: i += 1
        while a[j] > x: j -= 1
        # если еще остались элементы
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i, j = i + 1, j - 1
    quicksort(a, left, j)
    quicksort(a, i, right)


def bubble_gum(a):
    left = 0
    right = len(a) - 1

    while left < right:
        for i in range(left, right, 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1

        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
        left += 1


myList = [randint(0, 7) for i in range(15)]
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []

for i in range(len(myList)):
    a.append(myList[i])
    b.append(myList[i])
    c.append(myList[i])
    d.append(myList[i])
    e.append(myList[i])
    f.append(myList[i])
    g.append(myList[i])
    h.append(myList[i])

print(myList)

bubble_sort_start(a)
bubble_sort(b)
bubble_sort_end(c)
bubble_sort_flag(d)
selection_sort(e)
simple_insertion(f)
bubble_gum(g)
quicksort(h, 0, len(h) - 1)
# bin_insertion(myList)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


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


shaker_with_flag(myList)
print(myList)
