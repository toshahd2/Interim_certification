from datetime import datetime as dt
notes_file = 'notes.csv'

def input_data():
    item = dict()
    identifier = count_data(notes_file)
    item["id"] = identifier
    item["title"] = input('Введите заголовок заметки: ')
    item["note"] = input('Введите тело заметки: ')
    item["time"] = dt.now()
    return item


def count_data(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')


def write_data(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")


def push_data():
    item = input_data()
    write_data([item.get("id"), item.get("title"), item.get("note"), item.get("time")], notes_file)
