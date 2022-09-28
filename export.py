def show(request):
    with open('fone.txt', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        count = 0
        for i in data:
            if request in i:
                print(i)
                count +=1
        if count == 0:
            print('Такого номера нет в справочнике.')