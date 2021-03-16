def search(r, a, max_len):
    for i in range(len(a)):
        left, right = i - 1, i + r
        while left > 0 and right < len(a) - 1 and a[left] == a[right]:
            left, right = left - 1, right + 1
        if right - left + 1 > max_len and right - left + 1 > 1:
            pals.clear()
            max_len = right - left + 1
            pals.append([left, max_len])
        elif right - left + 1 == max_len and right - left + 1 > 1:
            pals.append([left, max_len])
    return max_len


data = [7, 8, 9, 10, 11, 13, 11, 10, 9, 8, 7, 6, 5, 4, 5, 6, 5, 1, 2, 3, 4, 4, 3, 2, 1, 5]
pals = []
# for i in range(len(a)):
#     left, right = i - 1, i + 1
#     while left > 0 and right < len(a) - 1 and a[left] == a[right]:
#         left, right = left - 1, right + 1
#     if right - left + 1 > maxlen and right - left + 1 > 1:
#         pals.clear()
#         maxlen = right - left + 1
#         start = left
#         pals.append([start, maxlen])
#     elif right - left + 1 == maxlen and right - left + 1 > 1:
#         start = left
#         pals.append([start, maxlen])
#
# for i in range(len(a)):
#     left, right = i - 1, i
#     while left > 0 and right < len(a) - 1 and a[left] == a[right]:
#         left, right = left - 1, right + 1
#     if right - left + 1 > maxlen and right - left + 1 > 1:
#         pals.clear()
#         maxlen = right - left + 1
#         start = left
#         pals.append([start, maxlen])
#     elif right - left + 1 == maxlen and right - left + 1 > 1:
#         start = left
#         pals.append([start, maxlen])
ml = search(r=0, a=data, max_len=0)
search(r=1, a=data, max_len=ml)
for j in range(len(pals)):
    start = pals[j][0]
    length = pals[j][1]
    end = start + length - 1
    print(start, end, length, data[start:end + 1])
