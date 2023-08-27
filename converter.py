
import re

def date(string):
    splited = string.split('/', maxsplit=3)
    return int(splited[1])

def wknd(string):
    # 0: weekday
    # 1: weekend

    splited = string.split('/', maxsplit=3)
    
    # date converting method
    month = int(splited[0])
    date = int(splited[1])

    if month==9:
        date=date+31
    elif month==10:
        date=date+61
    elif month==11:
        date=date+92
    elif month==12:
        date=date+122
    else:
        pass

    date_r = date-(int(date/7)*7)
    if date_r == 0 or date_r == 6:
        return 1
    else:
        return 0
    
def btconv(string):
    if string == '정기권':
        return 0
    elif string == '단체권':
        return 1
    elif string == '일일권':
        return 2
    elif string == '일일권(비회원)':
        return 3
    else:
        return 'ERROR'
    
def ageconv(string):
    age = re.findall(r'\d+', string)
    return int(age[0])