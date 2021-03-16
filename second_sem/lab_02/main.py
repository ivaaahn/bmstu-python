from tkinter import *
import tkinter.messagebox as mb
import pyperclip

need_clear: bool = True
checkpoint: bool = False
method: str = 'to_octal'


def change_color(event: str, x: str, btn: Button) -> None:
    if x == 'IN':
        btn.configure(bg='#B5B8B1')
    else:
        if btn in [bt, bl, bc]:
            btn.configure(bg='#403A3A')
        else:
            btn.configure(bg='black')


def make_clean() -> None:
    global need_clear, checkpoint
    field.delete(0, END)
    field.insert(END, '0')
    checkpoint = False
    need_clear = True


def make_input() -> None:
    global need_clear, checkpoint
    field.delete(0, END)
    checkpoint = False
    need_clear = False


def state_control(x: str) -> None:
    global method

    field.configure(state=NORMAL)
    make_clean()
    field.configure(state=DISABLED)

    if x == 'D':
        b8.configure(state=DISABLED)
        b9.configure(state=DISABLED)
        to_oct_btn.configure(relief=RAISED)
        to_oct_btn.configure(bg='#DBD7D2')
        to_dec_btn.configure(relief=SUNKEN)
        to_dec_btn.configure(bg='#1F75FE')
        precision_menu.entryconfig(2, state=NORMAL)
        method = 'to_decimal'

    else:
        b8.configure(state=NORMAL)
        b9.configure(state=NORMAL)
        to_oct_btn.configure(relief=SUNKEN)
        to_oct_btn.configure(bg='#1F75FE')
        to_dec_btn.configure(relief=RAISED)
        to_dec_btn.configure(bg='#DBD7D2')
        precision_menu.entryconfig(2, state=DISABLED)
        method = 'to_octal'


def dec_to_oct(number: int or float, precision: str = 'default') -> int or float:
    setminus = False
    if number < 0:
        number *= -1
        setminus = True

    _type = type(number)
    num_str = str(number)
    new_whole = new_frac = 0

    if _type == float:
        whole_part = int(num_str[:num_str.find('.')])
        frac_part = float('0.' + num_str[num_str.find('.') + 1:])

        if precision == 'default':
            precision = len(str(frac_part)) - 2
        else:
            precision = 8
    else:
        whole_part = number
        frac_part = precision = None

    if whole_part < 8:
        new_whole = whole_part
    else:
        counter = 1
        while whole_part:
            new_whole += (whole_part % 8) * counter
            whole_part //= 8
            counter *= 10

    if frac_part is None:
        return int(new_whole)

    counter = precision + 1
    while counter:
        frac_part *= 8
        fp_str = str(frac_part)

        new_frac = new_frac * 10 + int(frac_part)

        fp_str = '0.' + fp_str[fp_str.find('.') + 1:]
        frac_part = float(fp_str)

        counter -= 1

    new_frac = round(new_frac / (10 ** (precision + 1)), precision)
    return float(new_whole + new_frac) if not setminus else float(new_whole + new_frac) * (-1)


def oct_to_dec(number: int or float, precision: str = 'default') -> int or float:
    setminus = False
    if number < 0:
        number *= -1
        setminus = True

    _type = type(number)
    num_str = str(number)
    new_whole = new_frac = 0

    if _type == float:
        whole_part = int(num_str[:num_str.find('.')])
        frac_part = int(num_str[num_str.find('.') + 1:][::-1])

        if precision == 'default':
            precision = len(str(frac_part))
        elif precision == 'five':
            precision = 8
    else:
        whole_part = number
        frac_part = precision = None

    counter = 0
    while whole_part:
        new_whole += (whole_part % 10) * (8 ** counter)
        whole_part //= 10
        counter += 1

    if frac_part is None:
        return int(new_whole)

    counter = -1
    while frac_part:
        new_frac += (frac_part % 10) * (8 ** counter)
        frac_part //= 10
        counter -= 1

    if precision == 'not':
        precision = len(str(new_frac))

    return float(round(new_whole + new_frac, precision)) if not setminus else float(round(new_whole + new_frac, precision)) * (-1)


