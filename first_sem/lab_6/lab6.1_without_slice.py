# Лабортаорная работа номер 6. Задача 1.1.
#Выполнил Ивахненко Дмитрий ИУ7-16Б

#Проверка на корректность введенных данных для последовательности:
checkInp = False
while (not checkInp):
    checkInp = True

    # Ввод элементов последовательности с клавиатуры
    a = list(input('Введите элементы массива через пробел: ').strip().split(' '))
    if a[0] != '':
        for el in a:

            if (not checkInp):
                break

            # Флаг для точки и е
            checkP = False
            checkEps = False

            #Отдельно проверем первый символ элемента:
            if ('0' <= el[0] <= '9') or (len(el) > 1 and el[0] in '-+.' and '0' <= el[1] <= '9'):

                if el[0] == '.':
                    checkP = True
                #Проверка остальных символов
                for j in range(1, len(el)):
                    if ('0' <= el[j] <= '9') or (el[j] == '.' and not checkP) or (el[j] == 'e' and \
                    len(el) > j + 1 and not checkEps) or (el[j] in '+-' and el[j - 1] == 'e'):

                        if el[j] == '.':
                            checkP = True

                        if el[j] == 'e':
                            checkEps = True
                            checkP = True

                        continue
                    else:
                        print('Неверный ввод!')
                        checkInp = False
                        break
            else:
                print('Неверный ввод!')
                checkInp = False
    else:
        print('Неверный ввод!')
        checkInp = False

#Преобразование верно заполненного массива в float
for j in range(len(a)):
    a[j] = float(a[j])


#Проверка на корректность введенных данных для числа:
checkP = False
checkEps = False
chechInp = False

while (not chechInp):

    #Ввод числа с клавиатуры
    x = input('Введите действительное число: ')

    #флаг непосредственно для проверки верности ввода
    chechInp = True

    # Отдельно проверем первый символ числа:
    if ('0' <= x[0] <= '9') or (len(x) > 1 and x[0] in '-+.' and '0' <= x[1] <= '9'):

        if x[0] == '.':
            checkP = True

        #Проверка остальных сиволов числа
        for j in range(1, len(x)):
            if ('0' <= x[j] <= '9') or (x[j] == '.' and not checkP) or (x[j]=='e' and len(x) > j+1 and not checkEps)\
                    or (x[j] in '+-' and x[j-1] == 'e'):
                if x[j] == '.':
                    checkP = True
                if x[j] == 'e':
                    checkEps = True
                    checkP = True
            else:
                print('Неверный ввод!')
                chechInp = False
                break
    else:
        print('Неверный ввод!')
        chechInp = False
x = float(x)

#Вывод введенной последовательности и числа для наглядности:
print('Начальный массив: {}'.format(a))
print('Число: {}'.format(x))

#Поиск максимума, для определения индекса нового элемента
maxEl = a[0]
for i in range(len(a)):
    if a[i] >= maxEl:
        maxEl = a[i] #max el
        index = i # index of last max el

#Если последний максимум - это последний элемент последовательности
if index == len(a) - 1:
    a.append(x)

#Если не последний
else:
    #Сдвигаем все элементы, начиная с следующего после максимума на 1 вправо
    a.append(a[len(a) - 1])
    for i in range(len(a) - 1, index + 1, -1):
        a[i] = a[i - 1]

    #Вставляем x после максимума
    a[index + 1] = x

    print('Итоговый массив: {}'.format(a))






