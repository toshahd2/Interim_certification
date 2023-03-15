from datetime import datetime as dt
notes_file = 'notes.csv'

def edit_data(idRequest):
    item = dict()
    item["id"] = idRequest
    item["title"] = input('Введите новый заголовок заметки: ')
    item["note"] = input('Введите новое тело заметки: ')
    item["time"] = dt.now()
    return item

#def push_edited_data():
    #item = edit_data()
    #rewrite_data([item.get("id"), item.get("title"), item.get("note"), item.get("time")], notes_file)