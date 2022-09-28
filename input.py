def choice ():
    str_choice = input('Добавить в справочник новый номер - 1\n'
                    'Показать номер телефона - 2\n'
                    'Редактировать имя - 3\n'
                    'Что нужно сделать: ')
    return str_choice

def insert ():
    data = input('Введите данные для добавления в справочник: ')
    return data

def inp_show():
    request = input('Введите данные для экспорта: ')
    return request

def inp_edit():
    data = input('Чей номер изменить: ')
    return data

def exp_edit():
    new_data = input('Введите новое имя: ')
    return new_data