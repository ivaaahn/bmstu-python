def elDelete(index: int, arr: list):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]


b = [5, 5, 1, 5, 5, 0, 5]
NUM = []
maxx = b[0]

i = 1
while i < len(b):
    if b[i] == maxx:
        NUM.append(i)
    elif b[i] > maxx:
        maxx = b[i]
        NUM.clear()
        NUM.append(i)
    i += 1

l = 0
for index in range(0, len(NUM)):
    elDelete(NUM[index], b)

if b[0] == b[1] == maxx:
    print('Все элы одинак')
else:
    print(NUM)
    print(b)
