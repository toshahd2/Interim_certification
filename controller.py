from addModule import *
from readModule import *
from printModule import *
from searchIdModule import *
from searchDateModule import *
from deleteModule import *


def start():
    print("Выберите команду приложения:\n\
    1. Показать все заметки.\n\
    2. Показать заметки отпределённой даты создания/изменения.\n\
    3. Показать заметку по номеру ID.\n\
    4. Добавить новую заметку.\n\
    5. Изменить заметку по номеру ID.\n\
    6. Удалить заметку по номеру ID.")
    mode = input("Введите номер команды: ")
    while True:
        if mode == '1':
            data = read_data()
            print_data(data)
            start()
        elif mode == '2':
            year = input("Введите год целиком (напр. 2023) для поиска заметки: ")
            month = input("Введите месяц (2 цифры, напр. 02) для поиска заметки: ")
            day = input("Введите день (2 цифры, напр. 05) для поиска заметки: ")
            data = read_data()
            item = search_date(year, month, day, data)
            if item != None:
                print_data(item, True)
            else:
                print("Заметка не найдена.")
            start()
        elif mode == '3':
            idRequest = input("Введите ID для поиска заметки: ")
            data = read_data()
            item = search_data(idRequest, data)
            if item != None:
                print_data(item, True)
            else:
                print("ID не найден.")
            start()
        elif mode == "4":
            push_data()
            print("Заметка сохранена.")
            start()
        elif mode == '5':
            idRequest = input("Введите ID заметки для изменения заметки: ")
            data = read_data()
            item = search_data(idRequest, data)
            if item != None:
                print_data(item, True)
                print("Заметка сохранена.")
            else:
                print("ID не найден.")
            start()
        elif mode == '6':
            idRequest = input("Введите ID заметки для ее удаления: ")
            data = read_data()
            item = search_data(idRequest, data)
            if item != None:
                delete_data(idRequest)
                print("Заметка удалена.")
            else:
                print("ID не найден.")
            start()
        else:
            print("Вы ввели некорректную цифру, повторите ввод команды: ")
            start()
