import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox as mb

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify, diff
from sympy.parsing.sympy_parser import parse_expr

matplotlib.use("TkAgg")

data = []
extremums = []


# Функции для подсчета f(x) и ее производной
def f(x):
    arg = symbols('x')
    expr = parse_expr(_func.get())
    _f = lambdify(arg, expr, 'numpy')
    try:
        return _f(x)
    except:
        mb.showerror("Ошибка", "Что-то пошло не так")


def df(x):
    arg = symbols('x')
    expr = diff(parse_expr(_func.get()))
    _df = lambdify(arg, expr, 'numpy')
    try:
        return _df(x)
    except:
        mb.showerror("Ошибка", "Что-то пошло не так")


# Функции для уточнения корней и для уточнения экстремумов

def secants(left: float, right: float, eps: float, amount: int):
    step_eps = 0.1
    num_of_iterations = 0

    x0 = left
    x1 = x0 + step_eps
    while abs(x1 - x0) >= eps and num_of_iterations < amount:
        x1, x0 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)), x1
        num_of_iterations += 1

    print("numof == ", num_of_iterations)
    print("x == ", x1)
    if check_error(left, right, x1) == 0 or num_of_iterations == amount:
        x0 = right
        x1 = x0 - step_eps
        num_of_iterations = 0
        while abs(x1 - x0) >= eps and num_of_iterations < amount:
            x1, x0 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)), x1
            num_of_iterations += 1
    print("numof == ", num_of_iterations)
    print("x == ", x1)
    return x1, num_of_iterations


def bisection(left: float, right: float, func=df):
    eps = 1e-10
    while abs(right - left) >= eps:
        center = (left + right) / 2
        if func(left) * func(center) < 0:
            right = center
        else:
            left = center

    return center


# Функция, создающая таблицу

def renderTable():
    tree.delete(*tree.get_children())
    for i, d in enumerate(data, start=1):
        tree.insert("", 'end', text=i, values=(
            i,
            "[{:.3g};{:.3g}]".format(d["begin"], d["end"]),
            "{:.7g}".format(d["root"]),
            "{:.0e}".format(f(d["root"])),
            d["iter"],
            d["err"],

        ))
    if len(data) == 0:
        mb.showinfo('Информация', 'Корней нет!')


# Функции, проверяющие корректность

def check_error(a: float, b: float, x: float) -> bool:
    return a < x < b


def check_correct(a: str):
    try:
        float(a)
        return True
    except:
        return False


def check_correct_int(a: str):
    try:
        int(a)
        return True
    except:
        return False


def root_exist(left: float, right: float, func=f):
    return func(left) * func(right) <= 0  # одинаковые знаки


scatter = None


# Функция, которая строит график
def create():
    global scatter
    a = left_border.get()
    b = right_border.get()
    h = step.get()
    eps = precision.get()
    amount = num_of_iter.get()

    if not (check_correct(a) and check_correct(b) and check_correct(h) and check_correct(eps) and check_correct_int(
            amount) and float(eps) > 0 and float(h) > 0 and float(b) > float(a) and int(amount) > 0):
        mb.showerror("Ошибка", "Некорректный ввод")
        return -1
    else:
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)
        amount = int(amount)

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

    calculate(a, b, h, eps, amount)
    renderTable()

    x_roots = np.array([d["root"] for d in data if d["err"] != "Выход за пределы"])
    x_roots_err = np.array([d["root"] for d in data if d["err"] == "Выход за пределы"])

    y_roots = 0 * x_roots
    y_roots_err = 0 * x_roots_err

    ax.plot(x_roots, y_roots, 'go', label='roots')
    ax.plot(x_roots_err, y_roots_err, 'ko', label='errors')

    search_extremums(a, b, h / 2)

    x_extremums = np.array(extremums)
    y_extremums = f(x_extremums)

    ax.plot(x_extremums, y_extremums, 'mo', label='extremums')

    try:
        scatter.get_tk_widget().destroy()
    except:
        scatter = None

    scatter = FigureCanvasTkAgg(figure, graph)
    scatter.get_tk_widget().pack(side=TOP, fill=BOTH)
    ax.legend()
    scatter.draw()


