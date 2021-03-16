import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np


def create():
    move_btn.config(state=tk.NORMAL)

    x_min = int(x_min_field.get())
    x_max = int(x_max_field.get())

    points_number = int(points_number_field.get())

    x = np.linspace(x_min, x_max, points_number)
    y = x * x

    plt.cla()
    plt.plot(x, y, 'b')
    plt.show()


def change():
    plt.axis([int(x_first_field.get()), int(x_last_field.get()), int(y_first_field.get()), int(y_last_field.get())])
    plt.show()


root = tk.Tk()
root.title("Input")
root.geometry("220x250")

graph = tk.Frame(root)
graph.grid(row=0, column=0)

axis = tk.Frame(root)
axis.grid(row=3, column=0)

graph_main_label = tk.Label(graph, text='Graph')
graph_main_label.grid(row=1, column=1, sticky=tk.W)

x_min_label = tk.Label(graph, text='Xmin:')
x_min_label.grid(row=2, column=0, sticky=tk.W)
x_min_field = tk.Entry(graph)
x_min_field.grid(row=2, column=1, sticky=tk.W)

x_max_label = tk.Label(graph, text='Xmax:')
x_max_label.grid(row=3, column=0, sticky=tk.W)
x_max_field = tk.Entry(graph)
x_max_field.grid(row=3, column=1, sticky=tk.W)

points_number_label = tk.Label(graph, text='Points number:')
points_number_label.grid(row=4, column=0, sticky=tk.W)
points_number_field = tk.Entry(graph)
points_number_field.grid(row=4, column=1, sticky=tk.W)

create_btn = tk.Button(graph, text='Create', command=create)
create_btn.grid(row=5, column=1, sticky=tk.W)



axis_main_label = tk.Label(axis, text='Axis')
axis_main_label.grid(row=7, column=1, sticky=tk.W)

x_first_label = tk.Label(axis, text='X First:')
x_first_label.grid(row=8, column=0, sticky=tk.W)
x_first_field = tk.Entry(axis)
x_first_field.grid(row=8, column=1, sticky=tk.W)

x_last_label = tk.Label(axis, text='X Last:')
x_last_label.grid(row=9, column=0, sticky=tk.W)
x_last_field = tk.Entry(axis)
x_last_field.grid(row=9, column=1, sticky=tk.W)

y_first_label = tk.Label(axis, text='Y First:')
y_first_label.grid(row=10, column=0, sticky=tk.W)
y_first_field = tk.Entry(axis)
y_first_field.grid(row=10, column=1, sticky=tk.W)

y_last_label = tk.Label(axis, text='Y Last:')
y_last_label.grid(row=11, column=0, sticky=tk.W)
y_last_field = tk.Entry(axis)
y_last_field.grid(row=11, column=1, sticky=tk.W)

move_btn = tk.Button(axis, state=tk.DISABLED, text='Move', command=change)
move_btn.grid(row=12, column=1, sticky=tk.W)

root.mainloop()
