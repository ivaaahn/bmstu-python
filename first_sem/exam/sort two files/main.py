f1 = open('in1', 'r')
f2 = open('in2', 'r')
g1 = open('in1_sorted', 'w')
g2 = open('in2_sorted', 'w')


def sort_file(file, file2):
    old_min = int(file.readline())
    for line in file:
        if int(line) < old_min:
            old_min = int(line)
    old_min -= 1
    new_min = None
    while 1:
        file.seek(0)
        for line in file:
            if int(line) > old_min:
                new_min = int(line)
                break

        if old_min == new_min:
            break

        file.seek(0)
        for line in file:
            if old_min < int(line) < new_min:
                new_min = int(line)

        file.seek(0)
        for line in file:
            if int(line) == new_min:
                file2.write(line[0] + '\n')

        old_min = new_min


sort_file(f1, g1)
sort_file(f2, g2)

f1.close()
f2.close()
g1.close()
g2.close()

g1 = open('in1_sorted', 'r')
g2 = open('in2_sorted', 'r')
z = open('out', 'w')

x = g1.readline()
y = g2.readline()
while not (x is None and y is None):
    if not y or int(x) <= int(y):
        z.write(x[0] + '\n')
        temp = g1.readline()
        x = temp if temp else None
    elif not x or int(y) < int(x):
        z.write(y[0] + '\n')
        temp = g2.readline()
        y = temp if temp else None

g1.close()
g2.close()
z.close()
