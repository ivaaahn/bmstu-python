# Правильная скобочная последовательность
def max_p(index, line):
    stack = []
    i = index  # индекс с которого начинаем поиск правой части комбо
    max_right = -1  # максимальный индекс правого элемента
    while i < len(line):
        if line[i] in various:
            stack.append(line[i])
        else:
            if len(stack) < 1:  # Если лишняя правая скобка - брейкаемся
                break
            last = stack.pop()
            if (last == '(' and line[i] == ')') or (last == '[' and line[i] == ']') or (last == '{' and line[i] == '}'):
                if len(stack) == 0:  # обновляем индекс макс. правого элемента, если все скобки закрылись
                    max_right = i
            else:
                return max_right
        i += 1
    return max_right


s = input('Введите строку: ')
max_line = 0
ans = []
various = '({['
for k in range(len(s)):  # Бежим по строке
    if s[k] in various:  # Если видим открывающуюся скобку
        cur_line = max_p(k, s)  # Бежим по строке с k-го эл-та и ищем правую часть комбо
        if cur_line - k + 1 > max_line:  # Если найденное комбо по длине больше max_line
            ans.clear()  # Очищаем массив с ответами
            ans.append([k, cur_line])  # Добавляем [нач элемент, длина]
            max_line = cur_line - k + 1  # Обновляем максимальную длину
        elif cur_line - k + 1 == max_line:  # Если текущая длина совпала с максимальной
            ans.append([k, cur_line])  # Просто добавляем [нач элемент, длина]

print('Выбирайте: ')

for k in range(len(ans)):
    # Вывод: строка, начало, конец, длина
    print(s[ans[k][0]:ans[k][1] + 1], ans[k][0], ans[k][1], ans[k][1] - ans[k][0] + 1)
