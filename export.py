def show():
    with open('fone.txt', 'r', encoding='utf-8') as f:
        print(f.readline())