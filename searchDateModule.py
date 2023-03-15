def search_date(year, month, day, data):
    if len(data) > 0:
        date = year + '-' + month + '-' + day
        mylist = []
        for item in data:
            if date in item[3]:
                mylist.append(item)
        if mylist == []:
            return None
        else:
            return mylist
    else:
        return None