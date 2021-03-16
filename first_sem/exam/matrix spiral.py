def foo(x: int):
    i = j = 0
    a[0][0] = x
    x -= 1
    while x > 0:
        while j + 1 < N and a[i][j + 1] == 0:
            a[i][j + 1] = x
            x -= 1
            j += 1

        while i + 1 < N and a[i + 1][j] == 0:
            a[i + 1][j] = x
            x -= 1
            i += 1
        while a[i - 1][j - 1] == 0:
            a[i - 1][j - 1] = x
            x -= 1
            i -= 1
            j -= 1


N = int(input('Введите N: '))
a = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(a[i])

x = N * (N + 1) // 2
foo(x)

for i in range(N):
    print(a[i])
