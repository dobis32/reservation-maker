from datetime import datetime
def getTodayString():
    today = datetime.now()
    month = None
    if today.month < 10:
        month = '0' + str(today.month) # add padding zero
    else:
        month = str(today.month)

    day = None
    if today.day < 10:
        day = '0' + str(today.day) # add padding zero
    else:
        day = str(today.day)
    date = '{month}-{day}-{year}'.format(month= month, day = day, year = today.year - 2000)
    return date