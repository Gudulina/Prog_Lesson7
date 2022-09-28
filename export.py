def show(request):
    with open('fone.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if request in person:
                print(person)