# Основная функция для подсчета корней
def calculate(a, b, h, eps, amount):
    cur_start = a
    interval_num = 0
    data.clear()
    while cur_start < b:
        cur_end = (cur_start + h >= b) * b + (cur_start + h < b) * (cur_start + h)
        print("cur_start = ", cur_start, interval_num)
        print("cur_end = ", cur_end, interval_num)

        if interval_num == 0 and f(cur_start) == 0:
            print("first")
            cur_x = cur_start
            num_of_iterations = 0
            data.append(
                {"begin": cur_start, "end": cur_end, "root": cur_x, "iter": num_of_iterations,
                 "err": 'Корень на границе'})
            cur_start += h
            interval_num += 1

        elif root_exist(cur_start, cur_end) and f(cur_end) == 0:
            # print("second")
            cur_x = cur_end
            num_of_iterations = 0
            data.append(
                {"begin": cur_start, "end": cur_end, "root": cur_x, "iter": num_of_iterations,
                 "err": 'Корень на границе'})
            cur_start += 2 * h
            interval_num += 1

        elif root_exist(cur_start, cur_end):
            print("third")
            cur_x, num_of_iterations = secants(cur_start, cur_end, eps, amount)
            if check_error(cur_start, cur_end, cur_x):
                print("third + no error")
                data.append(
                    {"begin": cur_start, "end": cur_end, "root": cur_x, "iter": num_of_iterations, "err": 'Ошибок нет'})
            else:
                print("third + error")
                temp = bisection(cur_start, cur_end, f)
                data.append(
                    {"begin": cur_start, "end": cur_end,
                     "root": temp, "iter": num_of_iterations,
                     "err": 'Выход за пределы'})

            cur_start += h
            interval_num += 1

        else:
            print("fourth")
            cur_start += h


# Основная функция для подсчета экстремумов
def search_extremums(a, b, h):
    cur_start = a
    interval_num = 0
    extremums.clear()
    while cur_start < b:
        cur_end = (cur_start + h >= b) * b + (cur_start + h < b) * (cur_start + h)
        if interval_num == 0 and df(cur_start) == 0:
            # extremums.append(cur_start)
            cur_start += h
            interval_num += 1

        if root_exist(cur_start, cur_end, df) and df(cur_end) == 0:
            if cur_end != b:
                extremums.append(cur_end)
            cur_start += 2 * h
            interval_num += 1

        elif root_exist(cur_start, cur_end, df):
            cur_x = bisection(cur_start, cur_end)
            extremums.append(cur_x)
            cur_start += h
            interval_num += 1

        else:
            cur_start += h


# Создание окна
root = Tk()
root.title("Уточнение корней (МЕТОД СЕКУЩИХ)")
root.geometry("1100x750")
root.resizable(0, 0)

# Фрейм для верхней части окна
top = Frame(root)
top.pack(anchor='nw')

# Фрейм для полей ввода
mainFrame = Frame(top, width=50, height=150)
mainFrame.pack(side=LEFT)

# Фрейм для таблички
table = Frame(top, width=500, height=150)
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

right_border_l = Label(mainFrame, text='Правая граница', font=14)
right_border = Entry(mainFrame, font=18, width=14)
right_border_l.pack(anchor='n')
right_border.pack(anchor='n')

step_l = Label(mainFrame, text='Шаг', font=14)
step = Entry(mainFrame, font=18, width=14)
step_l.pack(anchor='n')
step.pack(anchor='n')

precision_l = Label(mainFrame, text='Точность', font=14)
precision = Entry(mainFrame, font=18, width=14)
precision_l.pack(anchor='n')
precision.pack()
precision.insert(0, 0.0001)

num_of_iter_l = Label(mainFrame, text='Кол-во итераций', font=14)
num_of_iter = Entry(mainFrame, font=18, width=14)
num_of_iter_l.pack(anchor='n')
num_of_iter.pack(anchor='n')
num_of_iter.insert(0, 500)

# Кнопка Create
create_b = Button(mainFrame, text='Create', command=create, width=16, height=1, bg='#123EAB',
                  activebackground="#0B5FA4", fg='#ffffff', font='16')
create_b.pack(side=BOTTOM)

# Создание таблицы
tree = ttk.Treeview(table, selectmode='extended', height=15)
vsb = ttk.Scrollbar(table, orient="vertical", command=tree.yview)

tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("1", "2", "3", "4", "5", "6")
tree['show'] = 'headings'
tree.column("1", anchor='c', width=35)
tree.column("2", anchor='c', width=160)
tree.column("3", anchor='c', width=160)
tree.column("4", anchor='c', width=160)
tree.column("5", anchor='c', width=160)
tree.column("6", anchor='c', width=230)
tree.heading("1", text="№")
tree.heading("2", text="Отрезок")
tree.heading("3", text="Корень")
tree.heading("4", text="Значение")
tree.heading("5", text="Кол-во итераций")
tree.heading("6", text="Ошибка или особенность")

tree.pack(side=LEFT, fill=BOTH)
vsb.pack(side=RIGHT, fill=Y)

root.mainloop()
