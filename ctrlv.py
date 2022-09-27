def into (str):
    with open('fone.txt', 'a', encoding='utf-8') as f:
        f.write(str + '\n')