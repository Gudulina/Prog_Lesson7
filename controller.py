import input
import ctrlv
import export

def start():
    data = input.choice()
    if data == '1':
        ctrlv.into(input.insert())
    elif data == '2':
        export.show(input.inp_show())
    else:
        print('Такие операции я делать ещё не умею :(')
        print()
        start()