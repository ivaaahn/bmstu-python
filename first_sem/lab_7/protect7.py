# Есть матрица 5*5 диаг =1
# вводися число, если оно мнеьше нуля то заполняется левый , а иначе - правый
# Найти среднее арифметическое всех ненуевых элементов матрицы и поделиить каждый элмент на среднее арфметичаеское

SIZE = 5
a = [[0,0,0,0,0] for _ in range(SIZE)]

for i in range(SIZE):
    a[i][i] = 1

print('\n')

for i in range(len(a)):
    print(a[i])


x = float(input('Введите число: '))
if x < 0:
    for i in range(SIZE):
        j=0
        while(i > j):
            a[i][j] = x
            j+=1
else:
    for i in range(SIZE):
        j=i+1
        while(j < SIZE):
            a[i][j] = x
            j+=1



print('\n')


arifm = (5+10*x)/15
print('\nАРИФМ', arifm)
for i in range(len(a)):
    print(a[i])

for i in range(SIZE):
    for j in range(SIZE):
        a[i][j] = a[i][j]/arifm


for i in range(len(a)):
    print(a[i])