# Лабораторная работа номер 9
# Выполнил: Ивахненко Дмитрий
# ИУ7-16Б
# Работа с текстом

# Текущее форматирование текста
# 0 - left
# 1 - width
# 2 - right
curAlign: int = 0

rus = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]
rus.append('ё')


def checkInWord2(a: str, b: str) -> bool:
    if b in a:
        for j in range(0, a.index(b[0])):
            if a[j] in rus:
                return False
        for i in range(a.rindex(b[-1]) + 1, len(a)):
            if a[i] in rus:
                return False
        return True
    return False


def error():
    print('Неверный ввод!')
    return False


def checkInterval(y: str):
    a = 0
    b = 7
    if not a <= int(y) <= b:
        print('Значение должно быть 0 <= a <= 7')
        return False
    return True


def checkNatural(x: str) -> bool:
    checkInp = True
    if len(x) > 0:
        for j in range(len(x)):
            if not (('1' <= x[j] <= '9') or (x[j] == '0' and j > 0) or (x[j] == '+' and j == 0 and len(x) > 1)):
                checkInp = error()
                break
    else:
        checkInp = error()
    return checkInp


def firstEdit(txt: list):
    for curRow in range(len(txt)):
        txt[curRow] = " ".join(txt[curRow].split())


# Поиск максимальной строки в тексте
def maxStrLen(txt: list) -> int:
    maxLen: int = 0
    for i in range(len(txt)):
        maxLen = max(maxLen, len(txt[i]))
    return maxLen


# Проверка, что данное слово нужно заменить
def checkInWord(a: str, b: str) -> bool:
    if b in a:
        if a[0] == "(" or a[0] == '"':
            a = a[1:]
        for i in range(len(b), len(a)):
            if a[i] not in ',.()!?-";:':
                return False
        return True
    return False


# Разбить данное выражение на части
def getNormalForm(a: str) -> list:
    if len(a) >= 3 and a[0].isdigit() and a[-1].isdigit():
        aCopy: list = [a]
        aNew = list()
        while '*' in aCopy[0] or '/' in aCopy[0]:
            if '*' in aCopy[0] and '/' in aCopy[0]:
                if aCopy[0].index('*') < aCopy[0].index('/'):
                    aCopy = list(aCopy[0].partition('*'))
                else:
                    aCopy = list(aCopy[0].partition('/'))
            elif '*' in aCopy[0]:
                aCopy = list(aCopy[0].partition('*'))
            elif '/' in aCopy[0]:
                aCopy = list(aCopy[0].partition('/'))
            if aCopy[0].isdigit():
                aNew.append(int(aCopy.pop(0)))
                aNew.append(aCopy.pop(0))
            else:
                return []
        aNew.append(int(aCopy.pop(0)))
        return aNew
    else:
        return []


# Выравнивание по левому краю
def alignLeft(txt: list):
    for curRow in range(len(txt)):
        txt[curRow] = " ".join(txt[curRow].split())
    global curAlign
    curAlign = 0


# Выравнивание по ширине
def alignWidth(txt: list):
    for curRow in range(len(txt)):
        delta: int = maxStrLen(txt) - len(' '.join(txt[curRow].split()))
        wordsInRow: int = len(txt[curRow].split())
        try:
            spacesPerWord: int = delta // (wordsInRow - 1) + 1
            restSpaces: int = delta % (wordsInRow - 1)
        except ZeroDivisionError:
            spacesPerWord = maxStrLen(txt) // 2
            restSpaces = 0
        tempRow: list = txt[curRow].split()
        if len(tempRow) > 0:
            txt[curRow] = ''
            for word in range(len(tempRow) - 1):
                if restSpaces > 0:
                    txt[curRow] += tempRow[word] + ' ' * (spacesPerWord + 1)
                    restSpaces -= 1
                else:
                    txt[curRow] += tempRow[word] + ' ' * spacesPerWord
            txt[curRow] += tempRow[-1]
            global curAlign
            curAlign = 1


# Выравниевание по правому краю
def alignRight(txt: list):
    for curRow in range(len(txt)):
        delta = maxStrLen(txt) - len(' '.join(txt[curRow].split()))
        txt[curRow] = ' ' * delta + ' '.join(txt[curRow].split())
    global curAlign
    curAlign = 2


