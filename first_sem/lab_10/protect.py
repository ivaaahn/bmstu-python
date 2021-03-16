f = open('a', 'a+', encoding='utf-8')
g = open('b', 'a+', encoding='utf-8')

f.seek(0)
max_length = len(f.readline()) - 1

i = 0
while i < max_length:
    f.seek(0)
    new_line = []
    for line in f:
        new_line += line[i]
    i += 1
    g.write(''.join(new_line))
    g.write('\n')

f.close()
g.close()
