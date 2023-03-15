from addModule import *
from readModule import *
from printModule import *
from searchIdModule import *


def start():
    print("Выберите команду приложения:\n\
    1. Показать все заметки.\n\
    2. Показать заметки в диапазоне дат.\n\
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
            print("Заметка сохранена.")
            start()
        elif mode == '6':
            print("Заметка удалена.")
            start()
        else:
            print("Вы ввели некорректную цифру, повторите ввод команды: ")
            start()
