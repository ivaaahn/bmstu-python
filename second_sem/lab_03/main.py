import tkinter.ttk as ttk
import matplotlib
from random import randint, shuffle
from time import perf_counter
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox as mb

matplotlib.use("TkAgg")
scatter = None

data1 = []
'''array for task1'''

sizes = [500, 1000, 2000]
'''Размеры массива для Задачи 2'''

def checkErr(x: str) -> bool:
    try:
        int(x)
        return True
    except:
        return False


def cocktail_sort(a: list) -> None:
    left = 0
    right = len(a) - 1

    while left < right:
        for i in range(left, right, 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1

        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
        left += 1

def getRandArr(size: int, left: int=-100, right: int=100) -> list:
    array = [randint(left, right) for i in range(size)]
    return array


def getSortedArr(size: int) -> list:
    array = [i for i in range(size)]
    return array


def getReversedArr(size: int) -> list:
    return list(reversed(getSortedArr(size)))


def getTimeWork(data: list) -> float:
    start = perf_counter()
    cocktail_sort(data)
    end = perf_counter()
    return end - start


def renderTable(labels: list, values: list) -> None:
    tree.delete(*tree.get_children())
    for row, value in enumerate(values):
        tree.insert('', 'end', text='', values=(
            labels[row],
            '{:.4}'.format(value[0]),
            '{:.4}'.format(value[1]),
            '{:.4}'.format(value[2])))


def renderGraph(x: list, y: list) -> None:
    global scatter

    figure = plt.Figure(figsize=(40, 30), dpi=100)
    ax = figure.add_subplot(111)
    
    ax.clear()


    ax.plot(x, y, 'b')
    ax.plot(x, y, 'mo')

    ax.set_xticks(x)    
    ax.set_xlabel("SIZE")
    ax.set_ylabel("TIME(SIZE) [seconds]")

    try:
        scatter.get_tk_widget().destroy()
    except:
        scatter = None

    scatter = FigureCanvasTkAgg(figure, task3Graph)
    scatter.get_tk_widget().pack(side=TOP, fill=BOTH)
    
    scatter.draw()


def task1(arg: str) -> bool:
    global data1

    left = e_left.get()
    right = e_right.get()
    if not (checkErr(left) and checkErr(right)):
        mb.showerror('ERROR', 'Вы должны ввести целое число')
        return False

    left, right = int(left), int(right)

    if left >= right:
        mb.showerror('ERROR', 'A не может быть больше B')
        return False

    SIZE = randint(2, 10)
    if arg == 'G':
        data1 = getRandArr(SIZE, left, right)
        data1_str = ', '.join(map(str, data1))
        fieldG.config(state=NORMAL)
        fieldG.delete(0, END)
        fieldG.insert(0, data1_str)
        fieldG.config(state=DISABLED)

        buttonS.config(state=NORMAL)
    elif arg == 'S':
        cocktail_sort(data1)
        data1_str = ', '.join(map(str, data1))
        fieldS.config(state=NORMAL)
        fieldS.delete(0, END)
        fieldS.insert(0, data1_str)
        fieldS.config(state=DISABLED)
    return True


def task2() -> bool:
    global sizes

    N1 = e_N1.get()
    N2 = e_N2.get()
    N3 = e_N3.get()

    if not (checkErr(N1) and checkErr(N2) and checkErr(N3)):
        mb.showerror('ERROR', 'Вы должны ввести целое число')
        return False

    N1, N2, N3 = int(N1), int(N2), int(N3)

    if N1 <= 0 or N2 <= 0 or N3 <= 0:
        mb.showerror('ERROR', 'Вы должны ввести положительное число')
        return False
    else:
        sizes[0] = N1
        sizes[1] = N2
        sizes[2] = N3

    labels = ['Sorted',
              'Random',
              'Reversed']

    times = [[], [], []]

    for func in [getSortedArr, getRandArr, getReversedArr]:
        for i, time in enumerate(sizes):
            array = func(time)
            times[i].append(getTimeWork(array))
    print(times)
    renderTable(labels, times)

    return True


def task3() -> bool:
    start = e_start.get()
    step = e_step.get()

    if not (checkErr(start) and checkErr(step)):
        mb.showerror('ERROR', 'Вы должны ввести целое число')
        return False

    start, step = int(start), int(step)

    if not step:
         mb.showerror('ERROR', 'Шаг - положительное число')
         return False
    

         
    X = [q for q in range(int(start), int(start) + 10*int(step), int(step))]
    Y = []
    for size in X:
        array = getRandArr(size)
        tmp = getTimeWork(array)
        print(tmp)
        Y.append(tmp)
    print(Y)
    renderGraph(X, Y)

    return True


# Создание окна
root = Tk()
root.title("Сocktail sort(Shaker sort). Сортировка перемешиванием(Шейкер-сортировка)")
root.geometry("980x480")
root.resizable(0, 0)


task12 = Frame(root)

task1All = Frame(task12)

Label(task1All, text='Task 1', font="Segoe 22 bold").pack(anchor='n')

task1All.pack()

task1E = Frame(task1All)

l_left= Label(task1E, text='Left:', font="Segoe 14 bold")
l_right = Label(task1E, text='Right', font="Segoe 14 bold")

e_left = Entry(task1E, font=18, width=8)
e_right = Entry(task1E, font=18, width=8)

e_left.insert(0, 0)
e_right.insert(0, 10)

task1E.pack(side=LEFT, anchor='w')
l_left.pack(side=LEFT)
e_left.pack(side=LEFT, ipady=12, anchor='w')
l_right.pack(side=LEFT)
e_right.pack(side=LEFT, ipady=12, anchor='e')



task1G = Frame(task12)

buttonG = Button(task1G, text='Generate', command=lambda x='G': task1('G'), font='Cambria 12 bold',
                 width=14, height=2, bg='black', activebackground="#0B5FA4", fg='white')
fieldG = Entry(task1G, font="Segoe 16", width=28,
               disabledbackground="white", disabledforeground='black', state=DISABLED)

buttonG.pack(side=LEFT)
fieldG.pack(side=LEFT, ipady=16)
task1G.pack(anchor='nw')


task1S = Frame(task12)

buttonS = Button(task1S, text='Sort', command=lambda x='S': task1('S'), font='Cambria 12 bold',
                 width=14, height=2, bg='black', activebackground="#0B5FA4", fg='white', state=DISABLED)
fieldS = Entry(task1S, font="Segoe 16", width=28,
               disabledbackground="white", disabledforeground='black', state=DISABLED)

buttonS.pack(side=LEFT)
fieldS.pack(side=LEFT, ipady=16)
task1S.pack(anchor='nw')



task2All = Frame(task12)
Label(task2All, text='Task 2', font="Segoe 22 bold").pack()

task2E = Frame(task2All)
l_N1 = Label(task2E, text='N1', font="Segoe 14 bold")
l_N2 = Label(task2E, text='N2', font="Segoe 14 bold")
l_N3 = Label(task2E, text='N3', font="Segoe 14 bold")

e_N1 = Entry(task2E, font=18, width=12)
e_N2 = Entry(task2E, font=18, width=12)
e_N3 = Entry(task2E, font=18, width=12)

e_N1.insert(0, sizes[0])
e_N2.insert(0, sizes[1])
e_N3.insert(0, sizes[2])

l_N1.pack(anchor='n')
e_N1.pack(ipady=6)

l_N2.pack()
e_N2.pack(ipady=6)

l_N3.pack()
e_N3.pack(ipady=6)

Button(task2E, text='Calculate', command=task2, font='Cambria 12 bold',
       width=14, height=2, bg='black', activebackground="#0B5FA4", fg='white').pack(anchor='s')

tree = ttk.Treeview(task2All, selectmode='extended', height=3, columns=('1', "2", '3', '4'), show='headings')

tree.column("1", anchor='c', width=100)
tree.column("2", anchor='c', width=78)
tree.column("3", anchor='c', width=78)
tree.column("4", anchor='c', width=78)

tree.heading("2", text='N1')
tree.heading("3", text='N2')
tree.heading("4", text='N3')


task2All.pack(anchor='sw')
task2E.pack(side=LEFT, anchor='nw')
tree.pack(side=LEFT, fill=BOTH)
task12.pack(side=LEFT,anchor='nw')


task3All = Frame(root)
Label(task3All, text='Task 3', font="Segoe 22 bold").pack(anchor='n')
task3All.pack()

task3E = Frame(task3All)
Button(task3E, text='Build', command=task3, font='Cambria 12 bold',
       width=15, height=2, bg='black', activebackground="#0B5FA4", fg='white').pack(side=LEFT, anchor='w')

l_start = Label(task3E, text='Start:', font="Segoe 14 bold")
l_step = Label(task3E, text='Step:', font="Segoe 14 bold")

e_start = Entry(task3E, font=18, width=8)
e_step = Entry(task3E, font=18, width=8)

e_start.insert(0, 2000)
e_step.insert(0, 500)

l_start.pack(side=LEFT)
e_start.pack(side=LEFT, ipady=6)

l_step.pack(side=LEFT)
e_step.pack(side=LEFT, ipady=6)
task3E.pack()

task3Graph = Frame(task3All)
task3Graph.pack(side=LEFT)

root.mainloop()