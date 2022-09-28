def choice ():
    str_choice = input('Добавить в справочник новый номер - 1\n'
                    'Показать номер телефона - 2\n'
                    'Что нужно сделать: ')
    return str_choice

def insert ():
    data = input('Введите данные для добавления в справочник: ')
    return data

def inp_show():
    request = input('Введите данные для экспорта: ')
    return request