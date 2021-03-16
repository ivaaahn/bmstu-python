# Лабораторная работа №10
# Выполнил: Ивахненко Дмитрий
# ИУ7-16Б
# Работа с файлами

import os
from pickle import dump, load
from tkinter import *
from tkinter import messagebox as mb

cur_file = None


def hide_show(smth):
    if smth.winfo_viewable():
        smth.grid_remove()
    else:
        smth.grid()


def choose_file_f():
    global choose_file_frame, cur_file
    hide_show(menu_frame)
    hide_show(choose_file_frame)

    def choose_f():
        global cur_file
        file_index = lbox.curselection()[0]
        choosen_file = list_of_files[file_index]
        cur_file = open(choosen_file, 'ab+')
        mb.showinfo("Успешно!", "Выбран файл '" + choosen_file + "'")
        hide_show(choose_file_frame)
        hide_show(menu_frame)

    list_of_files = os.listdir(os.getcwd())

    Label(choose_file_frame, text="Выберите нужный файл").grid(column=1, row=1)

    lbox = Listbox(choose_file_frame, width=20, height=10)
    lbox.grid(column=1, row=2)

    Button(choose_file_frame, text='Выбрать', command=choose_f).grid(column=2, row=2)

    for file in list_of_files:
        lbox.insert(END, file)


def add_file_f():
    global add_file_frame

    def add_f():
        name_new_file = entry.get()
        open(name_new_file, 'w').close()
        mb.showinfo("Успешно!", "Cоздан файл '" + name_new_file + "'")
        hide_show(add_file_frame)
        hide_show(menu_frame)

    hide_show(menu_frame)
    hide_show(add_file_frame)
    entry = Entry(add_file_frame, font=11, width=20)
    entry.grid(row=1, column=0)
    Button(add_file_frame, text='Создать', command=add_f).grid(row=1, column=1)


def print_all_entries_f():
    def ret():
        hide_show(menu_frame)
        hide_show(file_text_frame)

    global cur_file, file_text_frame
    print(type(cur_file))
    hide_show(menu_frame)
    hide_show(file_text_frame)
    text = Text(file_text_frame, width=120, height=25)
    text.grid()
    scroll = Scrollbar(file_text_frame, command=text.yview)
    scroll.grid()
    text.config(yscrollcommand=scroll.set)
    Button(file_text_frame, text="Назад", command=ret).grid()

    def print_entry(entry: dict):
        text.insert(END, '│{:^20}│{:^20}│{:^20}│{:^20}│\n'.format(entry.get('city_name')[:20],
                                                                  entry.get('country_name')[:20],
                                                                  entry.get('travel_cost'), entry.get('rating')))

    def print_header():
        text.insert(END, "┌────────────────────┬────────────────────┬────────────────────┬────────────────────┐\n")
        text.insert(END, '│       Город        │        Страна      │   Стоимость(руб)   │       Рейтинг      │\n')

    def print_footer():
        text.insert(END, "└────────────────────┴────────────────────┴────────────────────┴────────────────────┘")

    cur_file.seek(0)
    try:
        load(cur_file)
        print_header()
        end_of_file = cur_file.seek(0, 2)
        cur_file.seek(0)
        while cur_file.tell() != end_of_file:
            try:
                print_entry(load(cur_file))
            except:
                text.insert(END,
                            '├───────────────────────────────────────────────────────────────────────────────────┤\n')
                text.insert(END,
                            '                        Данную запись прочитать не удалось!                          \n')
        print_footer()
    except:
        text.insert(END, 'Данный файл пуст!\n')


def search_one_field_f():
    print("Здесь скоро что-то будет")


def search_two_field_f():
    print("Здесь скоро что-то будет")


