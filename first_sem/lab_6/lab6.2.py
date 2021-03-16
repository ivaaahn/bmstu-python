# cur_arr and new_arr - текущая выстраиваемая последовательность
# final_arr and max_final_arr - текущая составленная последовательность и максимальная составленная
def f(s: list):
    return _f_(0, [1], 0, s)[1:]

def _f_(start_index, cur_arr: list, max_length: int, chain: list) -> list:

    # Если последний элемент у рассматриваемой последовательности равен нулю, то сделать ее длиннее невозможно
    if cur_arr[-1] == 0:
        return cur_arr

    #максиамльной окончательной версии временно присваиваем текущую
    max_final_arr = cur_arr

    # Прохожу по исходному массиву chain, начиная с start_index, имитируя срез
    for i in range(start_index, len(chain)):
        # Если элемент исходного массива делится на последний эл. текущей послед.
        if chain[i] % cur_arr[-1] == 0:

            # Если макс. допустимая длина текущей ветки меньше максимальной зафиксированной длины, выходим из цикла
            # так как дальше длина будет только уменьшаться
            # +1 из-за того, что дальше мы гарантированно добавим один эл, -(i+1) из-за того, что нумерация с нуля
            if len(cur_arr)+1 + (len(chain) - (i+1)) < max_length:
                break

            # обновляем текущую выстраиваемую последовательность
            new_arr = list(cur_arr)
            new_arr.append(chain[i])

            final_arr = _f_(i + 1, new_arr, max_length, chain)

            # после выхода из шага рекурсии проводим обновление max_length and max_final_arr
            if len(final_arr) > max_length:
                max_final_arr = final_arr
                max_length = len(final_arr)

    # Искомая последовательность max_final_arr
    return max_final_arr

def checkE(el: str) -> bool:
    if float(el)%1==0:
        return True
    else:
        return False

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


        if not checkE(el):
            print('Неверный ввод!')
            checkInp = False
    else:
        print('Неверный ввод!')
        checkInp = False

#Преобразование в целые числа из строки
for i in range(len(a)):
    a[i] = float(a[i])
    a[i] = int(a[i])

print('Исходная последовательность: {}'.format(a))
print('Новая последовательность: {}'.format(f(a)))
