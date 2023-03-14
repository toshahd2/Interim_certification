def print_data(data):
    if len(data) > 0:
        del data[0]
        for content in data:
            print('id: ', content[0], "\n", 'Заголовок: ', content[1], "\n", 'Заметка: ', content[2], "\n", 'Дата изменения: ', content[3], "\n")
    else:
        print("\n")