def add_entry_f():
    global cur_file, add_entry_frame

    def add_e():
        global cur_file
        new_entry = {'city_name': city_name_e.get(), 'country_name': country_name_e.get(),
                     'travel_cost': travel_cost_e.get(), 'rating': rating_e.get()}
        print(new_entry)
        dump(new_entry, cur_file)

        hide_show(add_entry_frame)
        hide_show(menu_frame)

    hide_show(menu_frame)
    hide_show(add_entry_frame)
    city_name_l = Label(text='Введите название города')
    city_name_l.grid(column=1, row=0)
    city_name_e = Entry(add_entry_frame, font=11, width=20)
    city_name_e.grid(column=0, row=0)
    country_name_l = Label(text='Введите название страны')
    country_name_l.grid(column=1, row=1)
    country_name_e = Entry(add_entry_frame, font=11, width=20)
    country_name_e.grid(column=0, row=1)
    travel_cost_l = Label(text='Введите стоимость поездки(в рублях)')
    travel_cost_l.grid(column=1, row=2)
    travel_cost_e = Entry(add_entry_frame, font=11, width=20)
    travel_cost_e.grid(column=0, row=2)
    rating_l = Label(text='Введите рейтинг данного города(0/100)')
    rating_l.grid(column=1, row=3)
    rating_e = Entry(add_entry_frame, font=11, width=20)
    rating_e.grid(column=0, row=3)
    Button(add_entry_frame, text='Добавить запиcь', command=add_e).grid(column=2, row=2)


def exit_f():
    print("Здесь скоро что-то будет")


root = Tk()
root.title("Путешествия (version 0.0 alpha)")
root.geometry("800x400")

menu_frame = Frame(root)
menu_frame.grid()
Button(menu_frame, text='Выбрать файл', width='25', height='3', command=choose_file_f).grid(column=1)
Button(menu_frame, text='Создать файл', width='25', height='3', command=add_file_f).grid(column=1)
Button(menu_frame, text='Вывести все записи', width='25', height='3', command=print_all_entries_f).grid(column=1)
Button(menu_frame, text='Поиск по одному полю', width='25', height='3', command=search_one_field_f).grid(column=1)
Button(menu_frame, text='Поиск по двум полям', width='25', height='3', command=search_two_field_f).grid(column=1)
Button(menu_frame, text='Добавить запись', width='25', height='3', command=add_entry_f).grid(column=1)
Button(menu_frame, text='Выход', width='25', height='3', command=exit_f).grid(column=1)

choose_file_frame = Frame(root)
add_file_frame = Frame(root)
file_text_frame = Frame(root)
add_entry_frame = Frame(root)
root.mainloop()


def check_open_file_value_correct(value: str) -> bool:
    try:
        value = int(value)
    except:
        return False
    return 0 <= value <= 1


# Проверка файла на корректность
def check_file_correct() -> bool:
    global cur_file
    end_of_file = cur_file.seek(0, 2)
    cur_file.seek(0)
    while cur_file.tell() != end_of_file:
        try:
            load(cur_file)
        except:
            return False
    return True


# Ф-я, проверяющая корректность типа float
def check_float_correct(num: str) -> bool:
    try:
        float(num)
        return True
    except:
        return False


# Ф-я, проверяющая корректность цифры, обозначающей выбор пользователя в осн.меню
def check_start_value(value: str) -> bool:
    check = True
    try:
        value = int(value)
    except:
        return False

    check = check and 0 <= value <= 6
    check = check and cur_file is not None or (cur_file is None and value in [0, 1, 6])
    if value in [2, 3, 4, 5] and cur_file is None:
        print('Вы не выбрали файл')
    return check


# Ф-я, выполняющая поиск по одному полю
def search_solo():
    global cur_file
    print_search_menu()

    search_type = get_search_type_id()
    key_word = get_search_key_word(search_type)

    end_of_file = cur_file.seek(0, 2)
    header_was_printed = False

    cur_file.seek(0)
    while cur_file.tell() != end_of_file:
        try:
            cur_entry = load(cur_file)

            if check_entry_for_search(cur_entry, search_type, key_word):
                if not header_was_printed:
                    print_header()
                    header_was_printed = True

                print_entry(cur_entry)
        except:
            if header_was_printed:
                print("├───────────────────────────────────────────────────────────────────────────────────┤")
                print('                        Дальнейшее чтение невозможно!                                ')
            break

    if header_was_printed:
        print_footer()
    else:
        print('По вашему запросу ничего не найдено.')


# Получение цифры, показывающей, по какому полю выполняется поиск
def get_search_type_id() -> str:
    search_type_id = input('Введите цифру - по какому полю вы хотите выполнить поиск: ').strip()

    while check_search_id(search_type_id) is False:
        print('Некорректный ввод!')
        search_type_id = input('Введите цифру - по какому полю вы хотите выполнить поиск: ').strip()

    return convert_id_to_type(int(search_type_id))