def check_input(key: str) -> bool:
    global checkpoint
    if key == '.' and checkpoint:
        return False

    if method == 'to_decimal' and (key in '89' or key == 'CV' and pyperclip.paste() in '89'):
        return False

    return True


def calc(event: str, key: str) -> None:
    global need_clear, method, checkpoint

    if not check_input(key):
        return

    if key == '.' and not checkpoint:
        checkpoint = True

    field.configure(state=NORMAL)

    if key == 'C':
        make_clean()

    elif key == 'CC':
        pyperclip.copy(field.get())

    elif key == 'CV':
        print(pyperclip.paste())
        try:
            float(pyperclip.paste())
            if field.get() == '0':
                make_input()
            field.insert(END, pyperclip.paste())
        except:
            field.configure(state=DISABLED)
            return

    elif key == 'T':
        if ('8' in field.get() or '9' in field.get()) and method == 'to_decimal':
            field.configure(state=DISABLED)
            mb.showerror('Ошибка', 'Ввод содержит цифру 8 или 9')
            return

        number = field.get()
        if not len(number.split()):
            field.configure(state=DISABLED)
            return

        number = float(number) if '.' in number else int(number)
        if method == 'to_octal':
            answer = dec_to_oct(number, set_precision.get())
        else:
            answer = oct_to_dec(number, set_precision.get())
        field.delete(0, END)
        field.insert(0, answer)
        need_clear = True

    elif key == 'E':
        exit(0)

    elif key == 'L':
        if field.get()[-1] == '.':
            checkpoint = False
        field.delete(len(field.get()) - 1, END)
        if len(field.get()) == 0 or field.get() == '-':
            make_clean()

    elif key == '-':
        if float(field.get()) == 0:
            field.configure(state=DISABLED)
            return

        if len(field.get()) and field.get()[0] == '-':
            field.delete(0, 1)
        else:
            field.insert(0, key)

    else:

        if need_clear:
            make_input()

        if key == '.' and len(field.get()) == 0:
            field.insert(END, '0')
            checkpoint = True

        if field.get() == '0' and key != '.':
            make_input()

        field.insert(END, key)

    field.configure(state=DISABLED)


root = Tk()
root.title("Translator")
root.geometry("280x408")
root.resizable(0, 0)

main_menu = Menu(root)
root.config(menu=main_menu)

option_menu = Menu(main_menu, tearoff=0)
option_menu.add_command(label="Перевести (<Enter>)",
                        command=lambda x='T': calc('', x))
option_menu.add_command(
    label="Скопировать в буфер (<Ctrl + C>)", command=lambda x='CC': calc('', x))
option_menu.add_command(
    label="Вставить из буфера (<Ctrl + V>)", command=lambda x='CV': calc('', x))
option_menu.add_command(label="Очистить (<Del>)",
                        command=lambda x='C': calc('', x))
option_menu.add_command(label="Выход", command=lambda x='E': calc('', x))

precision_menu = Menu(main_menu, tearoff=0)
set_precision = StringVar()
set_precision.set('default')
precision_menu.add_radiobutton(
    label="Как в исходном (default)", variable=set_precision, value='default')
precision_menu.add_radiobutton(
    label="До восьми знаков", variable=set_precision, value='five')
precision_menu.add_radiobutton(
    label="Не округлять (только для 8->10)", variable=set_precision, value='not')
precision_menu.entryconfig(2, state=DISABLED)

about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="Автор: Ивахненко Д.А")
about_menu.add_command(label="Группа: ИУ7-26Б")
about_menu.add_command(label="Год: 2020")

main_menu.add_cascade(label="Опции", menu=option_menu)
main_menu.add_cascade(label='Точность', menu=precision_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)

field = Entry(root, font="Segoe 32 bold", width=25, justify=RIGHT, disabledbackground="#0A0A0A",
              disabledforeground='white')
