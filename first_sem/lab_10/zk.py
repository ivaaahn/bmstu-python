f = open('text.txt', 'r', encoding='UTF8')
text = f.readlines()
f.close()

numbers = []
eMails = []

for curLine in range(0, len(text)):
    tempLine = text[curLine].split()
    for curWord in range(0, len(tempLine)):
        if '@' in tempLine[curWord]:
            maybeMail = tempLine[curWord].split('@')
            if len(maybeMail) == 2:
                if ',' not in tempLine[curWord] and '.' in maybeMail[1] and len(maybeMail[1].split('.')) == 2:
                    eMails.append(tempLine[curWord])
        elif tempLine[curWord][:2] == '89' and len(tempLine[curWord]) == 11 and tempLine[curWord].isdigit():
            numbers.append(tempLine[curWord])

print('Numbers: ')
for i in range(len(numbers)):
    print('#{}: {}'.format(i + 1, numbers[i]))

print('\neMails: ')
for j in range(len(eMails)):
    print('#{}: {}'.format(j + 1, eMails[j]))
