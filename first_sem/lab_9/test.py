rus = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]
rus.append('ё')

num = '0123456789'
op = '/*'

row = 'err fegrt e trg er grte'.split()
newRow = []
curSolve = []

curSym = 0
checkNormal = False
while curSym < len(row):
    if row[curSym].isdigit() and row[curSym - 1] == ' ':
        sym = start = curSym+1
        end = -1
        solve = False
        while 1:


            if row[sym-1] == ' ' and row[sym-2] in num:
                if (row[sym] not in op) or (row[sym] in op and row[sym] :
                    solve = True
                    end = sym-2
                    break





    else:
        newRow.append(row[curSym])
        curSym += 1

'''
Бегу по строке, нахожу цифру => начало возможного выражения
Начинаю отдельно анализировать выражение:
бегу по нему, пока не встречу ** или // или */ или /* или букву или "цифра"+"пробел"+НЕ(* или /)
если флаг фолс, то ничего не делать
если флаг тру, значит это выражение нужно прочекать дополнительно
спличу срез в массив, убивая 

'''
