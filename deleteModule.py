notes_file = 'notes.csv'


def delete_data(idRequest):
    text = idRequest + ';'
    with open(notes_file,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if text not in line:
                f.write(line)
        f.truncate()