field.insert(END, '0')
field.configure(state=DISABLED)
vsb = Scrollbar(root, orient=HORIZONTAL, command=field.xview)

field.configure(xscrollcommand=vsb.set)

main_btn = Frame(root)
bt = Button(main_btn, text="Перевести", command=lambda x='T': calc('', x), font='Cambria 12 bold', bg='#403A3A',
            fg='white', width=14, height=1, activebackground='#0B5FA4')
bl = Button(main_btn, text="<--", command=lambda x='L': calc('', x), font='Cambria 12 bold', bg='#403A3A', fg='white',
            width=7, height=1, activebackground="#0B5FA4")
bc = Button(main_btn, text='C', command=lambda x='C': calc('', x), width=7, height=1, font='Cambria 12 bold',
            bg='#403A3A', activebackground="#0B5FA4", fg='white')

numpad_F = Frame(root)
b0 = Button(numpad_F, text='0', command=lambda x='0': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b1 = Button(numpad_F, text='1', command=lambda x='1': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b2 = Button(numpad_F, text='2', command=lambda x='2': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b3 = Button(numpad_F, text='3', command=lambda x='3': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b4 = Button(numpad_F, text='4', command=lambda x='4': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b5 = Button(numpad_F, text='5', command=lambda x='5': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b6 = Button(numpad_F, text='6', command=lambda x='6': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b7 = Button(numpad_F, text='7', command=lambda x='7': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b8 = Button(numpad_F, text='8', command=lambda x='8': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
b9 = Button(numpad_F, text='9', command=lambda x='9': calc('', x), width=7, height=2, font='Segoe 14 bold', bg='black',
            activebackground="#0B5FA4", fg='white')
bdot = Button(numpad_F, text='.', command=lambda x='.': calc('', x), width=7, height=2, font='Segoe 14 bold',
              bg='black', activebackground="#0B5FA4", fg='white')
bpm = Button(numpad_F, text='+/-', command=lambda x='-': calc('', x), width=7, height=2, font='Segoe 14 bold',
             bg='black', activebackground="#0B5FA4", fg='white')

state_buttons = Frame(root, bg='#90EE90')
to_oct_btn = Button(state_buttons, bg='#1F75FE', text='10 -> 8', font='Segoe 12 bold', width=13, height=2,
                    activebackground="#0B5FA4", command=lambda x='O': state_control(x), relief=SUNKEN)
to_dec_btn = Button(state_buttons, bg='#DBD7D2', text='8 -> 10', font='Segoe 12 bold', width=13, height=2,
                    activebackground='#0B5FA4', command=lambda x='D': state_control(x))


root.bind('<Control-c>', lambda event, x='CC': calc(event, x))
root.bind('<Control-v>', lambda event, x='CV': calc(event, x))
root.bind('<Delete>', lambda event, x='C': calc(event, x))


root.bind('<Return>', lambda event, x='T': calc(event, x))
root.bind('<BackSpace>', lambda event, x='L': calc(event, x))

root.bind('.', lambda event, x='.': calc(event, x))
root.bind('-', lambda event, x='-': calc(event, x))

buttons = [bt, bl, bc,
           b7, b8, b9,
           b4, b5, b6,
           b1, b2, b3,
           b0, bdot, bpm
           ]

for b in buttons:
    b.bind('<Enter>', lambda event, x='IN', btn=b: change_color(event, x, btn))
    b.bind('<Leave>', lambda event, x='OUT',
           btn=b: change_color(event, x, btn))

for i in range(10):
    root.bind(str(i), lambda event, x=str(i): calc(event, x))


vsb.pack(fill=X)
field.pack(ipady=12)
main_btn.pack()
numpad_F.pack()
state_buttons.pack()
to_oct_btn.pack(side=LEFT)
to_dec_btn.pack(side=LEFT)

r, c = 1, 0
for b in buttons:
    b.grid(row=r, column=c)
    c += 1
    if c == 3:
        r, c = r+1, 0

root.mainloop()