# Ф-я, выполняющая поиск по двум полям
def search_double():
    global cur_file
    print_search_menu()

    search_types = get_search_types_id()
    key_words = [get_search_key_word(search_types[0]), get_search_key_word(search_types[1])]

    header_was_printed = False
    end_of_file = cur_file.seek(0, 2)

    cur_file.seek(0)
    while cur_file.tell() != end_of_file:
        try:
            cur_entry = load(cur_file)
            if check_entry_for_search(cur_entry, search_types[0], key_words[0]) and \
                    check_entry_for_search(cur_entry, search_types[1], key_words[1]):
                if not header_was_printed:
                    print_header()
                    header_was_printed = True

                print_entry(cur_entry)
        except:
            if header_was_printed:
                print("├───────────────────────────────────────────────────────────────────────────────────┤")
                print('                        Дальнейшее чтение невозможно!                                ')
                break

    if header_was_printed:
        print_footer()
    else:
        print('По вашему запросу ничего не найдено.')


# Получение цифр, показывающей, по каким полям выполняется поиск
def get_search_types_id() -> list:
    first_search_type_id = input('Выберите поле #1: ').strip()
    while check_search_id(first_search_type_id) is False:
        print('Некорректный ввод.')
        first_search_type_id = input('Выберите поле #1: ').strip()

    second_search_type_id = input('Выберите поле #2: ').strip()
    while check_search_id(second_search_type_id) is False or second_search_type_id == first_search_type_id:
        print('Некорректный ввод.')
        second_search_type_id = input('Выберите поле #2: ').strip()

    return [convert_id_to_type(int(first_search_type_id)), convert_id_to_type(int(second_search_type_id))]


# Получение ключевого слова поиска с клавиатуры
def get_search_key_word(search_type: str):
    if search_type is 'city_name':
        key_word = input('Введите название города: ')

    elif search_type is 'country_name':
        key_word = input('Введите название страны: ')

    elif search_type is 'travel_cost':
        key_word = input('Введите верхнюю границу стоимости: ')
        while check_float_correct(key_word) is False:
            print('Вы ввели неверное значение!')
            key_word = input('Введите верхнюю границу стоимости: ')

        key_word = float(key_word)

    else:
        key_word = input('Введите нижнюю границу рейтинга: ')
        while check_float_correct(key_word) is False:
            print('Вы ввели неверное значение!')
            key_word = input('Введите нижнюю границу рейтинга: ')

        key_word = float(key_word)
    return key_word


# Ф-я, выполняющая проверку, содержится ли в записи ключевое слово поиска
def check_entry_for_search(entry: dict, search_type: str, key_word) -> bool:
    if 'name' in search_type:
        return entry.get(search_type).lower() == key_word.lower()
    elif search_type == 'travel_cost':
        return entry.get(search_type) <= key_word
    elif search_type == 'rating':
        return entry.get(search_type) >= key_word
    return False


# Ф-я, конвертирующая цифру, выбранную пользователем в меню поиска в конкретный тип поиска
def convert_id_to_type(search_type_id: int) -> str:
    if search_type_id == 0:
        return 'city_name'
    elif search_type_id == 1:
        return 'country_name'
    elif search_type_id == 2:
        return 'travel_cost'
    else:
        return 'rating'


# Ф-я, печатающая меню поиска
def print_search_menu():
    print(
        '\n0. Город'
        '\n1. Страна'
        '\n2. Стоимость'
        '\n3. Рейтинг')


# Ф-я, проверяющая корректность цифры, обозначающей выбор пользователя в меню поиска
def check_search_id(my_id: str) -> bool:
    try:
        my_id = int(my_id)
    except:
        return False
    return 0 <= my_id <= 4


# Ф-я, создающая файл
def add_file():
    file_name = input('Введите имя нового файла: ').strip()
    try:
        open(file_name, 'rb')
        print('Не удалось создать файл.')
        print('Файл с именем "' + file_name + '" уже существует')

    except FileNotFoundError:
        try:
            open(file_name, 'wb').close()
            print('Вы успешно создали новый файл: "' + file_name + '"')
            return True

        except:
            print('Не удалось создать файл.')
            print('Вы ввели некорректное имя: "' + file_name + '"')

    except:
        print('Не удалось создать файл.')
        print('Вы ввели некорректное имя: "' + file_name + '"')
    return False


