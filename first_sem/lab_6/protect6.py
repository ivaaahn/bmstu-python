a = list(map(int,input('Введите элементы массива через пробел: ').strip().split(' ')))
print('Начальный массив: {}'.format(a))
b = []
for i in range(len(a)):
    if a[i]%7!=0:
        b.append(a[i])
if len(b) == 0:
    print('Были вычеркнуты все элементы!')
else:
    print('Массив полсле вычеркивания: {}'.format(b))
