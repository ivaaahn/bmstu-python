f = open('database.txt', 'r', encoding='UTF-8')
g = open('many.txt', 'a+', encoding='UTF-8')

for line in f:
    name, amount, units, weight, store = line[:20].strip(), int(line[20:28].strip()), line[28:30].strip(), int(
        line[30:35].strip()), line[35:45].strip()

    if weight / 1000 > 10:
        if 2 <= amount % 10 <= 4 and not (12 <= amount % 100 <= 14):
            if units == 'шт':
                units += 'уки'
            else:
                units += 'ика'

        elif amount % 10 == 1 and amount % 100 != 11:
            if units == 'шт':
                units += 'ука'
            else:
                units += 'ик'

        else:
            if units == 'шт':
                units += 'ук'
            else:
                units += 'иков'

        g.write('{} {} "{}" хранится на складе "{}"\n'.format(amount, units, name, store))

f.close()
g.close()
