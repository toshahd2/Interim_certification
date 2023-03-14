notes_file = 'notes.csv'


def read_data():
    noteList = []
    with open(notes_file, 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            noteList.append(temp)
    return noteList
