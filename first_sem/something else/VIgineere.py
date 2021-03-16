reverse = bool(int(input("Чтобы дешифровать, введите: '1', иначе '0': ")))
word = input('Введите слово, которое вы хотите (за/де)шифровать: ').strip()
key = input('Введите ключевое слово: ').strip()

keySymbols = []
for i in key:
    keySymbols.append(i)

newWordSymbols = []
numOfKeySymbol = 0

for oldSymbol in word:
    if not reverse:
        newWordSymbols.append(chr(ord(oldSymbol) + ord(keySymbols[numOfKeySymbol]) - 65))
    else:
        newWordSymbols.append(chr( ord(oldSymbol) - ord(keySymbols[numOfKeySymbol])+65))

    if numOfKeySymbol == len(keySymbols) - 1:
        numOfKeySymbol = -1
    numOfKeySymbol += 1

newWord = ''.join(newWordSymbols)
print('За(де)шифрованное слово: ', newWord)

