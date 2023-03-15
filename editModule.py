from datetime import datetime as dt
notes_file = 'notes.csv'

def edit_data(idRequest):
    item = dict()
    identifier = idRequest
    item["id"] = identifier
    item["title"] = input('Введите новый заголовок заметки: ')
    item["note"] = input('Введите новое тело заметки: ')
    item["time"] = dt.now()
    return item