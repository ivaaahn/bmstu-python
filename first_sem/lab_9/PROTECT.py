glas = 'АаЕеЁёИиОоУуЫыэЭюЮЯя'
sogl = 'БбВвГгДдЖжЗзКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщЪъЬь'


def firstEdit(txt: list):
    for curRow in range(len(txt)):
        txt[curRow] = " ".join(txt[curRow].split())


f = open('text.txt', 'r', encoding='UTF8')
text = f.readlines()
f.close()
firstEdit(text)

new = ' '.join(text).split('.')
firstEdit(new)

indexRow = -1
max_k = 0
last = False  # F - согл, T - глас
flag = False
for curRow in range(len(new)):
    tempStr = new[curRow].split()
    cur_k = 0
    for curWord in range(len(tempStr)):

        if len(tempStr[curWord]) > 1 and tempStr[curWord][0] in sogl:
            last = False
        elif len(tempStr[curWord]) > 1 and tempStr[curWord][0] in glas:
            last = True
        else:
            break

        for sym in range(1, len(tempStr[curWord])):
            if (tempStr[curWord][sym] in glas and last is False) or (tempStr[curWord][sym] in sogl and last is True):
                last = not last
                flag = True
            else:
                flag = False
                break

        if flag is True:
            cur_k += 1

    if cur_k > max_k:
        max_k = cur_k
        indexRow = curRow


print(new[indexRow])
