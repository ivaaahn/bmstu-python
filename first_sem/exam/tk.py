from tkinter import *

def choice():
    q = var.get()
    if q:
        print('mom')
        print(q)
    else:
        print(q)
        print('dad')

root = Tk()

var = BooleanVar()

mom = Radiobutton(root, text='mom', variable = var, value=True)
dad = Radiobutton(root, text='dad', variable=var, value=False)

x = Button(root, text='Выбор', command=choice)

mom.pack()
dad.pack()
x.pack()

root.mainloop()