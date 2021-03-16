f = open('in.txt', 'r')
g = open('tmp.txt', 'w')


def get_max_word_in_line(line: str) -> str:
    max_len = 0
    cur_len = 0
    if len(line) == 0:
        return ''
    if len(line) == 1:
        return line
    for i in range(len(line)):
        if not line[i].isspace():
            cur_len += 1
            if i == len(line) - 1 and cur_len > max_len:
                max_len = cur_len
                cur_len = 0

        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = 0

    cur_len = 0
    for i in range(len(line)):
        if not line[i].isspace():
            cur_len += 1
            if cur_len == max_len:
                return line[i-max_len+1:i+1]
        else:
            cur_len = 0


for line in f:
    q = str(get_max_word_in_line(line[:-1]) + '\n')
    print(q)
    g.write(q)

# for line in f:
#     words = line.split()
#     if len(words) == 0:
#         g.write('\n')
#     else:
#         index_max_word = 0
#         max_word = len(words[0])
#         for i in range(len(words)):
#             if len(words[i]) > max_word:
#                 max_word = len(words[i])
#                 index_max_word = i
#         g.write(words[index_max_word] + '\n')
f.close()
g.close()

g = open('tmp.txt', 'r')
output_file = open('out.txt', 'a')

for line in g:
    if len(line) == 0:
        output_file.write('\n')

old_min = new_min = -1
while 1:
    g.seek(0)
    for line in g:
        if len(line) > new_min:
            new_min = len(line)

    if new_min == old_min:
        break

    g.seek(0)
    for line in g:
        if old_min < len(line) < new_min:
            new_min = len(line)

    g.seek(0)
    for line in g:
        if len(line) == new_min:
            output_file.write(line)

    old_min = new_min

g.close()
print(output_file.seek(0, 2))
output_file.close()
