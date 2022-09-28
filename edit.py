def change(data):
    with open('fone.txt', 'r', encoding='utf-8') as f1, open('fone.txt', 'w', encoding='utf-8') as f2:
        lines = f1.read().splitlines()
        for i in lines:
            i = i.strip()
            if data in i:
                f2.write(input('Введите новые данны (имя, номер телефона, комментарий): \n'))
            else:
                f2.write(i)