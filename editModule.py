from datetime import datetime as dt
notes_file = 'notes.csv'


def edit_data(idRequest):
    item = dict()
    item["id"] = idRequest
    item["title"] = input('Введите новый заголовок заметки: ')
    item["note"] = input('Введите новое тело заметки: ')
    item["time"] = dt.now()
    return item


def push_edited_data(idRequest):
    item = edit_data(idRequest)
    rewrite_data([item.get("id"), item.get("title"), item.get("note"), item.get("time")], idRequest)


def rewrite_data(data, idRequest):
    text = idRequest + ';'
    with open(notes_file,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if text in line:
                f.write(";".join(map(str, data)))
                f.write(f"\n")
            else:
                f.write(line)
        f.truncate()