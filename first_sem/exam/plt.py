import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

plt.figure(figsize=(7, 7))

x = np.array([age for age in range(11, 19)])

rus = np.array([7, 8, 9, 14.5, 15.0, 15.5, 15.0, 15.0], dtype=float)
usa = rus - 0.5 * np.random.rand(8)
afr = [7.7, 8.9, 10, 15.8, 17.6, 19.2, 19.0, 19.1]

wide = 0.3
plt.subplot(2, 2, 1)
plt.title('Длина члена в разных странах', loc='center', size=10)
plt.bar(x, rus, width=wide, color='r', label='Россия', edgecolor='k')
plt.bar(x + wide, usa, width=wide, color='b', label='США', edgecolor='k')
plt.bar(x + wide * 2, afr, width=wide, color='k', label='Африка', edgecolor='w')

plt.xticks(x + wide, x)
plt.yticks(np.arange(0, 21, 2.5))
plt.xlabel('Возраст (лет)')
plt.ylabel('Длина (см.)')
plt.grid(False)
plt.legend(loc=0)

plt.subplot(2, 2, 2)

def f(x):
    return np.sin(x) - x / 2


def df(x):
    return np.cos(x) - 1 / 2


plt.title('График функции')
x = np.linspace(-5, 5, 100)
y = f(x)
plt.plot(x, y, 'b' '--', linewidth=4, label='$y = sin(x) - x/2$')
x1 = opt.newton(f, 1, fprime=df, tol=0.0001)
plt.scatter(x1, 2)
plt.xticks(np.arange(-5, 6, 1))
plt.grid(True)
plt.legend(loc=0)
#
plt.subplot(2, 2, 3)
plt.title('Распределение роста людей людей')
lens = np.random.rand(150) * 0.7 + 1.40
plt.ylabel('Количество (чел)')
plt.xlabel('Рост(м.)')
plt.hist(lens, 50, color='g', edgecolor='k')
plt.xticks(np.arange(1.4, 2.1, 0.1))


plt.subplot(2, 2, 4)
plt.title('Выборы президента РФ 2024')
data = np.random.randint(1, 4, 1000)
putin = gir = vasya = 0
for choice in data:
    if choice == 1:
        putin += 1
    elif choice == 2:
        gir += 1
    elif choice == 3:
        vasya += 1

putin = (putin - 20)
gir = (gir - 60)
vasya = (vasya + 80)
labels = ['Путин', 'Жириновский', 'Васёк']

plt.pie([putin, gir, vasya], labeldistance=1.2, autopct='%.1f%%', labels=labels, explode=[0.1, 0.1, 0.3], shadow=True)

plt.show()
