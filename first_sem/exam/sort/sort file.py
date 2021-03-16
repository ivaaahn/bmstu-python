f = open('in', 'r')
g = open('out.txt', 'w')


def get_sum(line: str) -> int:
    sum_line: int = 0
    if line.isupper():
        return -1
    else:
        i = 0
        start = 0
        number = False
        while i < len(line):
            if line[i].isdigit() and not number:
                start = i
                number = True
            elif line[i].isalpha() and number:
                sum_line += int(line[start:i])
                number = False
            elif i == len(line) - 1 and number:
                sum_line += int(line[start:i + 1])
            i += 1
    return sum_line


def check_upper(line_num: int):
    f.seek(0)
    k = 0
    for line in f:
        if k == line_num:
            if get_sum(line) == -1:
                return line
            else:
                return False
        else:
            k += 1


def del_digits(line: str):
    new_line = ''
    for i in range(len(line)):
        if line[i].isalpha():
            new_line += line[i]
    return new_line


cur_line_num = 0  # Текущая строка в файле out.txt
cur_pos = 0

while check_upper(cur_line_num):
    g.write(del_digits(check_upper(cur_line_num)))
    cur_line_num += 1
    g.write('\n')

old_min = new_min = -1
while 1:
    f.seek(0)
    for line in f:  # Нахожу число, относительно которого буду искать новый минимум
        if get_sum(line) > old_min:
            new_min = get_sum(line)
            break

    if new_min == old_min:  # Условие выхода из цикла: два раза подряд один и тот же минимум
        break

    f.seek(0)
    for line in f:  # нахожу настоящий минимум, при этом он должен быть быльше старого минимума, т.к. поседний обработан
        if old_min < get_sum(line) < new_min:
            new_min = get_sum(line)

    old_min = new_min  # После чего обновляю старый минимум
    f.seek(0)
    count_writed_lines = 0  # Cчетчик записанных строк с текущей суммой
    for line in f:
        position = 0
        if get_sum(line) == old_min and (
                position > count_writed_lines or count_writed_lines == 0):  # Проверяю каждую строку на соответсвие минимуму
            g.write(del_digits(line))
            g.write('\n')
            cur_line_num += 1  # Обновляю текущую строку, после каждого врайта
            count_writed_lines += 1
            position += 1

            while check_upper(cur_line_num):  # Сразу же проверяю что на новой строке нет строки со всеми заглавными
                g.write(del_digits(check_upper(cur_line_num)))
                g.write('\n')
                cur_line_num += 1  # Обновляю текущую строку, после каждого врайта
            f.seek(0)

f.close()
g.close()
