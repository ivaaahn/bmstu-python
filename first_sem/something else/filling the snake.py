ROWS = 5

a = list()

for i in range(ROWS):
    temp = list(map(int, input('Введите строку {}: '.format(i + 1)).split()))
    if i % 2 == 0:
        temp.reverse()
    a.append(temp)

for i in range(ROWS):
    print(*a[i])
