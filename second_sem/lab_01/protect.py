import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox as mb

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify
from sympy.parsing.sympy_parser import parse_expr

matplotlib.use("TkAgg")

data = []

scatter = None


def f(x):
    arg = symbols('x')
    expr = parse_expr(_func.get())
    _f = lambdify(arg, expr, 'numpy')
    try:
        return _f(x)
    except:
        mb.showerror("Ошибка", "Что-то пошло не так")


def renderTable():
    tree.delete(*tree.get_children())
    for i, d in enumerate(data, start=1):
        tree.insert("", 'end', text=i, values=(
            "{:.3g}".format(d["Точка"]),
            "{:.7g}".format(d["Значение функции"]),
        ))


def create():
    global scatter
    a = float(left_border.get())
    b = float(right_border.get())
    h = float(step.get())

    figure = plt.Figure(figsize=(40, 30), dpi=100)
    ax = figure.add_subplot(111)
    x = np.arange(a, b, 0.01)
    y = f(x)
    y0 = x * 0

    ax.clear()
    ax.plot(x, y, 'b', label=parse_expr(_func.get()))
    ax.plot(x, y0, 'b', color='r')

    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")

    create_calculate(a, b, h)
    renderTable()

    try:
        scatter.get_tk_widget().destroy()
    except:
        scatter = None

    scatter = FigureCanvasTkAgg(figure, graph)
    scatter.get_tk_widget().pack(side=TOP, fill=BOTH)
    ax.legend()
    scatter.draw()


def create_calculate(a, b, h):
    value = a
    data.clear()
    while value < b:
        data.append({"Точка": value, "Значение функции": f(value)})
        value += h


# Создание окна
root = Tk()
root.title("Найти значения функции")
root.geometry("600x650")
root.resizable(0, 0)

# Фрейм для верхней части окна
top = Frame(root)
top.pack(anchor='nw')

# Фрейм для полей ввода
mainFrame = Frame(top, width=50, height=100)
mainFrame.pack(side=LEFT)

# Фрейм для таблички
table = Frame(top, width=500, height=100)
table.pack()

# Фрейм для графика
graph = Frame(root, width=1000, height=200)
graph.pack(side=LEFT)

# Поля ввода
_func_l = Label(mainFrame, text='Функция', font=14)
_func = Entry(mainFrame, font=18, width=14)
_func_l.pack(anchor='n')
_func.pack(anchor='n')
_func.insert(0, 'sin(x)')

left_border_l = Label(mainFrame, text='Левая граница', font=14)
left_border = Entry(mainFrame, font=18, width=14)
left_border_l.pack(anchor='n')
left_border.pack(anchor='n')
left_border.insert(0, '-10')

right_border_l = Label(mainFrame, text='Правая граница', font=14)
right_border = Entry(mainFrame, font=18, width=14)
right_border_l.pack(anchor='n')
right_border.pack(anchor='n')
right_border.insert(0, '10')

step_l = Label(mainFrame, text='Шаг', font=14)
step = Entry(mainFrame, font=18, width=14)
step_l.pack(anchor='n')
step.pack(anchor='n')
step.insert(0, '1')

# Кнопка Create
create_b = Button(mainFrame, text='Create', command=create, width=16, height=1, bg='#123EAB',
                  activebackground="#0B5FA4", fg='#ffffff', font='16')
create_b.pack(side=BOTTOM)

# Создание таблицы
tree = ttk.Treeview(table, selectmode='extended', height=10)
vsb = ttk.Scrollbar(table, orient="vertical", command=tree.yview)

tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("1", "2")
tree['show'] = 'headings'
tree.column("1", anchor='c', width=210)
tree.column("2", anchor='c', width=210)
tree.heading("1", text="Аргумент (X)")
tree.heading("2", text="Значение функции (Y)")

tree.pack(side=LEFT, fill=BOTH)
vsb.pack(side=RIGHT, fill=Y)

root.mainloop()