# Функция, открывающая файл
def open_file() -> bool:
    global cur_file
    file_name = input('Введите имя нужного файла: ').strip()
    check_exist = False

    while check_exist is False:
        check_exist = True
        try:
            cur_file = open(file_name, 'rb').close()
            cur_file = open(file_name, 'ab+')

        except:
            print('Файл с именем ' + file_name + ' не существует или не доступен для открытия!')
            return False

    print('Вы выбрали файл: ' + file_name)
    return True


# Ф-я, добавляющая запись в файл
def add_entry():
    global cur_file

    city_name = input('Введите название города: ').strip()
    country_name = input('Введите название страны: ').strip()

    travel_cost = input('Введите стоимость поездки(в рублях): ').strip()
    while check_float_correct(travel_cost) is False or float(travel_cost) < 0:
        print('Некорректный ввод')
        travel_cost = input('Введите стоимость поездки(в рублях): ').strip()

    rating = input('Введите рейтинг данного города(0/100): ').strip()
    while check_float_correct(rating) is False or not 0 <= float(rating) <= 100:
        print('Некорректный ввод')
        rating = input('Введите рейтинг данного города(0/100): ').strip()

    new_entry = {'city_name': city_name, 'country_name': country_name, 'travel_cost': float(travel_cost),
                 'rating': float(rating)}
    dump(new_entry, cur_file)


# def print_entry(entry: dict):
#     print("├────────────────────┼────────────────────┼────────────────────┼────────────────────┤")
#     print('│{:^20}│{:^20}│{:^20.5g}│{:^20.5g}│'.format(entry.get('city_name')[:20],
#                                                        entry.get('country_name')[:20], entry.get('travel_cost'),
#                                                        entry.get('rating')))


# # Ф-я, печатающая все строки
# def print_all_entries():
#     global cur_file
#     cur_file.seek(0)
#
#     try:
#         load(cur_file)
#         print_header()
#         end_of_file = cur_file.seek(0, 2)
#         cur_file.seek(0)
#
#         while cur_file.tell() != end_of_file:
#             try:
#                 print_entry(load(cur_file))
#             except:
#                 print('├───────────────────────────────────────────────────────────────────────────────────┤')
#                 print('                        Данную запись прочитать не удалось!                          ')
#
#         print_footer()
#     except:
#         print('Данный файл пуст!')
#
#
# # Ф-я, печатающая названия полей


# Стоимость Ф-я, печатающая основное меню
# def print_main_menu():
#     print("┌───┬──────────────────────┐")
#     print('│ 0 │    Выбрать файл      │')
#     print('├───┼──────────────────────┼')
#     print('│ 1 │    Создать файл      │')
#     print('├───┼──────────────────────┼')
#     print('│ 2 │  Вывести все записи  │')
#     print('├───┼──────────────────────┼')
#     print('│ 3 │ Поиск по одному полю │')
#     print('├───┼──────────────────────┼')
#     print('│ 4 │ Поиск по двум полям  │')
#     print('├───┼──────────────────────┼')
#     print('│ 5 │   Добавить запись    │')
#     print('├───┼──────────────────────┼')
#     print('│ 6 │       Выход          │')
#     print('└───┴──────────────────────┘')


# Получить стартовое значение
# def get_start_value() -> str:
#     return input('Выберите нужный пункт: ')


# Основная функция
# def start():
#     global cur_file
#
#     print_main_menu()
#     cur_value = get_start_value()
#
#     if check_start_value(cur_value) is False:
#         print('Введено некорректное значение. '
#               '\nПожалуйста, попробуйте снова.')
#         return True
#
#     cur_value = int(cur_value)
#
#     if cur_value == 0:
#         choice = open_file()
#         if choice is True and check_file_correct() is False:
#             print('Невозможно считать файл')
#
#     elif cur_value == 1:
#         add_file()
#     elif cur_value == 2:
#         print_all_entries()
#     elif cur_value == 3:
#         search_solo()
#     elif cur_value == 4:
#         search_double()
#     elif cur_value == 5:
#         add_entry()
#     else:
#         return False
#     return True


if cur_file is not None:
    cur_file.close()
