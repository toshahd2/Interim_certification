from addModule import *
from readModule import *
from printModule import *

def start():
    print("Выберите команду приложения:\n\
    1. Показать все заметки.\n\
    2. Добавить новую заметку.\n\
    3. Изменить заметку.\n\
    4. Удалить заметку.")
    mode = input("Введите номер команды: ")
    while True:
        if mode == '1':
            data = read_data()
            print_data(data)
            start()
        elif mode == '2':
            push_data()
            print("Заметка сохранена.")
            start()
        elif mode == '3':
            print("Заметка сохранена.")
            start()
        elif mode == '4':
            print("Заметка удалена.")
            start()
        else:
            print("Вы ввели некорректную цифру, повторите ввод команды: ")
            start()