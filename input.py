def choice (str):
    str_choice = input('Добавить в справочник новый номер - 1\n'
                    'Показать номер - 2\n'
                    'Что нужно сделать: ')
    return str_choice

def insert (str):
    data = input('Введите данные для добавления в справочник: ')
    return data

def inp_show(str):
    request = input('Введите данные для экспорта: ')
    return request