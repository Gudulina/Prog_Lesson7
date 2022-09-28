def into (data):
    with open('fone.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')