# Замена слова
def replaceWord(txt: list, oldWord: str, newWord: str):
    for curRow in range(len(txt)):
        tempRow: list = txt[curRow].split()
        for curWord in range(len(tempRow)):
            if checkInWord2(tempRow[curWord], oldWord):
                tempRow[curWord] = tempRow[curWord].replace(oldWord, newWord)
        txt[curRow] = ' '.join(tempRow)


# Удаление слова
def deleteWord(txt: list, word: str):
    replaceWord(txt, word, '')


# Решение арифметики
def solveAriph(txt: list):
    for curRow in range(len(txt)):
        tempRow: list = txt[curRow].split()
        for curWord in range(len(tempRow)):
            if len(getNormalForm(tempRow[curWord])) > 0:
                expres = getNormalForm(tempRow[curWord])
                result = expres[0]
                for symb in range(2, len(expres), 2):
                    if expres[symb - 1] == '*':
                        result *= expres[symb]
                    else:
                        try:
                            result /= expres[symb]
                        except ZeroDivisionError:
                            break
                    tempRow[curWord] = str(result)
                    txt[curRow] = ' '.join(tempRow)
    return


# Удаление самого длинного слова в самой многословной строке
def delLongest(txt: list):
    indOfMaxRow = lenOfMaxRow = 0
    for curRow in range(len(txt)):
        if lenOfMaxRow < len(txt[curRow].split()):
            lenOfMaxRow = len(txt[curRow].split())
            indOfMaxRow = curRow

    tempRow = txt[indOfMaxRow].split()
    lenOfMaxWord = indOfMaxWord = 0
    for curWord in range(len(tempRow)):
        if len(tempRow[curWord]) > lenOfMaxWord:
            lenOfMaxWord = len(tempRow[curWord])
            indOfMaxWord = curWord
    tempRow.pop(indOfMaxWord)
    txt[indOfMaxRow] = ' '.join(tempRow)


# Вывод текста
def printText(txt: list):
    global curAlign
    if curAlign == 0:
        alignLeft(txt)
    elif curAlign == 1:
        alignWidth(txt)
    elif curAlign == 2:
        alignRight(txt)
    print('*' * maxStrLen(txt))
    for i in range(len(txt)):
        print(txt[i])
    print('*' * maxStrLen(txt))


# Вывод меню
def printMenu():
    print('Вот что я умею!')
    print('1. Выровнять текст по левому краю')
    print('2. Выровнять текст по правому краю')
    print('3. Выровнять текст по ширине')
    print('4. Найти и заменить слово')
    print('5. Найти и удалить слово')
    print('6. Заменить арифметические операции с "*" "/" их результатом')
    print('7. (NEW!) Удалить самое длинное слово в строке, содержащей наибольшее кол-во слов')
    print('0. Выход')


# Начало работы программы
def start(txt: list):
    printText(txt)
    printMenu()
    q = input('Введите цифру: ').strip()

    while not checkNatural(q) or not checkInterval(q):
        q = input('Введите цифру: ').strip()
    q = int(q)

    if q == 1:
        alignLeft(txt)
        return 1
    elif q == 2:
        alignRight(txt)
        return 2
    elif q == 3:
        alignWidth(txt)
        return 3
    elif q == 4:
        old = input('Введите слово, которое хотите заменить: ')
        while len(old) == 0:
            print('Вы ввели пустую строку. Повторите ввод')
            old = input('Введите слово, которое хотите заменить: ')

        new = input('Введите новое слово: ')
        while len(new) == 0:
            print('Вы ввели пустую строку. Повторите ввод')
            new = input('Введите новое слово: ')

        replaceWord(txt, old, new)
        return 4
    elif q == 5:
        word = input('Введите слово, которое хотите удалить: ')
        while len(word) == 0:
            print('Вы ввели пустую строку. Повторите ввод')
            word = input('Введите слово, которое хотите удалить: ')
        deleteWord(txt, word)
        return 5
    elif q == 6:
        solveAriph(txt)
        return 6
    elif q == 7:
        delLongest(txt)
        return 7
    else:
        return 0


f = open('text.txt', 'r', encoding='UTF8')
text = f.readlines()
f.close()
firstEdit(text)

k = True
while k:
    k = start(text)
