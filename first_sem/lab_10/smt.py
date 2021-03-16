from tkinter import *

def hide_show():
    if label.winfo_viewable():
        label.grid_remove()
    else:
        label.grid()
root=Tk()
label = Label(text='Я здесь!')
label.grid()
button = Button(command=hide_show, text="Спрятать/показать")
button.grid()
root.mainloop()