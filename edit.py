def change(data, new_data):
    with open('fone.txt', 'rt', encoding='utf-8') as f:
        lines = f.read()
                
    with open("fone.txt", 'wt', encoding='utf-8') as f:
        lines = lines.replace(data, new_data)
        f.write(lines)