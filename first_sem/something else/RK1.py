a = ['q', 'd', 's', 'd', 'e', 's', 'p']


for i in range(len(a)):
    checkEqual = True
    for j in range(len(a)):
        if a[j] == a[i] and i != j:
            checkEqual = False
            break

    if checkEqual:
        print(a[i], end='')